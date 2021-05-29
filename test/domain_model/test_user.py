"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from uuid import uuid4

from src.domain_model.event.DomainPublishedEvents import DomainPublishedEvents
from src.domain_model.user.User import User
from src.domain_model.user.UserDeleted import UserDeleted
from src.domain_model.user.UserUpdated import UserUpdated


def setup_function(function):
    DomainPublishedEvents.cleanup()


def test_create_user():
    # Act
    user = User("1", "2")
    # Assert
    assert isinstance(user, User)


def test_create_user_with_semantic_constructor():
    # Arrange
    id = str(uuid4())
    # Act
    user = User.createFrom(id=id, email="Prj1@test.local")
    # Assert
    assert isinstance(user, User)
    assert user.id() == id
    assert user.email() == "Prj1@test.local"


def test_that_two_objects_with_same_attributes_are_equal():
    # Act
    object1 = User.createFrom("1234", "Prj1@test.local")
    object2 = User.createFrom("1234", "Prj1@test.local")
    # Assert
    assert object1 == object2


def test_that_two_objects_with_different_attributes_are_not_equal():
    # Act
    object1 = User.createFrom("1234", "Prj1@test.local")
    object2 = User.createFrom("1234", "Prj2@test.local")
    # Assert
    assert object1 != object2


def test_that_address_be_set():
    # Act
    object1 = User.createFrom(
        id="1234",
        email="Prj1@test.local",
        firstName="fn",
        lastName="ln",
        addressOne="addr 1",
        addressTwo="addr 2",
        postalCode="1234567",
        phoneNumber="01728835748",
        avatarImage="avatar url",
        countryId=1,
        cityId=2,
        stateId="ST",
        countryStateName="ST",
        startDate=None,
    )
    # Assert
    assert object1.id() == "1234"
    assert object1.email() == "Prj1@test.local"
    assert object1.firstName() == "fn"
    assert object1.lastName() == "ln"
    assert object1.addressOne() == "addr 1"
    assert object1.addressTwo() == "addr 2"
    assert object1.postalCode() == "1234567"
    assert object1.phoneNumber() == "01728835748"
    assert object1.avatarImage() == "avatar url"
    assert object1.countryId() == 1
    assert object1.cityId() == 2
    assert object1.stateId() == "ST"
    assert object1.countryStateName() == "ST"
    assert object1.startDate() is None


def test_user_update():
    # Act
    object1 = User.createFrom(
        id="1234",
        email="Prj1@test.local",
        firstName="fn",
        lastName="ln",
        addressOne="addr 1",
        addressTwo="addr 2",
        postalCode="1234567",
        phoneNumber="01728835748",
        avatarImage="avatar url",
        countryId=1,
        cityId=2,
        stateId="ST",
        countryStateName="ST",
        startDate=None,
    )
    object1.update(
        {"first_name": "new fn", "last_name": "new ln", "phone_number": "000000"}
    )
    # Assert
    assert len(DomainPublishedEvents.postponedEvents()) == 1
    assert isinstance(DomainPublishedEvents.postponedEvents()[0], UserUpdated)
    assert object1.firstName() == "new fn"
    assert object1.lastName() == "new ln"
    assert object1.phoneNumber() == "000000"


def test_user_deleted_event():
    # Act
    object1 = User.createFrom(
        id="1234",
        email="Prj1@test.local",
        firstName="fn",
        lastName="ln",
        addressOne="addr 1",
        addressTwo="addr 2",
        postalCode="1234567",
        avatarImage="avatar url",
    )
    object1.publishDelete()
    # Assert
    assert len(DomainPublishedEvents.postponedEvents()) == 1
    assert isinstance(DomainPublishedEvents.postponedEvents()[0], UserDeleted)
