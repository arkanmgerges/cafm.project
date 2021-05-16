"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import json
import os
from time import sleep

from src.domain_model.event.DomainPublishedEvents import DomainPublishedEvents
from src.domain_model.resource.exception.DomainModelException import (
    DomainModelException,
)
from src.port_adapter.messaging.common.model.IdentityFailedEventHandle import IdentityFailedEventHandle
from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand
from src.port_adapter.messaging.common.model.ProjectEvent import ProjectEvent
from src.port_adapter.messaging.listener.common.CommonListener import CommonListener
from src.port_adapter.messaging.listener.common.ProcessHandleData import ProcessHandleData
from src.port_adapter.messaging.listener.common.resource.exception.FailedMessageHandleException import (
    FailedMessageHandleException,
)
from src.resource.logging.logger import logger


class IdentityEventListener(CommonListener):
    def __init__(self):
        super().__init__(
            creatorServiceName=os.getenv("CAFM_PROJECT_SERVICE_NAME", "cafm.project"),
            handlersPath=f"{os.path.dirname(os.path.abspath(__file__))}/handler/**/*.py",
        )

    def run(self):
        self._process(
            consumerGroupId=os.getenv(
                "CAFM_PROJECT_CONSUMER_GROUP_IDENTITY_EVT_NAME",
                "cafm.project.consumer-group.identity.evt",
            ),
            consumerTopicList=[os.getenv("CAFM_IDENTITY_EVENT_TOPIC", "")],
        )

    def _processHandledResult(self, processHandleData: ProcessHandleData):
        handledResult = processHandleData.handledResult
        messageData = processHandleData.messageData
        producer = processHandleData.producer
        try:
            if handledResult is None:  # Consume the offset since there is no handler for it
                logger.info(
                    f'[{IdentityEventListener.run.__qualname__}] Command handle result is None, The offset is consumed for handleCommand(name={messageData["name"]}, data={messageData["data"]}, metadata={messageData["metadata"]})'
                )
                return

            logger.debug(f"[{IdentityEventListener.run.__qualname__}] handleResult returned with: {handledResult}")

            # Produce to project command
            if "external" in messageData:
                external = messageData["external"]
            else:
                external = []

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
        except DomainModelException as e:
            logger.warn(e)
            processHandleData.isSuccess = False
            processHandleData.exception = e
            DomainPublishedEvents.cleanup()
        except Exception as e:
            # Send the failed message to the failed topic
            DomainPublishedEvents.cleanup()
            isMessageProduced = False
            logger.error(e)
            while not isMessageProduced:
                try:
                    self._produceToFailedTopic(processHandleData=processHandleData)
                    isMessageProduced = True
                except Exception as e:
                    logger.error(e)
                    sleep(1)
            raise FailedMessageHandleException(message=f"Failed message: {processHandleData.messageData}")

    def _processHandleCommand(self, processHandleData: ProcessHandleData):
        try:
            return super()._handleCommand(processHandleData=processHandleData)
        except DomainModelException as e:
            logger.warn(e)
            DomainPublishedEvents.cleanup()
            processHandleData.exception = e
            processHandleData.isSuccess = False
        except Exception as e:
            # Send the failed message to the failed topic
            DomainPublishedEvents.cleanup()
            isMessageProduced = False
            logger.error(e)
            while not isMessageProduced:
                try:
                    self._produceToFailedTopic(processHandleData=processHandleData)
                    isMessageProduced = True
                except Exception as e:
                    logger.error(e)
                    sleep(1)
            raise FailedMessageHandleException(message=f"Failed message: {processHandleData.messageData}")

    def _produceToFailedTopic(self, processHandleData: ProcessHandleData):
        messageData = processHandleData.messageData
        producer = processHandleData.producer
        consumer = processHandleData.consumer
        external = []
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
        producer.produce(
            obj=IdentityFailedEventHandle(
                id=messageData["id"],
                creatorServiceName=self._creatorServiceName,
                name=messageData["name"],
                metadata=messageData["metadata"],
                data=messageData["data"],
                createdOn=messageData["created_on"],
                external=external,
            ),
            schema=ProjectEvent.get_schema(),
        )
        producer.sendOffsetsToTransaction(consumer)
        producer.commitTransaction()
        producer.beginTransaction()


IdentityEventListener().run()
