"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from abc import ABC, abstractmethod
from typing import List
from src.domain_model.project.daily_check.procedure.operation.DailyCheckProcedureOperation import (
    DailyCheckProcedureOperation,
)
from src.domain_model.token.TokenData import TokenData


class DailyCheckProcedureOperationRepository(ABC):
    @abstractmethod
    def bulkSave(self, objList: List[DailyCheckProcedureOperation], tokenData: TokenData = None):
        """Bulk save daily check procedure operation list

        Args:
            objList (List[DailyCheckProcedureOperation]): The daily check procedure operation list that needs to be saved
            tokenData (TokenData): Token data that has info about the token

        """

    @abstractmethod
    def bulkDelete(self, objList: List[DailyCheckProcedureOperation], tokenData: TokenData = None):
        """Bulk delete daily check procedure operation list

        Args:
            objList (List[DailyCheckProcedureOperation]): The daily check procedure operation list that needs to be deleted
            tokenData (TokenData): Token data that has info about the token

        """

    @abstractmethod
    def save(self, obj: DailyCheckProcedureOperation, tokenData: TokenData = None):
        """Save daily check procedure operation

        Args:
            obj (DailyCheckProcedureOperation): The daily check procedure operation that needs to be saved
            tokenData (TokenData): Token data that has info about the token

        """

    @abstractmethod
    def deleteDailyCheckProcedureOperation(
        self, obj: DailyCheckProcedureOperation, tokenData: TokenData
    ) -> None:
        """Delete a daily check procedure operation

        Args:
            obj (DailyCheckProcedureOperation): The daily check procedure operation that needs to be deleted
            tokenData (TokenData): Token data used for deleting the daily check procedure operation

        :raises:
            `ObjectCouldNotNotBeDeletedException
            <src.domain_model.resource.exception.ObjectCouldNotNotBeDeletedException>`
            Raise an exception if the daily check procedure operation could not be deleted
        """

    @abstractmethod
    def dailyCheckProcedureOperationById(self, id: str) -> DailyCheckProcedureOperation:
        """Get daily check procedure operation by id

        Args:
            id (str): The id of the daily check procedure operation

        Returns:
            DailyCheckProcedureOperation: daily check procedure operation object

        :raises:
            `DailyCheckProcedureOperationDoesNotExistException <src.domain_model.resource.exception.DailyCheckProcedureOperationDoesNotExistException>`
            Raise an exception if the daily check procedure operation does not exist
        """

    @abstractmethod
    def dailyCheckProcedureOperations(
        self,
        tokenData: TokenData,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
    ) -> dict:
        """Get list of daily check procedure operations based on the owned roles that the user has

        Args:
            tokenData (TokenData): A token data object
            resultFrom (int): The start offset of the result item
            resultSize (int): The size of the items in the result
            order (List[dict]): A list of order e.g. [{'orderBy': 'name', 'direction': 'asc'},
                                {'orderBy': 'quantity', 'direction': 'desc'}]

        Returns:
            dict: A dict that has {"items": [], "totalItemCount": 0}
        """

    @abstractmethod
    def dailyCheckProcedureOperationsByDailyCheckProcedureId(
        self,
        tokenData: TokenData,
        dailyCheckProcedureId: str = None,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
    ) -> dict:
        """Get list of daily check procedure operations by daily_check_procedure_operation id based on the owned roles that the user has

        Args:
            tokenData (TokenData): A token data object
            DailyCheckProcedureId: A daily_check_procedure_operation id
            resultFrom (int): The start offset of the result item
            resultSize (int): The size of the items in the result
            order (List[dict]): A list of order e.g. [{'orderBy': 'name', 'direction': 'asc'},
                                {'orderBy': 'quantity', 'direction': 'desc'}]

        Returns:
            dict: A dict that has {"items": [], "totalItemCount": 0}
        """
