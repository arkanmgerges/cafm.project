"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from src.domain_model.project.Project import Project
from src.domain_model.project.ProjectRepository import ProjectRepository
from src.domain_model.project.ProjectService import ProjectService
from src.domain_model.resource.exception.UpdateProjectFailedException import UpdateProjectFailedException
from src.domain_model.token.TokenService import TokenService
from src.resource.logging.decorator import debugLogger


class ProjectApplicationService:
    def __init__(self, repo: ProjectRepository, projectService: ProjectService):
        self._repo = repo
        self._projectService = projectService

    @debugLogger
    def newId(self):
        return Project.createFrom(skipValidation=True).id()

    @debugLogger
    def createProject(self, id: str = None, name: str = '', cityId: int = 0, countryId: int = 0, addressLine: str = '',
                      beneficiaryId: str = '', objectOnly: bool = False, startDate: int = None, token: str = ''):
        obj: Project = self.constructObject(id=id, name=name, cityId=cityId, countryId=countryId,
                                            addressLine=addressLine,
                                            beneficiaryId=beneficiaryId, startDate=startDate)
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._projectService.createProject(obj=obj,
                                                  objectOnly=objectOnly, tokenData=tokenData)

    @debugLogger
    def updateProject(self, id: str, name: str = None, cityId: int = None, countryId: int = None, addressLine: str = None, beneficiaryId: str = None,
                      startDate: int = None, token: str = ''):

        tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            oldObject: Project = self._repo.projectById(id=id)
            obj: Project = self.constructObject(id=id, name=name, cityId=cityId, countryId=countryId,
                                                addressLine=addressLine,
                                                beneficiaryId=beneficiaryId, startDate=startDate, _sourceObject=oldObject)
            self._projectService.updateProject(oldObject=oldObject,
                                               newObject=obj, tokenData=tokenData)
        except Exception as e:
            raise UpdateProjectFailedException(message=str(e))

    @debugLogger
    def deleteProject(self, id: str, token: str = ''):
        tokenData = TokenService.tokenDataFromToken(token=token)
        obj = self._repo.projectById(id=id)
        self._projectService.deleteProject(obj=obj, tokenData=tokenData)

    @debugLogger
    def changeState(self, projectId: str, newState: str, token: str = ''):
        tokenData = TokenService.tokenDataFromToken(token=token)
        project = self._repo.projectById(id=projectId)
        project.changeState(Project.stateStringToProjectState(newState))
        self._repo.changeState(project=project, tokenData=tokenData)

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
                        beneficiaryId: str, startDate: int, _sourceObject: Project = None) -> Project:
        if _sourceObject is not None:
            return Project.createFrom(id=id,
                                      name=name if name is not None else _sourceObject.name(),
                                      cityId=cityId if cityId is not None else _sourceObject.cityId(),
                                      countryId=countryId if countryId is not None else _sourceObject.countryId(),
                                      addressLine=addressLine if addressLine is not None else _sourceObject.addressLine(),
                                      beneficiaryId=beneficiaryId if beneficiaryId is not None else _sourceObject.beneficiaryId(),
                                      startDate=startDate if startDate is not None else _sourceObject.startDate()
                                      )
        else:
            return Project.createFrom(id=id, name=name, cityId=cityId, countryId=countryId, addressLine=addressLine,
                                  beneficiaryId=beneficiaryId, startDate=startDate)
