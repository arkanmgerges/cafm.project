"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List, Any, Callable


class BaseApplicationServiceBulkData:
    def __init__(
        self,
        objListParams: List[dict] = None,
        token: str = None,
        sourceId: str = None,
        domainService: Any = None,
        repositoryCallbackFunction: Callable = None,
    ):
        self.objListParams: List[dict] = objListParams
        self.token: str = token
        self.sourceId: str = sourceId
        self.domainService: Callable = domainService
        self.repositoryCallbackFunction: Callable = repositoryCallbackFunction
