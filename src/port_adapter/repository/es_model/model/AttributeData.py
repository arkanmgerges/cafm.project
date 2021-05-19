"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import Any


class AttributeData:
    def __init__(self, modelName: str = None, repoName: str = None, repoValue: Any = None, dataType: str = "str"):
        self.modelName = modelName
        self.repoName = repoName
        self.repoValue = repoValue
        self.dataType = dataType
