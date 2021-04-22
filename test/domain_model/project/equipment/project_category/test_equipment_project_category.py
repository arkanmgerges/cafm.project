"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

import pytest

from src.domain_model.event.DomainPublishedEvents import DomainPublishedEvents
from src.domain_model.project.equipment.project_category.EquipmentProjectCategory import (
    EquipmentProjectCategory,
)


def setup_function(function):
    DomainPublishedEvents.cleanup()


def test_create_object():
    # Act
    obj = _create_object()
    # Assert
    assert isinstance(obj, EquipmentProjectCategory)


def test_name():
    # Act
    obj = _create_object()
    # Assert
    assert obj.name() == "name"


def test_create_from_object():
    # Act
    obj = _create_object()
    obj2 = EquipmentProjectCategory.createFromObject(obj=obj)
    # Assert
    assert obj == obj2


def test_toMap():
    # Arrange
    obj = _create_object(
        id="1",
        name="name",
    )
    currentMap = {
        "equipment_project_category_id": "1",
        "name": "name",
    }
    # Act
    objectMap = obj.toMap()

    # Assert
    assert objectMap == currentMap
    assert len(objectMap.keys()) == len(currentMap.keys())


def _create_object(id: str = None, name: str = None, skipValidation: bool = False):
    id = "1" if id is None else id
    name = "name" if name is None else name

    return EquipmentProjectCategory.createFrom(
        id=id, name=name, skipValidation=skipValidation
    )
