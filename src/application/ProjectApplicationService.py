"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

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
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._projectService.createProject(id=id, name=name, cityId=cityId, countryId=countryId,
                                                  addressLine=addressLine, beneficiaryId=beneficiaryId,
                                                  objectOnly=objectOnly, tokenData=tokenData)
