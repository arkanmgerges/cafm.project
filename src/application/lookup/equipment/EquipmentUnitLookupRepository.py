"""
The file is generated by scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""


from abc import ABC, abstractmethod
from src.domain_model.project.unit.Unit import Unit


class EquipmentUnitLookupRepository(ABC):
    @abstractmethod
    def save(self, obj: Unit):
        """Save unit

        Args:
            obj (Unit): The unit that needs to be saved

        """
