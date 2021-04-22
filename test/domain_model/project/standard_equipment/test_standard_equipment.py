"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

import pytest

from src.domain_model.event.DomainPublishedEvents import DomainPublishedEvents
from src.domain_model.project.standard_equipment.StandardEquipment import (
    StandardEquipment,
)


def setup_function(function):
    DomainPublishedEvents.cleanup()


def test_create_object():
    # Act
    obj = _create_object()
    # Assert
    assert isinstance(obj, StandardEquipment)


def test_name():
    # Act
    obj = _create_object()
    # Assert
    assert obj.name() == "name"


def test_standard_equipment_category_id():
    # Act
    obj = _create_object()
    # Assert
    assert obj.standardEquipmentCategoryId() == "standard_equipment_category_id"


def test_standard_equipment_category_group_id():
    # Act
    obj = _create_object()
    # Assert
    assert (
        obj.standardEquipmentCategoryGroupId() == "standard_equipment_category_group_id"
    )


def test_manufacturer_id():
    # Act
    obj = _create_object()
    # Assert
    assert obj.manufacturerId() == "manufacturer_id"


def test_equipment_model_id():
    # Act
    obj = _create_object()
    # Assert
    assert obj.equipmentModelId() == "equipment_model_id"


def test_create_from_object():
    # Act
    obj = _create_object()
    obj2 = StandardEquipment.createFromObject(obj=obj)
    # Assert
    assert obj == obj2


def test_toMap():
    # Arrange
    obj = _create_object(
        id="1",
        name="name",
        standardEquipmentCategoryId="standard_equipment_category_id",
        standardEquipmentCategoryGroupId="standard_equipment_category_group_id",
        manufacturerId="manufacturer_id",
        equipmentModelId="equipment_model_id",
    )
    currentMap = {
        "standard_equipment_id": "1",
        "name": "name",
        "standard_equipment_category_id": "standard_equipment_category_id",
        "standard_equipment_category_group_id": "standard_equipment_category_group_id",
        "manufacturer_id": "manufacturer_id",
        "equipment_model_id": "equipment_model_id",
    }
    # Act
    objectMap = obj.toMap()

    # Assert
    assert objectMap == currentMap
    assert len(objectMap.keys()) == len(currentMap.keys())


def _create_object(
    id: str = None,
    name: str = None,
    standardEquipmentCategoryId: str = None,
    standardEquipmentCategoryGroupId: str = None,
    manufacturerId: str = None,
    equipmentModelId: str = None,
    skipValidation: bool = False,
):
    id = "1" if id is None else id
    name = "name" if name is None else name
    standardEquipmentCategoryId = (
        "standard_equipment_category_id"
        if standardEquipmentCategoryId is None
        else standardEquipmentCategoryId
    )
    standardEquipmentCategoryGroupId = (
        "standard_equipment_category_group_id"
        if standardEquipmentCategoryGroupId is None
        else standardEquipmentCategoryGroupId
    )
    manufacturerId = "manufacturer_id" if manufacturerId is None else manufacturerId
    equipmentModelId = (
        "equipment_model_id" if equipmentModelId is None else equipmentModelId
    )

    return StandardEquipment.createFrom(
        id=id,
        name=name,
        standardEquipmentCategoryId=standardEquipmentCategoryId,
        standardEquipmentCategoryGroupId=standardEquipmentCategoryGroupId,
        manufacturerId=manufacturerId,
        equipmentModelId=equipmentModelId,
        skipValidation=skipValidation,
    )
