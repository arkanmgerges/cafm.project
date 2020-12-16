"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from src.domain_model.project.Project import Project
from src.domain_model.project.ProjectRepository import ProjectRepository
from src.domain_model.resource.exception.ProjectAlreadyExistException import ProjectAlreadyExistException
from src.domain_model.resource.exception.ProjectDoesNotExistException import ProjectDoesNotExistException
from src.domain_model.token.TokenData import TokenData
from src.resource.logging.decorator import debugLogger


class ProjectService:
    def __init__(self, projectRepo: ProjectRepository):
        self._repo = projectRepo

    @debugLogger
    def createProject(self, id: str = '', name: str = '',
                      cityId: int = 0, countryId: int = 0, addressLine: str = '',
                      beneficiaryId: str = '',
                      objectOnly: bool = False, tokenData: TokenData = None):
        try:
            if id == '':
                raise ProjectDoesNotExistException()
            self._repo.projectById(id=id)
            raise ProjectAlreadyExistException(name)
        except ProjectDoesNotExistException:
            if objectOnly:
                if id == '':
                    id = None
                return Project.createFrom(id=id, name=name, cityId=cityId, countryId=countryId, addressLine=addressLine,
                                          beneficiaryId=beneficiaryId)
            else:
                project = Project.createFrom(id=id, name=name, cityId=cityId, countryId=countryId,
                                             addressLine=addressLine,
                                             beneficiaryId=beneficiaryId, publishEvent=True)
                self._repo.createProject(project=project, tokenData=tokenData)
                return project

    @debugLogger
    def deleteProject(self, project: Project, tokenData: TokenData = None):
        self._repo.deleteProject(project, tokenData=tokenData)
        project.publishDelete()

    @debugLogger
    def updateProject(self, oldObject: Project, newObject: Project, tokenData: TokenData = None):
        self._repo.updateProject(newObject, tokenData=tokenData)
        newObject.publishUpdate(oldObject)
