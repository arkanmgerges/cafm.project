"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from abc import ABC, abstractmethod
from typing import List

from src.domain_model.project.equipment.Equipment import Equipment
from src.domain_model.token.TokenData import TokenData


class EquipmentRepository(ABC):
    @abstractmethod
    def bulkSave(self, objList: List[Equipment], tokenData: TokenData = None):
        """Bulk save equipment list

        Args:
            objList (List[Equipment]): The equipment list that needs to be saved
            tokenData (TokenData): Token data that has info about the token

        """

    @abstractmethod
    def bulkDelete(self, objList: List[Equipment], tokenData: TokenData = None):
        """Bulk delete equipment list

        Args:
            objList (List[Equipment]): The equipment list that needs to be deleted
            tokenData (TokenData): Token data that has info about the token

        """

    @abstractmethod
    def save(self, obj: Equipment, tokenData: TokenData = None):
        """Save equipment

        Args:
            obj (Equipment): The equipment that needs to be saved
            tokenData (TokenData): Token data that has info about the token

        """

    @abstractmethod
    def linkEquipmentToEquipment(self, srcObj: Equipment, dstObj: Equipment, tokenData: TokenData = None):
        """Link equipment to another equipment

        Args:
            srcObj (Equipment): The source equipment
            dstObj (Equipment): The destination equipment
            tokenData (TokenData): Token data that has info about the token

        """

    @abstractmethod
    def unlinkEquipmentToEquipment(self, srcObj: Equipment, dstObj: Equipment, tokenData: TokenData = None):
        """Unlink equipment from another equipment

        Args:
            srcObj (Equipment): The source equipment
            dstObj (Equipment): The destination equipment
            tokenData (TokenData): Token data that has info about the token

        """

    @abstractmethod
    def deleteEquipment(self, obj: Equipment, tokenData: TokenData, ignoreRelations: bool) -> None:
        """Delete a equipment

        Args:
            obj (Equipment): The equipment that needs to be deleted
            tokenData (TokenData): Token data used for deleting the equipment
            ignoreRelations (bool): If 'False' then ignore any relation and delete the equipment, otherwise throws an error

        :raises:
            `ObjectCouldNotNotBeDeletedException
            <src.domain_model.resource.exception.ObjectCouldNotNotBeDeletedException>`
            Raise an exception if the equipment could not be deleted
        """

    @abstractmethod
    def equipmentById(self, id: str) -> Equipment:
        """Get equipment by id

        Args:
            id (str): The id of the equipment

        Returns:
            Equipment: equipment object

        :raises:
            `EquipmentDoesNotExistException <src.domain_model.resource.exception.EquipmentDoesNotExistException>`
            Raise an exception if the equipment does not exist
        """

    @abstractmethod
    def equipmentsByProjectId(
        self,
        tokenData: TokenData,
        projectId: str = None,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
    ) -> dict:
        """Fetch equipments by project id

        Args:
            tokenData (TokenData): A token data object
            projectId (str): Project id
            resultFrom (int): The start offset of the result item
            resultSize (int): The size of the items in the result
            order (List[dict]): A list of order e.g. [{'orderBy': 'name', 'direction': 'asc'},
                                {'orderBy': 'quantity', 'direction': 'desc'}]

        Returns:
            dict: A dict that has {"items": [], "totalItemCount": 0}
        """

    @abstractmethod
    def equipments(
        self,
        tokenData: TokenData,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
    ) -> dict:
        """Get list of equipments based on the owned roles that the user has

        Args:
            tokenData (TokenData): A token data object
            resultFrom (int): The start offset of the result item
            resultSize (int): The size of the items in the result
            order (List[dict]): A list of order e.g. [{'orderBy': 'name', 'direction': 'asc'},
                                {'orderBy': 'quantity', 'direction': 'desc'}]

        Returns:
            dict: A dict that has {"items": [], "totalItemCount": 0}
        """
