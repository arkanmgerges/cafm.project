"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from abc import ABC, abstractmethod
from typing import List
from src.domain_model.project.maintenance.procedure.operation.parameter.MaintenanceProcedureOperationParameter import MaintenanceProcedureOperationParameter
from src.domain_model.token.TokenData import TokenData


class MaintenanceProcedureOperationParameterRepository(ABC):
    @abstractmethod
    def save(self, obj: MaintenanceProcedureOperationParameter, tokenData: TokenData):
        """Save maintenance procedure operation parameter

        Args:
            obj (MaintenanceProcedureOperationParameter): The maintenance procedure operation parameter that needs to be saved
            tokenData (TokenData): Token data that has info about the token

        """

    @abstractmethod
    def createMaintenanceProcedureOperationParameter(self, obj: MaintenanceProcedureOperationParameter, tokenData: TokenData):
        """Create maintenance procedure operation parameter

        Args:
            obj (MaintenanceProcedureOperationParameter): The maintenance procedure operation parameter that needs to be created
            tokenData (TokenData): Token data that has info about the token

        """

    @abstractmethod
    def deleteMaintenanceProcedureOperationParameter(self, obj: MaintenanceProcedureOperationParameter, tokenData: TokenData) -> None:
        """Delete a maintenance procedure operation parameter

        Args:
            obj (MaintenanceProcedureOperationParameter): The maintenance procedure operation parameter that needs to be deleted
            tokenData (TokenData): Token data used for deleting the maintenance procedure operation parameter

        :raises:
            `ObjectCouldNotNotBeDeletedException
            <src.domain_model.resource.exception.ObjectCouldNotNotBeDeletedException>`
            Raise an exception if the maintenance procedure operation parameter could not be deleted
        """

    @abstractmethod
    def updateMaintenanceProcedureOperationParameter(self, obj: MaintenanceProcedureOperationParameter, tokenData: TokenData) -> None:
        """Update a maintenance procedure operation parameter

        Args:
            obj (MaintenanceProcedureOperationParameter): The maintenance procedure operation parameter that needs to be updated
            tokenData (TokenData): Token data used for updating the maintenance procedure operation parameter

        :raises:
            `ObjectCouldNotNotBeUpdatedException
            <src.domain_model.resource.exception.ObjectCouldNotNotBeUpdatedException>`
            Raise an exception if the maintenance procedure operation parameter could not be updated
        """


    @abstractmethod
    def maintenanceProcedureOperationParameterById(self, id: str) -> MaintenanceProcedureOperationParameter:
        """Get maintenance procedure operation parameter by id

        Args:
            id (str): The id of the maintenance procedure operation parameter

        Returns:
            MaintenanceProcedureOperationParameter: maintenance procedure operation parameter object

        :raises:
            `MaintenanceProcedureOperationParameterDoesNotExistException <src.domain_model.resource.exception.MaintenanceProcedureOperationParameterDoesNotExistException>`
            Raise an exception if the maintenance procedure operation parameter does not exist
        """

    @abstractmethod
    def maintenanceProcedureOperationParameters(self, tokenData: TokenData, resultFrom: int = 0, resultSize: int = 100,
                 order: List[dict] = None) -> dict:
        """Get list of maintenance procedure operation parameters based on the owned roles that the user has

        Args:
            tokenData (TokenData): A token data object
            resultFrom (int): The start offset of the result item
            resultSize (int): The size of the items in the result
            order (List[dict]): A list of order e.g. [{'orderBy': 'name', 'direction': 'asc'},
                                {'orderBy': 'quantity', 'direction': 'desc'}]

        Returns:
            dict: A dict that has {"items": [], "itemCount": 0}
        """
      
    @abstractmethod
    def maintenanceProcedureOperationParametersByMaintenanceProcedureOperationId(self, tokenData: TokenData, 
                 maintenanceProcedureOperationId: str = None, 
                 resultFrom: int = 0, 
                 resultSize: int = 100,
                 order: List[dict] = None) -> dict:
        """Get list of maintenance procedure operation parameters by maintenance_procedure_operation_parameter id based on the owned roles that the user has

        Args:
            tokenData (TokenData): A token data object
            MaintenanceProcedureOperationId: A maintenance_procedure_operation_parameter id
            resultFrom (int): The start offset of the result item
            resultSize (int): The size of the items in the result
            order (List[dict]): A list of order e.g. [{'orderBy': 'name', 'direction': 'asc'},
                                {'orderBy': 'quantity', 'direction': 'desc'}]

        Returns:
            dict: A dict that has {"items": [], "itemCount": 0}
        """
