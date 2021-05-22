"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from src.resource.common.Util import Util


class BaseLookupModel:
    def _toMap(self, classAttributes) -> dict:
        result = {}
        for classAttributeKey, lookupAttributeData in classAttributes.items():
            if lookupAttributeData.isLookupClass:
                result[classAttributeKey] = self._attributeValue(
                    Util.snakeCaseToLowerCameCaseString(classAttributeKey)
                ).toMap()
            else:
                result[classAttributeKey] = self._attributeValue(Util.snakeCaseToLowerCameCaseString(classAttributeKey))
        return result

    def _attributeValue(self, classAttribute):
        return getattr(self, classAttribute, None)

    @classmethod
    def attributes(cls) -> dict:
        pass
