"""
The file is generated by scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""


from abc import ABC, abstractmethod
from src.domain_model.project.equipment.project_category.EquipmentProjectCategory import EquipmentProjectCategory


class EquipmentProjectCategoryLookupRepository(ABC):
    @abstractmethod
    def save(self, obj: EquipmentProjectCategory):
        """Save equipment project category

        Args:
            obj (EquipmentProjectCategory): The equipment project category that needs to be saved

        """
