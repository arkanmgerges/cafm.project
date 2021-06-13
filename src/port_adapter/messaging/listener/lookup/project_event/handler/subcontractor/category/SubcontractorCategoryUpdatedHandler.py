"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from src.port_adapter.messaging.listener.common.handler.lookup.subcontractor.category.UpdateSubcontractorCategoryHandler import (
    UpdateSubcontractorCategoryHandler as Handler,
)


class SubcontractorCategoryUpdatedHandler(Handler):
    def canHandle(self, name: str) -> bool:
        from src.domain_model.event.EventConstant import CommonEventConstant
        return name == CommonEventConstant.SUBCONTRACTOR_CATEGORY_UPDATED.value

    def handleMessage(self, messageData: dict, extraData: dict = None) -> dict:
        import json
        messageData['data'] = json.dumps(json.loads(messageData['data'])['new'])
        return super().handleMessage(messageData=messageData, extraData=extraData)