"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from uuid import uuid4

from src.domain_model.project.Project import Project


def test_create_project():
    # Act
    project = Project('1', '2')
    # Assert
    assert isinstance(project, Project)


def test_create_project_with_semantic_constructor():
    # Arrange
    id = str(uuid4())
    # Act
    project = Project.createFrom(id=id, name='Prj1')
    # Assert
    assert isinstance(project, Project)
    assert project.id() == id
    assert project.name() == 'Prj1'


def test_that_two_objects_with_same_attributes_are_equal():
    # Act
    object1 = Project.createFrom('1234', 'test')
    object2 = Project.createFrom('1234', 'test')
    # Assert
    assert object1 == object2


def test_that_two_objects_with_different_attributes_are_not_equal():
    # Act
    object1 = Project.createFrom('1234', 'test')
    object2 = Project.createFrom('1234', 'test2')
    # Assert
    assert object1 != object2

def test_that_address_be_set():
    # Act
    object1 = Project.createFrom('1234', 'test', cityId=1, countryId=1, addressLine='this is a test address')
    # Assert
    assert object1.cityId() == 1
    assert object1.countryId() == 1
    assert object1.addressLine() == 'this is a test address'

def test_that_beneficiary_be_set():
    # Act
    object1 = Project.createFrom('1234', 'test', 1,1,'', '1222')
    # Assert
    assert object1.beneficiaryId() == '1222'