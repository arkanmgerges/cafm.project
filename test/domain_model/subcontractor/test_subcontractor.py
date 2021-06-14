"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

import pytest

from src.domain_model.event.DomainPublishedEvents import DomainPublishedEvents
from src.domain_model.subcontractor.Subcontractor import Subcontractor


def setup_function(function):
    DomainPublishedEvents.cleanup()


def test_create_object():
    # Act
    obj = _create_object()
    # Assert
    assert isinstance(obj, Subcontractor)


def test_company_name():
    # Act
    obj = _create_object()
    # Assert
    assert obj.companyName() == "company_name"


def test_website_url():
    # Act
    obj = _create_object()
    # Assert
    assert obj.websiteUrl() == "website_url"


def test_contact_person():
    # Act
    obj = _create_object()
    # Assert
    assert obj.contactPerson() == "contact_person"


def test_email():
    # Act
    obj = _create_object()
    # Assert
    assert obj.email() == "email"


def test_phone_number():
    # Act
    obj = _create_object()
    # Assert
    assert obj.phoneNumber() == "phone_number"


def test_address_one():
    # Act
    obj = _create_object()
    # Assert
    assert obj.addressOne() == "address_one"


def test_address_two():
    # Act
    obj = _create_object()
    # Assert
    assert obj.addressTwo() == "address_two"


def test_subcontractor_category_id():
    # Act
    obj = _create_object()
    # Assert
    assert obj.subcontractorCategoryId() == "subcontractor_category_id"


def test_description():
    # Act
    obj = _create_object()
    # Assert
    assert obj.description() == "description"


def test_city_id():
    # Act
    obj = _create_object()
    # Assert
    assert obj.cityId() == 1


def test_country_id():
    # Act
    obj = _create_object()
    # Assert
    assert obj.countryId() == 1


def test_country_state_iso_code():
    # Act
    obj = _create_object()
    # Assert
    assert obj.countryStateIsoCode() == "country_state_iso_code"

def test_country_state_name():
    # Act
    obj = _create_object()
    # Assert
    assert obj.countryStateName() == "country_state_name"

def test_postal_code():
    # Act
    obj = _create_object()
    # Assert
    assert obj.postalCode() == "postal_code"


def test_create_from_object():
    # Act
    obj = _create_object()
    obj2 = Subcontractor.createFromObject(obj=obj)
    # Assert
    assert obj == obj2


def test_toMap():
    # Arrange
    obj = _create_object(
        id="1",
        companyName="company_name",
        websiteUrl="website_url",
        contactPerson="contact_person",
        email="email",
        phoneNumber="phone_number",
        addressOne="address_one",
        addressTwo="address_two",
        subcontractorCategoryId="subcontractor_category_id",
        description="description",
        cityId=1,
        countryId=1,
        countryStateIsoCode="country_state_iso_code",
        countryStateName="country_state_name",
        postalCode="postal_code",
    )
    currentMap = {
        "subcontractor_id": "1",
        "company_name": "company_name",
        "website_url": "website_url",
        "contact_person": "contact_person",
        "email": "email",
        "phone_number": "phone_number",
        "address_one": "address_one",
        "address_two": "address_two",
        "subcontractor_category_id": "subcontractor_category_id",
        "description": "description",
        "city_id": 1,
        "country_id": 1,
        "postal_code": "postal_code",
        "country_state_iso_code": "country_state_iso_code",
        "country_state_name": "country_state_name",
    }
    # Act
    objectMap = obj.toMap()

    # Assert
    assert objectMap == currentMap
    assert len(objectMap.keys()) == len(currentMap.keys())


def _create_object(
    id: str = None,
    companyName: str = None,
    websiteUrl: str = None,
    contactPerson: str = None,
    email: str = None,
    phoneNumber: str = None,
    addressOne: str = None,
    addressTwo: str = None,
    subcontractorCategoryId: str = None,
    description: str = None,
    cityId: int = None,
    countryId: int = None,
    countryStateIsoCode: str = None,
    countryStateName: str = None,
    postalCode: str = None,
    skipValidation: bool = False,
):
    id = "1" if id is None else id
    companyName = "company_name" if companyName is None else companyName
    websiteUrl = "website_url" if websiteUrl is None else websiteUrl
    contactPerson = "contact_person" if contactPerson is None else contactPerson
    email = "email" if email is None else email
    phoneNumber = "phone_number" if phoneNumber is None else phoneNumber
    addressOne = "address_one" if addressOne is None else addressOne
    addressTwo = "address_two" if addressTwo is None else addressTwo
    subcontractorCategoryId = (
        "subcontractor_category_id"
        if subcontractorCategoryId is None
        else subcontractorCategoryId
    )
    description = "description" if description is None else description
    cityId = 1 if cityId is None else cityId
    countryId = 1 if countryId is None else countryId
    countryStateIsoCode = "country_state_iso_code" if countryStateIsoCode is None else countryStateIsoCode
    countryStateName = "country_state_name" if countryStateName is None else countryStateName
    postalCode = "postal_code" if postalCode is None else postalCode

    return Subcontractor.createFrom(
        id=id,
        companyName=companyName,
        websiteUrl=websiteUrl,
        contactPerson=contactPerson,
        email=email,
        phoneNumber=phoneNumber,
        addressOne=addressOne,
        addressTwo=addressTwo,
        subcontractorCategoryId=subcontractorCategoryId,
        description=description,
        cityId=cityId,
        countryId=countryId,
        countryStateName=countryStateName,
        countryStateIsoCode=countryStateIsoCode,
        postalCode=postalCode,
        skipValidation=skipValidation,
    )
