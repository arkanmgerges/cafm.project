"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from uuid import uuid4

from src.domain_model.event.DomainPublishedEvents import DomainPublishedEvents
from src.domain_model.organization.Organization import Organization
from src.domain_model.organization.OrganizationDeleted import OrganizationDeleted
from src.domain_model.organization.OrganizationUpdated import OrganizationUpdated


def setup_function(function):
    DomainPublishedEvents.cleanup()


def test_create_organization():
    # Act
    organization = Organization(id='1', name='2')
    # Assert
    assert isinstance(organization, Organization)


def test_create_organization_with_semantic_constructor():
    # Arrange
    id = str(uuid4())
    # Act
    obj = Organization.createFrom(id=id,
                                  name='org1',
                                  websiteUrl='local.me',
                                  organizationType='provider',
                                  addressOne='ad one',
                                  addressTwo='ad two',
                                  postalCode='1234',
                                  countryId=1,
                                  cityId=2,
                                  countryStateName='ST',
                                  managerFirstName='mn fn',
                                  managerLastName='mn ln',
                                  managerEmail='mn@local.me',
                                  managerPhoneNumber='0001234',
                                  managerAvatar='http://avt.local')
    # Assert
    assert isinstance(obj, Organization)
    assert obj.id() == id
    assert obj.name() == 'org1'
    assert obj.organizationType() == 'provider'
    assert obj.addressOne() == 'ad one'
    assert obj.addressTwo() == 'ad two'
    assert obj.postalCode() == '1234'
    assert obj.countryId() == 1
    assert obj.cityId() == 2
    assert obj.countryStateName() == 'ST'
    assert obj.managerFirstName() == 'mn fn'
    assert obj.managerLastName() == 'mn ln'
    assert obj.managerEmail() == 'mn@local.me'
    assert obj.managerPhoneNumber() == '0001234'
    assert obj.managerAvatar() == 'http://avt.local'


def test_that_two_objects_with_same_attributes_are_equal():
    # Act
    object1 = Organization.createFrom(id='1234', name='org1')
    object2 = Organization.createFrom(id='1234', name='org1')
    # Assert
    assert object1 == object2


def test_that_two_objects_with_different_attributes_are_not_equal():
    # Act
    object1 = Organization.createFrom(id='1234', name='n1')
    object2 = Organization.createFrom(id='1234', name='n2')
    # Assert
    assert object1 != object2


def test_that_address_be_set():
    # Act
    object1 = Organization.createFrom(id='1234',
                                      name='org1',
                                      websiteUrl='local.me',
                                      organizationType='provider',
                                      addressOne='ad one',
                                      addressTwo='ad two',
                                      postalCode='1234',
                                      countryId=1,
                                      cityId=2,
                                      countryStateName='ST',
                                      managerFirstName='mn fn',
                                      managerLastName='mn ln',
                                      managerEmail='mn@local.me',
                                      managerPhoneNumber='0001234',
                                      managerAvatar='http://avt.local')
    # Assert
    assert object1.id() == '1234'
    assert object1.name() == 'org1'
    assert object1.websiteUrl() == 'local.me'
    assert object1.organizationType() == 'provider'
    assert object1.addressOne() == 'ad one'
    assert object1.addressTwo() == 'ad two'
    assert object1.postalCode() == '1234'
    assert object1.countryId() == 1
    assert object1.cityId() == 2
    assert object1.countryStateName() == 'ST'
    assert object1.managerFirstName() == 'mn fn'
    assert object1.managerLastName() == 'mn ln'
    assert object1.managerEmail() == 'mn@local.me'
    assert object1.managerPhoneNumber() == '0001234'
    assert object1.managerAvatar() == 'http://avt.local'


def test_organization_update():
    # Act
    object1 = Organization.createFrom(id='1234',
                                      name='org1',
                                      websiteUrl='local.me',
                                      organizationType='provider',
                                      addressOne='ad one',
                                      addressTwo='ad two',
                                      postalCode='1234',
                                      countryId=1,
                                      cityId=2,
                                      countryStateName='ST',
                                      managerFirstName='mn fn',
                                      managerLastName='mn ln',
                                      managerEmail='mn@local.me',
                                      managerPhoneNumber='0001234',
                                      managerAvatar='http://avt.local')
    object1.update({'manager_first_name': 'new mn fn', 'manager_last_name': 'new mn ln',
                    'manager_phone_number': '000000'})
    # Assert
    assert len(DomainPublishedEvents.postponedEvents()) == 1
    assert isinstance(DomainPublishedEvents.postponedEvents()[0], OrganizationUpdated)
    assert object1.managerFirstName() == 'new mn fn'
    assert object1.managerLastName() == 'new mn ln'
    assert object1.managerPhoneNumber() == '000000'


def test_organization_deleted_event():
    # Act
    object1 = Organization.createFrom(id='1234', name='nm')
    object1.publishDelete()
    # Assert
    assert len(DomainPublishedEvents.postponedEvents()) == 1
    assert isinstance(DomainPublishedEvents.postponedEvents()[0], OrganizationDeleted)
