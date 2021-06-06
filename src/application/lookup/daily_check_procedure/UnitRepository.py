"""
The file is generated by scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""


from abc import ABC, abstractmethod
from src.domain_model.project.unit.Unit import Unit


class UnitRepository(ABC):
    @abstractmethod
    def save(self, obj: Unit):
        """Save unit

        Args:
            obj (Unit): The unit that needs to be saved

        """

    @abstractmethod
    def delete(self, obj: Unit):
        """Delete unit

        Args:
            obj (Unit): The unit that needs to be deleted

        """
