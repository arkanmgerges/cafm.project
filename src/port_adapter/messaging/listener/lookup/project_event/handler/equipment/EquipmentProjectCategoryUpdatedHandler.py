"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""


from src.port_adapter.messaging.listener.common.handler.lookup.equipment.UpdateEquipmentProjectCategoryHandler import \
    UpdateEquipmentProjectCategoryHandler as Handler


class EquipmentProjectCategoryUpdatedHandler(Handler):
    def canHandle(self, name: str) -> bool:
        from src.domain_model.event.EventConstant import CommonEventConstant
        return name == CommonEventConstant.EQUIPMENT_PROJECT_CATEGORY_UPDATED.value

    def handleMessage(self, messageData: dict, extraData: dict = None) -> dict:
        import json
        messageData['data'] = json.dumps(json.loads(messageData['data'])['new'])
        return super().handleMessage(messageData=messageData, extraData=extraData)