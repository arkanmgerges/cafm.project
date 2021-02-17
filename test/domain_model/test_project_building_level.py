"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import pytest

from src.domain_model.event.DomainPublishedEvents import DomainPublishedEvents
from src.domain_model.project.building.level.BuildingLevel import BuildingLevel
from src.domain_model.project.building.level.room.BuildingLevelRoom import BuildingLevelRoom
from src.domain_model.resource.exception.BuildingLevelAlreadyHasRoomException import \
    BuildingLevelAlreadyHasRoomException


def setup_function(function):
    DomainPublishedEvents.cleanup()


def test_add_room_to_level():
    buildingId = '1'
    buildingLevelId = '1'
    # Act
    obj = BuildingLevel.createFrom(id=buildingLevelId, buildingIds=[buildingId])
    r1 = BuildingLevelRoom.createFrom(buildingLevelId=buildingId)
    obj.addRoom(r1)
    # Assert
    assert isinstance(r1, BuildingLevelRoom)
    from src.domain_model.project.building.level.BuildingLevelRoomToBuildingLevelAdded import BuildingLevelRoomToBuildingLevelAdded
    assert isinstance(DomainPublishedEvents.postponedEvents()[0], BuildingLevelRoomToBuildingLevelAdded)


def test_throw_exception_when_adding_same_room_to_level():
    buildingId = '1'
    buildingLevelId = '1'
    roomId = '1'
    # Act, Assert
    with pytest.raises(BuildingLevelAlreadyHasRoomException):
        r1 = BuildingLevelRoom.createFrom(id=roomId, buildingLevelId=buildingId)
        obj = BuildingLevel.createFrom(id=buildingLevelId, buildingIds=[buildingId], rooms=[r1])
        obj.addRoom(r1)


def test_remove_room_from_level():
    buildingId = '1'
    buildingLevelId = '1'
    roomId = '1'
    # Act
    r1 = BuildingLevelRoom.createFrom(id=roomId, buildingLevelId=buildingId)
    obj = BuildingLevel.createFrom(id=buildingLevelId, buildingIds=[buildingId], rooms=[r1])
    obj.removeRoom(r1)
    # Assert
    assert isinstance(r1, BuildingLevelRoom)
    from src.domain_model.project.building.level.BuildingLevelRoomFromBuildingLevelRemoved import BuildingLevelRoomFromBuildingLevelRemoved
    assert isinstance(DomainPublishedEvents.postponedEvents()[0], BuildingLevelRoomFromBuildingLevelRemoved)


def test_change_room_index():
    # Arrange
    buildingId = 'b1'
    roomId = '1'
    # Act
    r1 = BuildingLevelRoom.createFrom(id=roomId, buildingLevelId=buildingId)
    r1.updateIndex(index=1)
    # Assert
    assert isinstance(r1, BuildingLevelRoom)

def test_change_description():
    # Arrange
    buildingId = 'b1'
    roomId = '1'
    # Act
    r1 = BuildingLevelRoom.createFrom(id=roomId, buildingLevelId=buildingId)
    r1.updateDescription(description='new description')
    # Assert
    assert isinstance(r1, BuildingLevelRoom)
    from src.domain_model.project.building.level.room.BuildingLevelRoomDescriptionUpdated import BuildingLevelRoomDescriptionUpdated
    assert isinstance(DomainPublishedEvents.postponedEvents()[0], BuildingLevelRoomDescriptionUpdated)
    assert r1.description() == 'new description'