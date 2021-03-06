"""
The file is generated by scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""



from src.application.lookup.common.model_data.BaseLookupModel import BaseLookupModel
from src.application.lookup.common.model_data.LookupModelAttributeData import LookupModelAttributeData
from src.domain_model.common.HasToMap import HasToMap
from src.application.lookup.equipment.MaintenanceProcedureOperationParameter import MaintenanceProcedureOperationParameter
from src.application.lookup.equipment.MaintenanceProcedureOperationLabel import MaintenanceProcedureOperationLabel

class MaintenanceProcedureOperation(HasToMap, BaseLookupModel):
    __slots__ = [
        "id",
        "name",
        "description",
        "type",
        "maintenanceProcedureOperationParameters",
        "maintenanceProcedureOperationLabels",
    ]

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def toMap(self) -> dict:
        return super()._toMap(MaintenanceProcedureOperation.attributes())

    def _attributeValue(self, classAttribute):
        return super()._attributeValue(classAttribute)

    @classmethod
    def attributes(cls):
        return {
            "id":LookupModelAttributeData(),
            "name":LookupModelAttributeData(),
            "description":LookupModelAttributeData(),
            "type":LookupModelAttributeData(),
            "maintenanceProcedureOperationParameters":LookupModelAttributeData(
                    dataType=MaintenanceProcedureOperationParameter, isClass=True, isArray=True
                ),
            "maintenanceProcedureOperationLabels":LookupModelAttributeData(
                    dataType=MaintenanceProcedureOperationLabel, isClass=True, isArray=True
                ),
        }

    def __repr__(self):
        return f"<{self.__module__} object at {hex(id(self))}> {self.toMap()}"

    def __str__(self) -> str:
        return f"<{self.__module__} object at {hex(id(self))}> {self.toMap()}"
