"""
The file is generated by scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""



from src.application.lookup.model_data.BaseLookupModel import BaseLookupModel
from src.application.lookup.model_data.LookupModelAttributeData import LookupModelAttributeData
from src.domain_model.common.HasToMap import HasToMap
from src.application.lookup.daily_check_procedure.EquipmentCategoryGroup import EquipmentCategoryGroup
from src.application.lookup.daily_check_procedure.DailyCheckProcedureOperation import DailyCheckProcedureOperation

class DailyCheckProcedure(HasToMap, BaseLookupModel):
    __slots__ = [
        "id",
        "name",
        "description",
        "equipmentId",
        "equipmentCategoryGroup",
        "dailyCheckProcedureOperations",
    ]

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def toMap(self) -> dict:
        return super()._toMap(DailyCheckProcedure.attributes())

    def _attributeValue(self, classAttribute):
        return super()._attributeValue(classAttribute)

    @classmethod
    def attributes(cls):
        return {
            "id":LookupModelAttributeData(),
            "name":LookupModelAttributeData(),
            "description":LookupModelAttributeData(),
            "equipmentId":LookupModelAttributeData(),
            "equipmentCategoryGroup":LookupModelAttributeData(
                    dataType=EquipmentCategoryGroup, isClass=True
                ),
            "dailyCheckProcedureOperations":LookupModelAttributeData(
                    dataType=DailyCheckProcedureOperation, isClass=True, isArray=True
                ),
        }

    def __repr__(self):
        return f"<{self.__module__} object at {hex(id(self))}> {self.toMap()}"

    def __str__(self) -> str:
        return f"<{self.__module__} object at {hex(id(self))}> {self.toMap()}"