"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import pytest

from src.domain_model.event.DomainPublishedEvents import DomainPublishedEvents
from src.domain_model.project.equipment.Equipment import Equipment
from src.domain_model.resource.exception.InvalidArgumentException import InvalidArgumentException


def setup_function(function):
    DomainPublishedEvents.cleanup()


def test_create_equipment():
    # Act
    equipment = _create_object()
    # Assert
    assert isinstance(equipment, Equipment)


def test_equipment_name():
    # Act
    equipment = _create_object()
    # Assert
    assert equipment.name() == 'equipment-1'


def test_create_from_object():
    # Act
    equipment = _create_object()
    equipment2 = Equipment.createFromObject(obj=equipment)
    # Assert
    assert equipment == equipment2


def test_equipment_category_and_group_ids():
    # Act
    equipment = _create_object()
    # Assert
    assert equipment.equipmentCategoryId() == '1234'
    assert equipment.equipmentCategoryGroupId() == '5678'


def test_invalid_category_id():
    # Act, Assert
    with pytest.raises(InvalidArgumentException):
        equipment = Equipment.createFrom(equipmentCategoryId=None)
    with pytest.raises(InvalidArgumentException):
        equipment = Equipment.createFrom(equipmentCategoryId='')

def test_manufacturer_id():
    # Act
    equipment = _create_object()
    # Assert
    assert equipment.manufacturerId() == '1234'

def test_model_id():
    # Act
    equipment = _create_object()
    # Assert
    assert equipment.equipmentModelId() == '1234'

def test_project_id():
    # Act
    equipment = _create_object()
    # Assert
    assert equipment.projectId() == '1234'

def test_invalid_group_id():
    # Act, Assert
    with pytest.raises(InvalidArgumentException):
        equipment = Equipment.createFrom(equipmentCategoryGroupId=None)
    with pytest.raises(InvalidArgumentException):
        equipment = Equipment.createFrom(equipmentCategoryGroupId='')

def test_invalid_building_id():
    # Act, Assert
    with pytest.raises(InvalidArgumentException):
        equipment = Equipment.createFrom(buildingId=None)
    with pytest.raises(InvalidArgumentException):
        equipment = Equipment.createFrom(buildingId='')

def test_invalid_level_id():
    # Act, Assert
    with pytest.raises(InvalidArgumentException):
        equipment = Equipment.createFrom(buildingLevelId=None)
    with pytest.raises(InvalidArgumentException):
        equipment = Equipment.createFrom(buildingLevelId='')

def test_invalid_room_id():
    # Act, Assert
    with pytest.raises(InvalidArgumentException):
        equipment = Equipment.createFrom(buildingLevelRoomId=None)
    with pytest.raises(InvalidArgumentException):
        equipment = Equipment.createFrom(buildingLevelRoomId='')


def test_equipment_building_level_room_ids():
    # Act
    equipment = _create_object(id='1', name='equipment-1', categoryId='1234', groupId='5678',
                                     buildingId='1', levelId='2', roomId='3')
    # Assert
    assert equipment.equipmentCategoryId() == '1234'
    assert equipment.equipmentCategoryGroupId() == '5678'
    assert equipment.buildingId() == '1'
    assert equipment.buildingLevelId() == '2'
    assert equipment.buildingLevelRoomId() == '3'

def test_equipment_with_skip_validation():
    # Act
    equipment = _create_object(id='1', name='equipment-1', categoryId='1234', groupId='5678',
                                     buildingId='', levelId='', roomId='', skipValidation=True)
    equipment2 = Equipment.createFromObject(obj=equipment, skipValidation=True)
    # Assert
    assert equipment.equipmentCategoryId() == '1234'
    assert equipment.equipmentCategoryGroupId() == '5678'
    assert equipment.buildingId() is ''
    assert equipment.buildingLevelId() is ''
    assert equipment.buildingLevelRoomId() is ''

    assert equipment2.buildingId() is ''
    assert equipment2.buildingLevelId() is ''
    assert equipment2.buildingLevelRoomId() is ''

def test_toMap():
    # Arrange
    equipment = _create_object(id='1', name='equipment-1', categoryId='1234', groupId='5678',
                                     buildingId='1', levelId='2', roomId='3', manufacturerId='12', modelId='34',
                               equipmentProjectCategoryId='1234')
    currentMap = {'id': '1', 'name': 'equipment-1', 'project_id': '1234', 'equipment_category_id': '1234',
                  'equipment_category_group_id': '5678', 'building_id': '1',
                  'building_level_id': '2', 'building_level_room_id': '3', 'manufacturer_id': '12', 'equipment_model_id': '34',
                  'equipment_project_category_id': '1234'}
    # Act
    objectMap = equipment.toMap()

    # Assert
    assert objectMap == currentMap
    assert len(objectMap.keys()) == len(currentMap.keys())

def _create_object(id: str = None, name: str = None, projectId: str = None, categoryId: str = None, groupId: str = None,
                   buildingId: str = None, levelId: str = None, roomId: str = None, manufacturerId: str = None,
                   modelId: str = None, quantity: int = 0, equipmentProjectCategoryId: str = None,
                   skipValidation: bool = False):
    id = '1' if id is None else id
    name = 'equipment-1' if name is None else name
    projectId = '1234' if projectId is None else projectId
    categoryId = '1234' if categoryId is None else categoryId
    groupId = '5678' if groupId is None else groupId
    buildingId = '1' if buildingId is None else buildingId
    levelId = '2' if levelId is None else levelId
    roomId = '3' if roomId is None else roomId
    manufacturerId = '1234' if manufacturerId is None else manufacturerId
    modelId = '1234' if modelId is None else modelId
    quantity = 10 if quantity is None else quantity
    equipmentProjectCategoryId = '1234' if equipmentProjectCategoryId is None else equipmentProjectCategoryId

    return Equipment.createFrom(id=id, name=name, projectId=projectId, equipmentCategoryId=categoryId, equipmentCategoryGroupId=groupId,
                                buildingId=buildingId, buildingLevelId=levelId, buildingLevelRoomId=roomId, manufacturerId=manufacturerId,
                                equipmentModelId=modelId, quantity=quantity, equipmentProjectCategoryId=equipmentProjectCategoryId,
                                skipValidation=skipValidation)
