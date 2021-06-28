"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from abc import ABC, abstractmethod
from typing import List, Tuple

from src.domain_model.project.Project import Project
from src.domain_model.token.TokenData import TokenData
from src.resource.logging.decorator import debugLogger


class ProjectService(ABC):
    @debugLogger
    def createProject(
        self, obj: Project, objectOnly: bool = False, tokenData: TokenData = None
    ):
        if objectOnly:
            return (
                Project.createFromObject(obj=obj, generateNewId=True)
                if obj.id() == ""
                else obj
            )
        else:
            obj = Project.createFromObject(obj=obj, publishEvent=True)
            self._repo.save(obj=obj)
            return obj

    @debugLogger
    def deleteProject(self, obj: Project, tokenData: TokenData = None):
        obj.publishDelete()
        self._repo.deleteProject(obj=obj)

    @debugLogger
    def updateProject(
        self, oldObject: Project, newObject: Project, tokenData: TokenData = None
    ):
        newObject.publishUpdate(oldObject)
        self._repo.save(obj=newObject)

    @debugLogger
    def bulkCreate(self, objList: List[Project]):
        return
        # self._repo.bulkSave(objList=objList)
        # for obj in objList:
        #     Project.createFromObject(obj=obj, publishEvent=True)

    @debugLogger
    def bulkDelete(self, objList: List[Project]):
        return
        # self._repo.bulkDelete(objList=objList)
        # for obj in objList:
        #     obj.publishDelete()

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
    def projects(
        self,
        tokenData: TokenData = None,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
    ):
        pass

    @debugLogger
    def projectsByState(
        self,
        state: str = None,
        tokenData: TokenData = None,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
    ):
        pass

    @debugLogger
    def projectsByOrganizationId(
        self,
        organizationId: str,
        tokenData: TokenData = None,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
    ):
        pass

