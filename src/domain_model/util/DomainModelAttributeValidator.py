"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from src.domain_model.common.HasToMap import HasToMap
from src.domain_model.resource.exception.InvalidAttributeException import InvalidAttributeException


class DomainModelAttributeValidator:
    @staticmethod
    def validate(domainModelObject: HasToMap, attributeDictionary: dict, attributeExclusionList: List[str] = None):
        attributeExclusionList = attributeExclusionList if attributeExclusionList is not None else []
        mapDict = domainModelObject.toMap()
        invalidAttributes = []
        for attributeItem in attributeDictionary.keys():
            if attributeItem not in attributeExclusionList and attributeItem not in mapDict:
                invalidAttributes.append(attributeItem)

        if len(invalidAttributes) > 0:
            raise InvalidAttributeException(message=f'Invalid attributes: {",".join(invalidAttributes)}, valid model attributes: {",".join(mapDict.keys())}')