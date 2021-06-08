"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from src.port_adapter.messaging.listener.common.handler.lookup.subcontractor.CreateSubcontractorHandler import (
    CreateSubcontractorHandler as Handler,
)

class SubcontractorCreatedHandler(Handler):
    def canHandle(self, name: str) -> bool:
        from src.domain_model.event.EventConstant import CommonEventConstant
        return name == CommonEventConstant.SUBCONTRACTOR_CREATED.value
