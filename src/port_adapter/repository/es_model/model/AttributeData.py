"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import Any


class AttributeData:
    def __init__(self, attributeModelName: str = None, attributeRepoName: str = None, attributeRepoValue: Any = None, dataType: type = str, isInnerClass: bool = False):
        self.attributeModelName = attributeModelName
        self.attributeRepoName = attributeRepoName
        self.attributeRepoValue = attributeRepoValue
        self.dataType = dataType
        self.isInnerClass = isInnerClass


    def __repr__(self):
        return f'attribute_model_name": {self.attributeModelName}, "attribute_repo_name": {self.attributeRepoName}, "attribute_repo_value": {self.attributeRepoValue}, \
                "data_type": {self.dataType}, "is_inner_class": {self.isInnerClass}'
