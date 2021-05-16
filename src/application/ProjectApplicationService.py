"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from src.application.BaseApplicationService import BaseApplicationService
from src.domain_model.project.Project import Project
from src.domain_model.project.ProjectRepository import ProjectRepository
from src.domain_model.project.ProjectService import ProjectService
from src.domain_model.resource.exception.UpdateProjectFailedException import (
    UpdateProjectFailedException,
)
from src.domain_model.token.TokenService import TokenService
from src.resource.logging.decorator import debugLogger


class ProjectApplicationService(BaseApplicationService):
    def __init__(self, repo: ProjectRepository, projectService: ProjectService):
        self._repo = repo
        self._projectService = projectService

    @debugLogger
    def newId(self):
        return Project.createFrom(skipValidation=True).id()

    @debugLogger
    def createProject(self, token: str = None, objectOnly: bool = False, **kwargs):
        obj: Project = self._constructObject(**kwargs)
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._projectService.createProject(obj=obj, objectOnly=objectOnly, tokenData=tokenData)

    @debugLogger
    def updateProject(self, token: str = None, **kwargs):
        tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            oldObject: Project = self._repo.projectById(id=kwargs["id"])
            obj: Project = self._constructObject(_sourceObject=oldObject, **kwargs)
            self._projectService.updateProject(oldObject=oldObject, newObject=obj, tokenData=tokenData)
        except Exception as e:
            raise UpdateProjectFailedException(message=str(e))

    @debugLogger
    def deleteProject(self, id: str, token: str = "", **_kwargs):
        tokenData = TokenService.tokenDataFromToken(token=token)
        obj = self._repo.projectById(id=id)
        self._projectService.deleteProject(obj=obj, tokenData=tokenData)

    @debugLogger
    def changeState(self, projectId: str, state: str, token: str = "", **_kwargs):
        tokenData = TokenService.tokenDataFromToken(token=token)
        project = self._repo.projectById(id=projectId)
        project.changeState(Project.stateStringToProjectState(state))
        self._repo.changeState(project=project, tokenData=tokenData)

    @debugLogger
    def projectById(self, id: str, token: str = "") -> Project:
        project = self._repo.projectById(id=id)
        _tokenData = TokenService.tokenDataFromToken(token=token)
        return project

    @debugLogger
    def projects(
        self,
        resultFrom: int = 0,
        resultSize: int = 100,
        token: str = "",
        order: List[dict] = None,
    ) -> dict:
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._projectService.projects(
            tokenData=tokenData,
            resultFrom=resultFrom,
            resultSize=resultSize,
            order=order,
        )

    @debugLogger
    def _constructObject(self, *args, **kwargs) -> Project:
        kwargs[BaseApplicationService.DOMAIN_MODEL_CLASS] = Project
        return super()._constructObject(*args, **kwargs)
