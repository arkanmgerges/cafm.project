"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from uuid import uuid4

from src.domain_model.event.DomainPublishedEvents import DomainPublishedEvents
from src.domain_model.role.Role import Role
from src.domain_model.role.RoleDeleted import RoleDeleted
from src.domain_model.role.RoleUpdated import RoleUpdated


def setup_function(function):
    DomainPublishedEvents.cleanup()


def test_create_role():
    # Act
    role = Role(id='1', name='role1', title='title')
    # Assert
    assert isinstance(role, Role)


def test_create_role_with_semantic_constructor():
    # Arrange
    id = str(uuid4())
    # Act
    role = Role.createFrom(id=id, name='r1', title='title')
    # Assert
    assert isinstance(role, Role)
    assert role.id() == id
    assert role.name() == 'r1'
    assert role.title() == 'title'


def test_that_two_objects_with_same_attributes_are_equal():
    # Act
    object1 = Role.createFrom('1234', 'r1', 'title')
    object2 = Role.createFrom('1234', 'r1', 'title')
    # Assert
    assert object1 == object2


def test_that_two_objects_with_different_attributes_are_not_equal():
    # Act
    object1 = Role.createFrom('1234', 'r1', 'title')
    object2 = Role.createFrom('1234', 'r2', 'title2')
    # Assert
    assert object1 != object2


def test_that_address_be_set():
    # Act
    object1 = Role.createFrom(id='1234', name='r1', title="title")
    # Assert
    assert object1.id() == '1234'
    assert object1.name() == 'r1'
    assert object1.title() == 'title'


def test_role_update():
    # Act
    object1 = Role.createFrom(id='1234', name='r1', title="title")
    object1.update({'name': 'new role', 'title': 'new title'})
    # Assert
    assert len(DomainPublishedEvents.postponedEvents()) == 1
    assert isinstance(DomainPublishedEvents.postponedEvents()[0], RoleUpdated)
    assert object1.name() == 'new role'
    assert object1.title() == 'new title'


def test_role_deleted_event():
    # Act
    object1 = Role.createFrom(id='1234', name='r1', title="title")
    object1.publishDelete()
    # Assert
    assert len(DomainPublishedEvents.postponedEvents()) == 1
    assert isinstance(DomainPublishedEvents.postponedEvents()[0], RoleDeleted)
