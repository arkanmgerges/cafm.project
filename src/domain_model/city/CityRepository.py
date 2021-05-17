"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from abc import ABC, abstractmethod

from src.domain_model.city.City import City


class CityRepository(ABC):
    @abstractmethod
    def cityById(self, id: int) -> City:
        """Get city by id

        Args:
            id (int): The id of the city

        Returns:
            City: city object

        :raises:
            `CityDoesNotExistException <src.domain_model.resource.exception.CityDoesNotExistException>`
            Raise an exception if the city does not exist
        """
