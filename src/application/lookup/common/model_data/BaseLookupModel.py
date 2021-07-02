"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from src.application.lookup.common.model_data.LookupModelAttributeData import LookupModelAttributeData
from src.resource.common.Util import Util


class BaseLookupModel:
    def _toMap(self, classAttributes) -> dict:
        result = {}
        lookupModelAttributeData: LookupModelAttributeData
        for classAttributeKey, lookupModelAttributeData in classAttributes.items():
            toMapAttributeValue = self._attributeValue(
                Util.snakeCaseToLowerCameCaseString(classAttributeKey)
            )
            if lookupModelAttributeData.isClass:
                if lookupModelAttributeData.isArray and toMapAttributeValue is not None:
                    result[classAttributeKey] = [x.toMap() for x in toMapAttributeValue]
                else:
                    toMapValue = toMapAttributeValue.toMap() if toMapAttributeValue is not None else None
                    result[classAttributeKey] = toMapValue
            else:
                result[classAttributeKey] = toMapAttributeValue
        return result

    def _attributeValue(self, classAttribute):
        return getattr(self, classAttribute, None)

    @classmethod
    def attributes(cls) -> dict:
        pass
