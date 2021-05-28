"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import Any, Union


class EsModelAttributeData:
    from elasticsearch_dsl import Document

    def __init__(
        self,
        attributeModelName: str = None,
        attributeRepoName: str = None,
        attributeRepoValue: Any = None,
        dataType: Union[Document, type] = str,
        isClass: bool = False,
        isArray: bool = False,
    ):
        self.attributeModelName = attributeModelName
        self.attributeRepoName = attributeRepoName
        self.attributeRepoValue = attributeRepoValue
        self.dataType = dataType
        self.isClass = isClass
        self.isArray = isArray

    def __repr__(self):
        return f'attribute_model_name": {self.attributeModelName}, "attribute_repo_name": {self.attributeRepoName}, "attribute_repo_value": {self.attributeRepoValue}, \
                "data_type": {self.dataType}, "is_class": {self.isClass}, "is_array": {self.isArray}'
