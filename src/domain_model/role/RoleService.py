"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from abc import ABC, abstractmethod
from typing import List, Tuple
from src.domain_model.role.Role import Role
from src.domain_model.role.RoleRepository import RoleRepository
from src.domain_model.token.TokenData import TokenData
from src.resource.logging.decorator import debugLogger


class RoleService(ABC):
    @debugLogger
    def createRole(
        self, obj: Role, objectOnly: bool = False, tokenData: TokenData = None
    ):
        if objectOnly:
            return (
                Role.createFromObject(obj=obj, generateNewId=True)
                if obj.id() == ""
                else obj
            )
        else:
            obj: Role = Role.createFromObject(obj=obj, publishEvent=True)
            self._repo.save(obj=obj)
            return obj

    @debugLogger
    def deleteRole(self, obj: Role, tokenData: TokenData = None):
        obj.publishDelete()
        self._repo.deleteRole(obj=obj)

    @debugLogger
    def updateRole(self, oldObject: Role, newObject: Role, tokenData: TokenData = None):
        newObject.publishUpdate(oldObject)
        self._repo.save(obj=newObject)

    @debugLogger
    def bulkCreate(self, objList: List[Role]):
        self._repo.bulkSave(objList=objList)
        for obj in objList:
            Role.createFromObject(obj=obj, publishEvent=True)

    @debugLogger
    def bulkDelete(self, objList: List[Role]):
        self._repo.bulkDelete(objList=objList)
        for obj in objList:
            obj.publishDelete()

    @debugLogger
    def bulkUpdate(self, objList: List[Tuple]):
        newObjList = list(map(lambda x: x[0], objList))
        self._repo.bulkSave(objList=newObjList)
        for obj in objList:
            newObj = obj[0]
            oldObj = obj[1]
            newObj.publishUpdate(oldObj)

    @debugLogger
    @abstractmethod
    def roles(
        self,
        tokenData: TokenData = None,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
    ):
        pass

    @debugLogger
    @abstractmethod
    def rolesByOrganizationType(
        self,
        organizationType: str = None,
        tokenData: TokenData = None,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
    ):
        pass

    @debugLogger
    @abstractmethod
    def rolesByTagName(
        self,
        tagName: str = None,
        tokenData: TokenData = None,
    ):
        pass
