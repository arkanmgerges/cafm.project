"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from abc import ABC, abstractmethod
from typing import List

from src.domain_model.user.User import User
from src.domain_model.token.TokenData import TokenData


class UserRepository(ABC):
    @abstractmethod
    def createUser(self, user: User, tokenData: TokenData):
        """Create user

        Args:
            user (User): The user that needs to be created
            tokenData (TokenData): Token data that has info about the token

        """

    @abstractmethod
    def deleteUser(self, user: User, tokenData: TokenData) -> None:
        """Delete a user

        Args:
            user (User): The user that needs to be deleted
            tokenData (TokenData): Token data used for deleting the user

        :raises:
            `ObjectCouldNotNotBeDeletedException
            <src.domain_model.resource.exception.ObjectCouldNotNotBeDeletedException>`
            Raise an exception if the user could not be deleted
        """

    @abstractmethod
    def updateUser(self, user: User, tokenData: TokenData) -> None:
        """Update a user

        Args:
            user (User): The user that needs to be updated
            tokenData (TokenData): Token data used for updating the user

        :raises:
            `ObjectCouldNotNotBeUpdatedException
            <src.domain_model.resource.exception.ObjectCouldNotNotBeUpdatedException>`
            Raise an exception if the user could not be updated
        """

    @abstractmethod
    def userByEmail(self, email: str) -> User:
        """Get user by email

        Args:
            email (str): The email of the user

        Returns:
            User: user object
            
        :raises:
            `UserDoesNotExistException <src.domain_model.resource.exception.UserDoesNotExistException>`
            Raise an exception if the user does not exist
        """

    @abstractmethod
    def userById(self, id: str) -> User:
        """Get user by id

        Args:
            id (str): The id of the user

        Returns:
            User: user object

        :raises:
            `UserDoesNotExistException <src.domain_model.resource.exception.UserDoesNotExistException>`
            Raise an exception if the user does not exist
        """

    @abstractmethod
    def users(self, tokenData: TokenData, resultFrom: int = 0, resultSize: int = 100,
                 order: List[dict] = None) -> dict:
        """Get list of users based on the owned roles that the user has

        Args:
            tokenData (TokenData): A token data object
            resultFrom (int): The start offset of the result item
            resultSize (int): The size of the items in the result
            order (List[dict]): A list of order e.g. [{'orderBy': 'name', 'direction': 'asc'},
                                {'orderBy': 'age', 'direction': 'desc'}]

        Returns:
            dict: A dict that has {"items": [], "itemCount": 0}
        """

