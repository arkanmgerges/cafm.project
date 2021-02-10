"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import pytest

from src.domain_model.event.DomainPublishedEvents import DomainPublishedEvents
from src.domain_model.project.building.Building import Building
from src.domain_model.project.building.level.BuildingLevel import BuildingLevel
from src.domain_model.resource.exception.InvalidArgumentException import InvalidArgumentException


def setup_function(function):
    DomainPublishedEvents.cleanup()


def test_create_building_object():
    # Act
    obj = Building(projectId='1')
    # Assert
    assert isinstance(obj, Building)


def test_create_building_has_project_id():
    projectId = '1'
    # Act
    obj = Building(projectId=projectId)
    # Assert
    assert obj.projectId() == projectId


def test_throw_invalid_argument_exception_when_project_id_is_invalid():
    # Arrange
    projectId = None
    # Act, Assert
    with pytest.raises(InvalidArgumentException):
        obj = Building(projectId=projectId)


def test_create_building_from_class_method():
    # Arrange
    projectId = '1'
    # Act
    obj = Building.createFrom(projectId=projectId)
    # Assert
    assert obj.projectId() == projectId


def test_create_building_from_another_object():
    # Arrange
    projectId = '1'
    obj1 = Building.createFrom(projectId=projectId)
    # Act
    obj2 = Building.createFromObject(obj=obj1)
    # Assert
    assert obj1.projectId() == obj2.projectId()


def test_throw_invalid_argument_exception_when_creating_from_object_that_is_invalid():
    # Act, Assert
    with pytest.raises(InvalidArgumentException):
        obj = Building.createFromObject(obj=None)


def test_throw_publish_domain_event_when_building_is_created():
    # Arrange
    projectId = '1'
    # Act
    obj = Building.createFrom(projectId=projectId, publishEvent=True)
    # Assert
    from src.domain_model.project.building.BuildingCreated import BuildingCreated
    assert isinstance(DomainPublishedEvents.postponedEvents()[0], BuildingCreated)


def test_add_level():
    # Arrange
    projectId = '1'
    # Act
    obj = Building.createFrom(projectId=projectId)
    obj2 = BuildingLevel.createFrom(buildingIds=[obj.id()])
    obj.addLevel(level=obj2)
    # Assert
    assert isinstance(obj2, BuildingLevel)
    from src.domain_model.project.building.BuildingLevelToBuildingAdded import BuildingLevelToBuildingAdded
    assert isinstance(DomainPublishedEvents.postponedEvents()[0], BuildingLevelToBuildingAdded)


def test_remove_level():
    # Arrange
    buildingId = '1'
    projectId = '2'
    # Act
    obj2 = BuildingLevel.createFrom(buildingIds=[buildingId])
    obj = Building.createFrom(id=buildingId, projectId=projectId, buildingLevels=[obj2])
    obj.removeLevel(level=obj2)
    # Assert
    assert isinstance(obj2, BuildingLevel)
    from src.domain_model.project.building.BuildingLevelToBuildingRemoved import BuildingLevelToBuildingRemoved
    assert isinstance(DomainPublishedEvents.postponedEvents()[0], BuildingLevelToBuildingRemoved)


def test_throw_level_already_exist_when_adding_same_level_to_building():
    # Arrange
    buildingId = '1'
    projectId = '2'
    # Act, Assert
    from src.domain_model.resource.exception.BuildingLevelAlreadyExistException import \
        BuildingLevelAlreadyExistException
    with pytest.raises(BuildingLevelAlreadyExistException):
        obj2 = BuildingLevel.createFrom(buildingIds=[buildingId])
        obj = Building.createFrom(id=buildingId, projectId=projectId, buildingLevels=[obj2])
        obj.addLevel(level=obj2)


def test_throw_level_does_not_exist_when_removing_unexistent_level_from_building():
    # Arrange
    buildingId = '1'
    projectId = '2'
    # Act, Assert
    from src.domain_model.resource.exception.BuildingLevelDoesNotExistException import \
        BuildingLevelDoesNotExistException
    with pytest.raises(BuildingLevelDoesNotExistException):
        obj2 = BuildingLevel.createFrom(buildingIds=[buildingId])
        obj = Building.createFrom(id=buildingId, projectId=projectId)
        obj.removeLevel(level=obj2)


def test_link_two_buildings_to_one_level():
    # Arrange
    buildingId1 = 'b1'
    buildingId2 = 'b2'
    projectId = '1'
    # Act
    level: BuildingLevel = BuildingLevel.createFrom(buildingIds=[buildingId1])
    objBuilding1 = Building.createFrom(id=buildingId1, projectId=projectId)
    objBuilding2 = Building.createFrom(id=buildingId2, projectId=projectId)
    level.linkBuildingById(buildingId=objBuilding2.id())
    # Assert
    assert len(level.buildingIds()) == 2
    from src.domain_model.project.building.level.BuildingLevelToBuildingLinked import BuildingLevelToBuildingLinked
    assert isinstance(DomainPublishedEvents.postponedEvents()[0], BuildingLevelToBuildingLinked)


def test_link_already_linked_level_to_building():
    # Arrange
    buildingId = '1'
    projectId = '2'
    # Act, Assert
    from src.domain_model.resource.exception.BuildingLevelAlreadyLinkedToBuildingException import \
        BuildingLevelAlreadyLinkedToBuildingException
    with pytest.raises(BuildingLevelAlreadyLinkedToBuildingException):
        obj2 = BuildingLevel.createFrom(buildingIds=[buildingId])
        obj = Building.createFrom(id=buildingId, projectId=projectId)
        obj2.linkBuildingById(buildingId=obj.id())


def test_unlink_building_from_building_level():
    # Arrange
    buildingId1 = 'b1'
    buildingId2 = 'b2'
    projectId = '1'
    # Act
    level: BuildingLevel = BuildingLevel.createFrom(buildingIds=[buildingId1])
    objBuilding1 = Building.createFrom(id=buildingId1, projectId=projectId)
    objBuilding2 = Building.createFrom(id=buildingId2, projectId=projectId)
    level.linkBuildingById(buildingId=objBuilding2.id())
    level.unlinkBuildingById(buildingId=buildingId2)
    # Assert
    assert len(level.buildingIds()) == 1

    from src.domain_model.project.building.level.BuildingLevelToBuildingUnlinked import BuildingLevelToBuildingUnlinked
    assert isinstance(DomainPublishedEvents.postponedEvents()[1], BuildingLevelToBuildingUnlinked)


