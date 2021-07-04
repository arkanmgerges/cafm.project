"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from src.application.lookup.project.ProjectLookupRepository import ProjectLookupRepository
from src.domain_model.project.ProjectRepository import ProjectRepository
from src.domain_model.project.ProjectService import ProjectService
from src.domain_model.resource.exception.ProjectDoesNotExistException import ProjectDoesNotExistException
from src.domain_model.token.TokenData import TokenData
from src.port_adapter.service.identity.IdentityAndAccessAdapter import IdentityAndAccessAdapter
from src.resource.logging.decorator import debugLogger


class ProjectServiceImpl(ProjectService):
    def __init__(self, projectRepo: ProjectRepository, lookupProjectRepo: ProjectLookupRepository,
                 identityAndAccessAdapter: IdentityAndAccessAdapter):
        self._repo = projectRepo
        self._lookupRepo = lookupProjectRepo
        self._identityAndAccessAdapter = identityAndAccessAdapter

    @debugLogger
    def projectById(
            self,
            tokenData: TokenData = None,
            id: str = "",
    ):
        try:
            _ = self._identityAndAccessAdapter.projectById(tokenData=tokenData, id=id)
        except:
            raise ProjectDoesNotExistException(f'project id: {id}')
        return self._repo.projectById(id = id,)

    @debugLogger
    def projects(
            self,
            tokenData: TokenData = None,
            resultFrom: int = 0,
            resultSize: int = 100,
            order: List[dict] = None,
    ):
        projectList = self._identityAndAccessAdapter.projects(tokenData=tokenData)["items"]
        return self._repo.projectsFilteredByProjectList(
            tokenData=tokenData,
            resultFrom=resultFrom,
            resultSize=resultSize,
            order=order,
            projectList=projectList,
        )

    @debugLogger
    def projectsByState(
            self,
            state: str = None,
            tokenData: TokenData = None,
            resultFrom: int = 0,
            resultSize: int = 100,
            order: List[dict] = None,
    ):
        projectList = self._identityAndAccessAdapter.projects(tokenData=tokenData)["items"]
        return self._repo.projectsByStateFilteredByProjectList(
            tokenData=tokenData,
            state=state,
            resultFrom=resultFrom,
            resultSize=resultSize,
            order=order,
            projectList=projectList,
        )

    @debugLogger
    def projectsByOrganizationId(
        self,
        organizationId: str,
        tokenData: TokenData = None,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
    ):
        projectList = self._identityAndAccessAdapter.projectsByOrganizationId(tokenData=tokenData,
                                                                              organizationId=organizationId)["items"]
        return self._repo.projectsFilteredByProjectList(
            tokenData=tokenData,
            resultFrom=resultFrom,
            resultSize=resultSize,
            order=order,
            projectList=projectList,
        )

    def projectsIncludeOrganizationsIncludeUsersIncludeRoles(self,
        tokenData: TokenData = None,
        type: str = None,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
        filter: List[dict] = None,) -> dict:

        response = self._identityAndAccessAdapter.projectsIncludeOrganizationsIncludeUsersIncludeRoles(tokenData=tokenData)["items"]
        return self._lookupRepo.projectsIncludeOrganizationsIncludeUsersIncludeRolesFilteredByProjectsIncludeOrganizationsIncludeUsersIncludeRoles(
            tokenData=tokenData,
            resultFrom=resultFrom,
            resultSize=resultSize,
            order=order,
            projectsIncludeOrganizationsIncludeUsersIncludeRoles=response,
        )