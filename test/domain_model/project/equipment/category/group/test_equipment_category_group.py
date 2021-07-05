"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

import pytest

from src.domain_model.event.DomainPublishedEvents import DomainPublishedEvents
from src.domain_model.project.equipment.category.group.EquipmentCategoryGroup import (
    EquipmentCategoryGroup,
)


def setup_function(function):
    DomainPublishedEvents.cleanup()


def test_create_object():
    # Act
    obj = _create_object()
    # Assert
    assert isinstance(obj, EquipmentCategoryGroup)


def test_name():
    # Act
    obj = _create_object()
    # Assert
    assert obj.name() == "name"
    assert obj.projectId() == "projectId"
    assert obj.equipmentProjectCategoryId() == "equipmentProjectCategoryId"


def test_create_from_object():
    # Act
    obj = _create_object()
    obj2 = EquipmentCategoryGroup.createFromObject(obj=obj)
    # Assert
    assert obj == obj2


def test_toMap():
    # Arrange
    obj = _create_object(
        id="1",
        name="name",
        projectId="projectId",
        equipmentProjectCategoryId="equipmentProjectCategoryId",

    )
    currentMap = {
        "equipment_category_group_id": "1",
        "name": "name",
        "project_id": "projectId",
        "equipment_project_category_id": "equipmentProjectCategoryId"

    }
    # Act
    objectMap = obj.toMap()

    # Assert
    assert objectMap == currentMap
    assert len(objectMap.keys()) == len(currentMap.keys())


def _create_object(
    id: str = None,
    name: str = None,
    projectId: str = None,
    equipmentProjectCategoryId: str = None,
    skipValidation: bool = False,
):
    id = "1" if id is None else id
    name = "name" if name is None else name
    projectId = "projectId" if projectId is None else projectId
    equipmentProjectCategoryId = "equipmentProjectCategoryId" if equipmentProjectCategoryId is None else equipmentProjectCategoryId


    return EquipmentCategoryGroup.createFrom(
        id=id,
        name=name,
        projectId=projectId,
        equipmentProjectCategoryId=equipmentProjectCategoryId,
        skipValidation=skipValidation,
    )
