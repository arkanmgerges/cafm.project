"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from src.domain_model.project.Project import Project
from src.domain_model.project.ProjectRepository import ProjectRepository
from src.domain_model.project.ProjectService import ProjectService
from src.domain_model.token.TokenService import TokenService
from src.resource.logging.decorator import debugLogger


class ProjectApplicationService:
    def __init__(self, repo: ProjectRepository, projectService: ProjectService):
        self._repo = repo
        self._projectService = projectService

    @debugLogger
    def createProject(self, id: str = '', name: str = '', cityId: int = 0, countryId: int = 0, addressLine: str = '',
                      beneficiaryId: str = '', objectOnly: bool = False, token: str = ''):
        obj: Project = self.constructObject(id=id, name=name, cityId=cityId, countryId=countryId,
                                            addressLine=addressLine,
                                            beneficiaryId=beneficiaryId)
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._projectService.createProject(obj=obj,
                                                  objectOnly=objectOnly, tokenData=tokenData)

    @debugLogger
    def updateProject(self, id: str, name: str, cityId: int, countryId: int, addressLine: str, beneficiaryId: str,
                      token: str = ''):
        obj: Project = self.constructObject(id=id, name=name, cityId=cityId, countryId=countryId,
                                            addressLine=addressLine,
                                            beneficiaryId=beneficiaryId)
        tokenData = TokenService.tokenDataFromToken(token=token)
        oldObject: Project = self._repo.projectById(id=id)
        self._projectService.updateProject(oldObject=oldObject,
                                           newObject=obj, tokenData=tokenData)

    @debugLogger
    def deleteProject(self, id: str, token: str = ''):
        tokenData = TokenService.tokenDataFromToken(token=token)
        obj = self._repo.projectById(id=id)
        self._projectService.deleteProject(obj=obj, tokenData=tokenData)

    @debugLogger
    def changeState(self, id: str, newState: str, token: str = ''):
        tokenData = TokenService.tokenDataFromToken(token=token)
        project = self._repo.projectById(id=id)
        project.changeState(Project.stateStringToProjectState(newState))
        self._repo.changeState(project=project, tokenData=tokenData)

    @debugLogger
    def projectByName(self, name: str, token: str = '') -> Project:
        project = self._repo.projectByName(name=name)
        tokenData = TokenService.tokenDataFromToken(token=token)
        return project

    @debugLogger
    def projectById(self, id: str, token: str = '') -> Project:
        project = self._repo.projectById(id=id)
        tokenData = TokenService.tokenDataFromToken(token=token)
        return project

    @debugLogger
    def projects(self, resultFrom: int = 0, resultSize: int = 100, token: str = '',
                 order: List[dict] = None) -> dict:
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._projectService.projects(tokenData=tokenData,
                                             resultFrom=resultFrom,
                                             resultSize=resultSize,
                                             order=order)

    @debugLogger
    def constructObject(self, id: str, name: str, cityId: int, countryId: int, addressLine: str,
                        beneficiaryId: str) -> Project:
        return Project.createFrom(id=id, name=name, cityId=cityId, countryId=countryId, addressLine=addressLine,
                                  beneficiaryId=beneficiaryId)
