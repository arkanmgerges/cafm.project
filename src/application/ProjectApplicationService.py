"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from src.application.BaseApplicationService import BaseApplicationService
from src.application.lifecycle.decorator.readOnly import readOnly
from src.application.lifecycle.decorator.transactional import transactional
from src.domain_model.project.Project import Project
from src.domain_model.project.ProjectRepository import ProjectRepository
from src.domain_model.project.ProjectService import ProjectService
from src.domain_model.resource.exception.ProjectDoesNotExistException import ProjectDoesNotExistException
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

    @transactional
    @debugLogger
    def createProject(self, token: str = None, objectOnly: bool = False, **kwargs):
        obj: Project = self._constructObject(**kwargs)
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._projectService.createProject(
            obj=obj,
            objectOnly=objectOnly,
            tokenData=tokenData,
        )

    @transactional
    @debugLogger
    def updateProject(self, token: str = None, **kwargs):
        tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            allProjects = self._projectService.projects(resultSize=999999, tokenData=tokenData)["items"]
            hasProject = any([kwargs["id"] == x.id() for x in allProjects])
            if not hasProject:
                raise Exception(f'project id: {kwargs["id"]} does not exist')

            oldObject: Project = self._repo.projectById(id=kwargs["id"])
            obj: Project = self._constructObject(
                _sourceObject=oldObject, **kwargs)
            self._projectService.updateProject(
                oldObject=oldObject,
                newObject=obj,
                tokenData=tokenData,
            )
        except Exception as e:
            raise UpdateProjectFailedException(message=str(e))

    @transactional
    @debugLogger
    def deleteProject(self, id: str, token: str = "", **_kwargs):
        tokenData = TokenService.tokenDataFromToken(token=token)
        allProjects = self._projectService.projects(resultSize=999999, tokenData=tokenData)["items"]
        hasProject = any([id == x.id() for x in allProjects])
        if not hasProject:
            raise ProjectDoesNotExistException(f'project id: {id} does not exist')
        obj = self._repo.projectById(id=id)
        self._projectService.deleteProject(obj=obj, tokenData=tokenData)

    @transactional
    @debugLogger
    def changeState(self, projectId: str, state: str, token: str = "", **_kwargs):
        tokenData = TokenService.tokenDataFromToken(token=token)
        allProjects = self._projectService.projects(resultSize=999999, tokenData=tokenData)["items"]
        hasProject = any([projectId == x.id() for x in allProjects])
        if not hasProject:
            raise ProjectDoesNotExistException(f'project id: {id} does not exist')
        project = self._repo.projectById(id=projectId)
        project.changeState(Project.stateStringToProjectState(state))
        self._repo.changeState(project=project, tokenData=tokenData)

    @readOnly
    @debugLogger
    def projectById(self, id: str, token: str = "", **_kwargs) -> Project:
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._projectService.projectById(id=id, tokenData=tokenData)

    @readOnly
    @debugLogger
    def projects(
        self,
        resultFrom: int = 0,
        resultSize: int = 100,
        token: str = "",
        order: List[dict] = None,
        **_kwargs,
    ) -> dict:
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._projectService.projects(
            tokenData=tokenData,
            resultFrom=resultFrom,
            resultSize=resultSize,
            order=order,
        )

    @readOnly
    @debugLogger
    def statistics(
        self,
        resultFrom: int = 0,
        resultSize: int = 100,
        token: str = "",
        order: List[dict] = None,
        filter: List[dict] = None,
        **_kwargs,
    ) -> dict:
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._projectService.statistics(
            tokenData=tokenData,
            resultFrom=resultFrom,
            resultSize=resultSize,
            order=order,
            filter=filter,
        )

    @readOnly
    @debugLogger
    def projectsByState(
        self,
        state: str = None,
        resultFrom: int = 0,
        resultSize: int = 100,
        token: str = "",
        order: List[dict] = None,
        **_kwargs,
    ) -> dict:
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._projectService.projectsByState(
            state=state,
            tokenData=tokenData,
            resultFrom=resultFrom,
            resultSize=resultSize,
            order=order,
        )

    @readOnly
    @debugLogger
    def projectsByOrganizationId(
        self,
        organizationId: str,
        resultFrom: int = 0,
        resultSize: int = 100,
        token: str = "",
        order: List[dict] = None,
        **_kwargs,
    ) -> dict:
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._projectService.projectsByOrganizationId(
            organizationId=organizationId,
            tokenData=tokenData,
            resultFrom=resultFrom,
            resultSize=resultSize,
            order=order,
        )

    @debugLogger
    def _constructObject(self, *args, **kwargs) -> Project:
        kwargs[BaseApplicationService.DOMAIN_MODEL_CLASS] = Project
        return super()._constructObject(*args, **kwargs)
