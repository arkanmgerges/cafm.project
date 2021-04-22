"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from src.domain_model.project.Project import Project
from src.domain_model.project.ProjectRepository import ProjectRepository
from src.domain_model.resource.exception.ProjectAlreadyExistException import (
    ProjectAlreadyExistException,
)
from src.domain_model.resource.exception.ProjectDoesNotExistException import (
    ProjectDoesNotExistException,
)
from src.domain_model.token.TokenData import TokenData
from src.resource.logging.decorator import debugLogger


class ProjectService:
    def __init__(self, projectRepo: ProjectRepository):
        self._repo = projectRepo

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
    def projects(
        self,
        tokenData: TokenData = None,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
    ):
        return self._repo.projects(
            tokenData=tokenData,
            resultFrom=resultFrom,
            resultSize=resultSize,
            order=order,
        )
