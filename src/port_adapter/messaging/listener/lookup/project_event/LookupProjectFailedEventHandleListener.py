"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import os
from copy import copy
from time import sleep

from src.domain_model.event.DomainPublishedEvents import DomainPublishedEvents
from src.domain_model.resource.exception.DomainModelException import (
    DomainModelException,
)
from src.port_adapter.messaging.listener.common.CommonListener import CommonListener
from src.port_adapter.messaging.listener.common.ProcessHandleData import ProcessHandleData
from src.resource.logging.logger import logger


class LookupProjectFailedEventHandleListener(CommonListener):
    def __init__(self):
        super().__init__(
            creatorServiceName=os.getenv("CAFM_PROJECT_SERVICE_NAME", "cafm.project"),
            handlersPath=f"{os.path.dirname(os.path.abspath(__file__))}/handler/**/*.py",
        )

    def run(self):
        self._process(
            consumerGroupId=os.getenv("CAFM_PROJECT_CONSUMER_GROUP_PROJECT_FAILED_LOOKUP_EVENT_HANDLE_NAME", "cafm.project.consumer-group.failed-lookup-evt-handle"),
            consumerTopicList=[os.getenv("CAFM_PROJECT_FAILED_LOOKUP_EVENT_HANDLE_TOPIC", "cafm.project.failed-lookup-evt-handle")],
        )

    def _processHandledResult(self, processHandleData: ProcessHandleData):
        handledResult = processHandleData.handledResult
        messageData = processHandleData.messageData
        isMessageProcessed = False
        while not isMessageProcessed:
            try:
                if handledResult is None:  # Consume the offset since there is no handler for it
                    logger.info(
                        f'[{LookupProjectFailedEventHandleListener.run.__qualname__}] Command handle result is None, The '
                        f'offset is consumed for handleMessage(name={messageData["name"]}, data='
                        f'{messageData["data"]}, metadata={messageData["metadata"]})'
                    )
                    return

                logger.debug(
                    f"[{LookupProjectFailedEventHandleListener.run.__qualname__}] handleResult "
                    f"returned with: {handledResult}"
                )

                logger.debug(f"[{LookupProjectFailedEventHandleListener.run.__qualname__}] cleanup event publisher")
                processHandleData.isSuccess = True
                DomainPublishedEvents.cleanup()
                isMessageProcessed = True

            except DomainModelException as e:
                logger.warn(e)
                DomainPublishedEvents.cleanup()
                processHandleData.exception = e
                processHandleData.isSuccess = False
                isMessageProcessed = True
            except Exception as e:
                if getattr(e, 'info', None) is not None:
                    logger.error(e.info)
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
            except Exception as e:
                # Send the failed message to the failed topic
                DomainPublishedEvents.cleanup()
                if getattr(e, 'info', None) is not None:
                    logger.error(e.info)
                logger.error(e)
                sleep(1)

LookupProjectFailedEventHandleListener().run()
