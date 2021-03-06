"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import os
import threading
from copy import copy
from time import sleep

from src.domain_model.event.DomainPublishedEvents import DomainPublishedEvents
from src.domain_model.resource.exception.DomainModelException import (
    DomainModelException,
)
from src.port_adapter.messaging.common.model.LookupProjectFailedEventHandle import LookupProjectFailedEventHandle
from src.port_adapter.messaging.common.model.ProjectEvent import ProjectEvent
from src.port_adapter.messaging.listener.common.CommonListener import CommonListener
from src.port_adapter.messaging.listener.common.ProcessHandleData import ProcessHandleData
from src.port_adapter.messaging.listener.common.resource.exception.FailedMessageHandleException import (
    FailedMessageHandleException,
)
from src.resource.logging.LogProcessor import LogProcessor
from src.resource.logging.logger import logger


class LookupProjectEventListener(CommonListener):
    def __init__(self):
        super().__init__(
            creatorServiceName=os.getenv("CAFM_PROJECT_SERVICE_NAME", "cafm.project"),
            handlersPath=f"{os.path.dirname(os.path.abspath(__file__))}/handler/**/*.py",
        )

    def run(self):
        self._process(
            consumerGroupId=os.getenv("CAFM_PROJECT_CONSUMER_GROUP_LOOKUP_PROJECT_EVENT_NAME", ""),
            consumerTopicList=[os.getenv("CAFM_PROJECT_EVENT_TOPIC", "")],
        )

    def _processHandledResult(self, processHandleData: ProcessHandleData):
        handledResult = processHandleData.handledResult
        messageData = processHandleData.messageData
        try:
            if handledResult is None:  # Consume the offset since there is no handler for it
                logger.info(
                    f'[{LookupProjectEventListener.run.__qualname__}] Command handle result is None, The offset is consumed for handleMessage(name={messageData["name"]}, data={messageData["data"]}, metadata={messageData["metadata"]})'
                )
                return

            logger.debug(
                f"[{LookupProjectEventListener.run.__qualname__}] handleResult returned with: {handledResult}"
            )

            logger.debug(f"[{LookupProjectEventListener.run.__qualname__}] cleanup event publisher")
            processHandleData.isSuccess = True
            DomainPublishedEvents.cleanup()

        except DomainModelException as e:
            logger.warn(e)
            DomainPublishedEvents.cleanup()
            processHandleData.exception = e
            processHandleData.isSuccess = False

        except Exception as e:
            # Send the failed message to the failed topic
            DomainPublishedEvents.cleanup()
            isMessageProduced = False
            if getattr(e, 'info', None) is not None:
                logger.error(e.info)
            logger.error(e)
            while not isMessageProduced:
                try:
                    self._produceToFailedTopic(processHandleData=processHandleData)
                    isMessageProduced = True
                except Exception as e:
                    logger.error(e)
                    sleep(1)
            raise FailedMessageHandleException(message=f"Failed message: {processHandleData.messageData}")

    def _processHandleMessage(self, processHandleData: ProcessHandleData):
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
        except Exception as e:
            # Send the failed message to the failed topic
            DomainPublishedEvents.cleanup()
            isMessageProduced = False
            if getattr(e, 'info', None) is not None:
                logger.error(e.info)
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

        producer.produce(
            obj=LookupProjectFailedEventHandle(
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

# region Logger
import src.resource.Di as Di
logProcessor = Di.instance.get(LogProcessor)
thread = threading.Thread(target=logProcessor.start)
thread.start()
# endregion
LookupProjectEventListener().run()
