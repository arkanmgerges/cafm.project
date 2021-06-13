"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import json
import os
from copy import copy
from time import sleep

from src.domain_model.event.DomainPublishedEvents import DomainPublishedEvents
from src.domain_model.resource.exception.DomainModelException import (
    DomainModelException,
)
from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand
from src.port_adapter.messaging.listener.common.CommonListener import CommonListener
from src.port_adapter.messaging.listener.common.ProcessHandleData import ProcessHandleData
from src.port_adapter.repository.resource.exception.IntegrityErrorRepositoryException import \
    IntegrityErrorRepositoryException
from src.resource.logging.logger import logger


class IdentityFailedEventHandleListener(CommonListener):
    def __init__(self):
        super().__init__(
            creatorServiceName=os.getenv("CAFM_PROJECT_SERVICE_NAME", "cafm.project"),
            handlersPath=f"{os.path.dirname(os.path.abspath(__file__))}/handler/**/*.py",
        )

    def run(self):
        self._process(
            consumerGroupId=os.getenv(
                "CAFM_PROJECT_CONSUMER_GROUP_IDENTITY_FAILED_EVT_HANDLE_NAME",
                "cafm.project.consumer-group.identity-failed-evt-handle",
            ),
            consumerTopicList=[os.getenv("CAFM_PROJECT_IDENTITY_FAILED_EVENT_HANDLE_TOPIC", "cafm.project.identity-failed-evt-handle")],
        )

    def _processHandledResult(self, processHandleData: ProcessHandleData):
        handledResult = processHandleData.handledResult
        messageData = processHandleData.messageData
        producer = processHandleData.producer
        isMessageProcessed = False
        while not isMessageProcessed:
            try:
                external = []
                # Produce to project command
                if "external" in messageData:
                    external = messageData["external"]

                external.append(
                    {
                        "id": messageData["id"],
                        "creator_service_name": messageData["creator_service_name"],
                        "name": messageData["name"],
                        "version": messageData["version"],
                        "metadata": messageData["metadata"],
                        "data": messageData["data"],
                        "created_on": messageData["created_on"],
                    }
                )

                if handledResult is None:  # Consume the offset since there is no handler for it
                    logger.info(
                        f"[{IdentityFailedEventHandleListener.run.__qualname__}] Command handle result is None, "
                        f"The offset is consumed "
                        f'for handleMessage(name={messageData["name"]}, data={messageData["data"]}, '
                        f'metadata={messageData["metadata"]})'
                    )
                    self._produceDomainEvents(producer=producer, messageData=messageData, external=external)
                    return

                logger.debug(
                    f"[{IdentityFailedEventHandleListener.run.__qualname__}] handleResult returned with: {handledResult}"
                )
                self._produceDomainEvents(producer=producer, messageData=messageData, external=external)
                producer.produce(
                    obj=ProjectCommand(
                        id=messageData["id"],
                        creatorServiceName=self._creatorServiceName,
                        name=handledResult["name"],
                        metadata=messageData["metadata"],
                        data=json.dumps(handledResult["data"]),
                        createdOn=handledResult["created_on"],
                        external=external,
                    ),
                    schema=ProjectCommand.get_schema(),
                )

                processHandleData.isSuccess = True
                isMessageProcessed = True
            except DomainModelException as e:
                logger.warn(e)
                processHandleData.isSuccess = False
                processHandleData.exception = e
                DomainPublishedEvents.cleanup()
                isMessageProcessed = True
            except IntegrityErrorRepositoryException as e:
                logger.warn(e)
                DomainPublishedEvents.cleanup()
                processHandleData.exception = e
                processHandleData.isSuccess = False
                isMessageProcessed = True
            except Exception as e:
                DomainPublishedEvents.cleanup()
                logger.error(e)
                sleep(1)

    def _processHandleMessage(self, processHandleData: ProcessHandleData):
        isMessageProcessed = False
        while not isMessageProcessed:
            try:
                # Sometimes we are modifying messageData['data'], e.g. on update we are using 'new' and overwrite
                # messageData['data'], that is why we need to send a copy
                processHandleDataCopy = copy(processHandleData)
                processHandleDataCopy.messageData = copy(processHandleData.messageData)
                return super()._handleMessage(processHandleData=processHandleDataCopy)
            except DomainModelException as e:
                logger.warn(e)
                DomainPublishedEvents.cleanup()
                processHandleData.exception = e
                processHandleData.isSuccess = False
                isMessageProcessed = True
            except IntegrityErrorRepositoryException as e:
                logger.warn(e)
                DomainPublishedEvents.cleanup()
                processHandleData.exception = e
                processHandleData.isSuccess = False
                isMessageProcessed = True
            except Exception as e:
                # Send the failed message to the failed topic
                DomainPublishedEvents.cleanup()
                logger.error(e)
                sleep(1)


IdentityFailedEventHandleListener().run()
