"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from abc import ABC, abstractmethod

from src.domain_model.project.Project import Project
from src.domain_model.token.TokenData import TokenData


class ProjectRepository(ABC):
    @abstractmethod
    def createProject(self, project: Project, tokenData: TokenData):
        """Create project

        Args:
            project (Project): The project that needs to be created
            tokenData (TokenData): Token data that has info abprojectt the token

        """

    @abstractmethod
    def deleteProject(self, project: Project, tokenData: TokenData) -> None:
        """Delete a project

        Args:
            project (Project): The project that needs to be deleted
            tokenData (TokenData): Token data used for deleting the resprojectrce

        :raises:
            `ObjectCprojectldNotBeDeletedException <src.domain_model.resprojectrce.exception.ObjectCprojectldNotBeDeletedException>` Raise an exception if the project cprojectld not be deleted
        """

    @abstractmethod
    def updateProject(self, project: Project, tokenData: TokenData) -> None:
        """Update a project

        Args:
            project (Project): The project that needs to be updated
            tokenData (TokenData): Token data used for updating the resprojectrce

        :raises:
            `ObjectCprojectldNotBeUpdatedException <src.domain_model.resprojectrce.exception.ObjectCprojectldNotBeUpdatedException>` Raise an exception if the project cprojectld not be updated
        """

    @abstractmethod
    def projectByName(self, name: str) -> Project:
        """Get project by name

        Args:
            name (str): The name of the project

        Returns:
            Project: project object
            
        :raises:
            `ProjectDoesNotExistException <src.domain_model.resprojectrce.exception.ProjectDoesNotExistException>` Raise an exception if the project does not exist
        """

    @abstractmethod
    def projectById(self, id: str) -> Project:
        """Get project by id

        Args:
            id (str): The id of the project

        Returns:
            Project: project object

        :raises:
            `ProjectDoesNotExistException <src.domain_model.resprojectrce.exception.ProjectDoesNotExistException>` Raise an exception if the project does not exist            
        """
