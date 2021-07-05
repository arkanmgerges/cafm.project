"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from abc import ABC, abstractmethod
from typing import List

from src.domain_model.project.Project import Project
from src.domain_model.token.TokenData import TokenData


class ProjectRepository(ABC):
    @abstractmethod
    def bulkSave(self, objList: List[Project], tokenData: TokenData = None):
        """Bulk save project list

        Args:
            objList (List[Project]): The project list that needs to be saved
            tokenData (TokenData): Token data that has info about the token

        """

    @abstractmethod
    def bulkDelete(self, objList: List[Project], tokenData: TokenData = None):
        """Bulk delete project list

        Args:
            objList (List[Project]): The project list that needs to be deleted
            tokenData (TokenData): Token data that has info about the token

        """

    @abstractmethod
    def save(self, obj: Project, tokenData: TokenData = None):
        """Save project

        Args:
            obj (Project): The project that needs to be saved
            tokenData (TokenData): Token data that has info about the token

        """

    @abstractmethod
    def deleteProject(self, obj: Project, tokenData: TokenData) -> None:
        """Delete a project

        Args:
            obj (Project): The project that needs to be deleted
            tokenData (TokenData): Token data used for deleting the project

        :raises:
            `ObjectCouldNotNotBeDeletedException
            <src.domain_model.resource.exception.ObjectCouldNotNotBeDeletedException>`
            Raise an exception if the project could not be deleted
        """

    @abstractmethod
    def projectById(self, id: str) -> Project:
        """Get project by id

        Args:
            id (str): The id of the project

        Returns:
            Project: project object

        :raises:
            `ProjectDoesNotExistException <src.domain_model.resource.exception.ProjectDoesNotExistException>`
            Raise an exception if the project does not exist
        """

    @abstractmethod
    def projects(
        self,
        tokenData: TokenData,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
    ) -> dict:
        """Get list of projects based on the owned roles that the user has

        Args:
            tokenData (TokenData): A token data object
            resultFrom (int): The start offset of the result item
            resultSize (int): The size of the items in the result
            order (List[dict]): A list of order e.g. [{'orderBy': 'name', 'direction': 'asc'},
                                {'orderBy': 'age', 'direction': 'desc'}]

        Returns:
            dict: A dict that has {"items": [], "totalItemCount": 0}
        """

    @abstractmethod
    def projectsByState(
        self,
        tokenData: TokenData,
        state: str = None,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
    ) -> dict:
        """Get list of projects based on the owned roles that the user has, filtered by state

        Args:
            tokenData (TokenData): A token data object
            state(str): Project state
            resultFrom (int): The start offset of the result item
            resultSize (int): The size of the items in the result
            order (List[dict]): A list of order e.g. [{'orderBy': 'name', 'direction': 'asc'},
                                {'orderBy': 'age', 'direction': 'desc'}]

        Returns:
            dict: A dict that has {"items": [], "totalItemCount": 0}
        """

    @abstractmethod
    def projectsByOrganizationId(
        self,
        organizationId: str,
        tokenData: TokenData,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
    ) -> dict:
        """Get list of projects based on the owned roles that the user has

        Args:
            organizationId (str): The Organization id used to fetch project data
            tokenData (TokenData): A token data object
            resultFrom (int): The start offset of the result item
            resultSize (int): The size of the items in the result
            order (List[dict]): A list of order e.g. [{'orderBy': 'name', 'direction': 'asc'},
                                {'orderBy': 'age', 'direction': 'desc'}]

        Returns:
            dict: A dict that has {"items": [], "totalItemCount": 0}
        """

    @abstractmethod
    def changeState(self, project: Project, tokenData: TokenData) -> None:
        """Change project state

        Args:
            project (Project): The project that needs for its state to be changed
            tokenData (TokenData): Token data used for updating the project state
        """

    @abstractmethod
    def projectsFilteredByProjectList(self, tokenData: TokenData, resultFrom: int = 0, resultSize: int = 10,
                                      order: List[dict] = None, projectList: List[Project] = None) -> dict:
        """Retrieve projects by list of projects passed as an argument

        Args:
            tokenData (TokenData): A token data object
            resultFrom (int): The start offset of the result item
            resultSize (int): The size of the items in the result
            order (List[dict]): A list of order e.g. [{'orderBy': 'name', 'direction': 'asc'},
                                {'orderBy': 'age', 'direction': 'desc'}]
            projectList (List[Project]): List of project objects to be used for filtering

        Returns:
            dict: A dict that has {"items": [], "totalItemCount": 0}
        """

    @abstractmethod
    def projectsByStateFilteredByProjectList(self, tokenData: TokenData, state: str,
                                             resultFrom: int = 0, resultSize: int = 10,
                                      order: List[dict] = None, projectList: List[Project] = None) -> dict:
        """Retrieve projects by state and filter by list of projects passed as an argument

        Args:
            tokenData (TokenData): A token data object
            state (str): Project state used for filtering
            resultFrom (int): The start offset of the result item
            resultSize (int): The size of the items in the result
            order (List[dict]): A list of order e.g. [{'orderBy': 'name', 'direction': 'asc'},
                                {'orderBy': 'age', 'direction': 'desc'}]
            projectList (List[Project]): List of project objects to be used for filtering

        Returns:
            dict: A dict that has {"items": [], "totalItemCount": 0}
        """