"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from uuid import uuid4

import pytest

from src.domain_model.event.DomainPublishedEvents import DomainPublishedEvents
from src.domain_model.project.Project import Project
from src.domain_model.project.ProjectState import ProjectState
from src.domain_model.project.ProjectStateChanged import ProjectStateChanged
from src.domain_model.resource.exception.ProjectStateException import (
    ProjectStateException,
)


def setup_function(function):
    DomainPublishedEvents.cleanup()


def test_create_project():
    # Act
    project = Project("1", "2")
    # Assert
    assert isinstance(project, Project)


def test_create_project_with_semantic_constructor():
    # Arrange
    id = str(uuid4())
    # Act
    project = Project.createFrom(id=id, name="Prj1")
    # Assert
    assert isinstance(project, Project)
    assert project.id() == id
    assert project.name() == "Prj1"


def test_that_two_objects_with_same_attributes_are_equal():
    # Act
    object1 = Project.createFrom("1234", "test")
    object2 = Project.createFrom("1234", "test")
    # Assert
    assert object1 == object2


def test_that_two_objects_with_different_attributes_are_not_equal():
    # Act
    object1 = Project.createFrom("1234", "test")
    object2 = Project.createFrom("1234", "test2")
    # Assert
    assert object1 != object2


def test_that_address_be_set():
    # Act
    object1 = Project.createFrom(
        "1234", "test", cityId=1, countryId=1, addressLine="this is a test address"
    )
    # Assert
    assert object1.cityId() == 1
    assert object1.countryId() == 1
    assert object1.addressLine() == "this is a test address"


def test_that_beneficiary_be_set():
    # Act
    object1 = Project.createFrom(
        id="1234",
        name="test",
        cityId=1,
        countryId=1,
        addressLine="",
        beneficiaryId="1222",
    )
    # Assert
    assert object1.beneficiaryId() == "1222"


def test_project_state_is_draft_when_it_is_created():
    # Act
    object1 = Project.createFrom(
        id="1234",
        name="projec-1",
        cityId=1,
        countryId=1,
        addressLine="address 1",
        beneficiaryId="1234",
    )
    # Assert
    assert object1.state() == ProjectState.DRAFT


def test_project_state_publish_event_when_change_state():
    # Act
    object1 = Project.createFrom(
        id="1234",
        name="projec-1",
        cityId=1,
        countryId=1,
        addressLine="address 1",
        beneficiaryId="1234",
    )
    object1.changeState(ProjectState.ACTIVE)
    # Assert
    assert len(DomainPublishedEvents.postponedEvents()) == 1
    assert isinstance(DomainPublishedEvents.postponedEvents()[0], ProjectStateChanged)
    assert object1.state() == ProjectState.ACTIVE


def test_project_state_throw_exception_when_change_state_from_active_to_draft():
    # Act
    object1 = Project.createFrom(
        id="1234",
        name="projec-1",
        cityId=1,
        countryId=1,
        addressLine="address 1",
        beneficiaryId="1234",
    )
    object1.changeState(ProjectState.ACTIVE)
    # Assert
    with pytest.raises(ProjectStateException):
        object1.changeState(ProjectState.DRAFT)
