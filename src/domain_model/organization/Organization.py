"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from copy import copy
from uuid import uuid4

from src.domain_model.event.DomainPublishedEvents import DomainPublishedEvents
from src.domain_model.organization.OrganizationType import OrganizationType
from src.resource.logging.logger import logger


class Organization:
    def __init__(
        self,
        id: str = None,
        name: str = None,
        websiteUrl: str = None,
        organizationType: str = None,
        addressOne: str = None,
        addressTwo: str = None,
        postalCode: str = None,
        countryId: int = 69543,
        cityId: int = 49747,
        countryStateName: str = None,
        managerFirstName: str = None,
        managerLastName: str = None,
        managerEmail: str = None,
        managerPhoneNumber: str = None,
        managerAvatar: str = None,
        skipValidation: bool = False,
    ):
        anId = str(uuid4()) if id is None else id
        self._id = anId
        self._name = name
        self._websiteUrl = websiteUrl
        if not skipValidation:
            if not self._isOrganizationType(organizationType):
                from src.domain_model.resource.exception.InvalidOrganizationTypeException import (
                    InvalidOrganizationTypeException,
                )

                raise InvalidOrganizationTypeException(
                    "Invalid organization type, only these types are supported: "
                    + ", ".join([e.value for e in OrganizationType])
                )
        self._organizationType = organizationType
        self._addressOne = addressOne
        self._addressTwo = addressTwo
        self._postalCode = postalCode
        self._countryId = countryId if countryId is not None else 69543
        self._cityId = cityId if cityId is not None else 49747
        self._countryStateName = countryStateName
        self._managerFirstName = managerFirstName
        self._managerLastName = managerLastName
        self._managerEmail = managerEmail
        self._managerPhoneNumber = managerPhoneNumber
        self._managerAvatar = managerAvatar

    @classmethod
    def createFrom(
        cls,
        id: str = None,
        name: str = None,
        websiteUrl: str = None,
        organizationType: str = None,
        addressOne: str = None,
        addressTwo: str = None,
        postalCode: str = None,
        countryId: int = None,
        cityId: int = None,
        countryStateName: str = None,
        managerFirstName: str = None,
        managerLastName: str = None,
        managerEmail: str = None,
        managerPhoneNumber: str = None,
        managerAvatar: str = None,
        publishEvent: bool = False,
        skipValidation: bool = False,
    ):
        organization: Organization = Organization(
            id=id,
            name=name,
            websiteUrl=websiteUrl,
            organizationType=organizationType,
            addressOne=addressOne,
            addressTwo=addressTwo,
            postalCode=postalCode,
            countryId=countryId,
            cityId=cityId,
            countryStateName=countryStateName,
            managerFirstName=managerFirstName,
            managerLastName=managerLastName,
            managerEmail=managerEmail,
            managerPhoneNumber=managerPhoneNumber,
            managerAvatar=managerAvatar,
            skipValidation=skipValidation,
        )
        logger.debug(
            f"[{Organization.createFrom.__qualname__}] - data: {organization.toMap()}"
        )
        if publishEvent:
            logger.debug(
                f"[{Organization.createFrom.__qualname__}] - publish OrganizationCreated event"
            )
            from src.domain_model.event.DomainPublishedEvents import (
                DomainPublishedEvents,
            )
            from src.domain_model.organization.OrganizationCreated import (
                OrganizationCreated,
            )

            DomainPublishedEvents.addEventForPublishing(
                OrganizationCreated(organization)
            )
        return organization

    @classmethod
    def createFromObject(
        cls,
        obj: "Organization",
        publishEvent: bool = False,
        generateNewId: bool = False,
        skipValidation: bool = False,
    ):
        logger.debug(f"[{Organization.createFromObject.__qualname__}]")
        id = None if generateNewId else obj.id()
        return cls.createFrom(
            id=id,
            name=obj.name(),
            websiteUrl=obj.websiteUrl(),
            organizationType=obj.organizationType(),
            addressOne=obj.addressOne(),
            addressTwo=obj.addressTwo(),
            postalCode=obj.postalCode(),
            countryId=obj.countryId(),
            cityId=obj.cityId(),
            countryStateName=obj.countryStateName(),
            managerFirstName=obj.managerFirstName(),
            managerLastName=obj.managerLastName(),
            managerEmail=obj.managerEmail(),
            managerPhoneNumber=obj.managerPhoneNumber(),
            managerAvatar=obj.managerAvatar(),
            publishEvent=publishEvent,
            skipValidation=skipValidation,
        )

    def id(self) -> str:
        return self._id

    def name(self) -> str:
        return self._name

    def websiteUrl(self) -> str:
        return self._websiteUrl

    def organizationType(self) -> str:
        return self._organizationType

    def addressOne(self) -> str:
        return self._addressOne

    def addressTwo(self) -> str:
        return self._addressTwo

    def postalCode(self) -> str:
        return self._postalCode

    def countryId(self) -> int:
        return self._countryId

    def cityId(self) -> int:
        return self._cityId

    def countryStateName(self) -> str:
        return self._countryStateName

    def managerFirstName(self) -> str:
        return self._managerFirstName

    def managerLastName(self) -> str:
        return self._managerLastName

    def managerEmail(self) -> str:
        return self._managerEmail

    def managerPhoneNumber(self) -> str:
        return self._managerPhoneNumber

    def managerAvatar(self) -> str:
        return self._managerAvatar

    def update(self, data: dict):
        updated = False
        old = copy(self)
        if "name" in data and data["name"] != self._name and data["name"] is not None:
            updated = True
            self._name = data["name"]
        if (
            "website_url" in data
            and data["website_url"] != self._websiteUrl
            and data["website_url"] is not None
        ):
            updated = True
            self._websiteUrl = data["website_url"]
        if (
            "organization_type" in data
            and data["organization_type"] != self._organizationType
            and data["organization_type"] is not None
        ):
            updated = True
            self._organizationType = data["organization_type"]
        if (
            "address_one" in data
            and data["address_one"] != self._addressOne
            and data["address_one"] is not None
        ):
            updated = True
            self._addressOne = data["address_one"]
        if (
            "address_two" in data
            and data["address_two"] != self._addressTwo
            and data["address_two"] is not None
        ):
            updated = True
            self._addressTwo = data["address_two"]
        if (
            "postal_code" in data
            and data["postal_code"] != self._postalCode
            and data["postal_code"] is not None
        ):
            updated = True
            self._postalCode = data["postal_code"]
        if (
            "country_id" in data
            and data["country_id"] != self._countryId
            and data["country_id"] is not None
        ):
            updated = True
            self._countryId = data["country_id"]
        if (
            "city_id" in data
            and data["city_id"] != self._cityId
            and data["city_id"] is not None
        ):
            updated = True
            self._cityId = data["city_id"]
        if (
            "country_state_name" in data
            and data["country_state_name"] != self._countryStateName
            and data["country_state_name"] is not None
        ):
            updated = True
            self._countryStateName = data["country_state_name"]
        if (
            "manager_first_name" in data
            and data["manager_first_name"] != self._managerFirstName
            and data["manager_first_name"] is not None
        ):
            updated = True
            self._managerFirstName = data["manager_first_name"]
        if (
            "manager_last_name" in data
            and data["manager_last_name"] != self._managerLastName
            and data["manager_last_name"] is not None
        ):
            updated = True
            self._managerLastName = data["manager_last_name"]
        if (
            "manager_email" in data
            and data["manager_email"] != self._managerEmail
            and data["manager_email"] is not None
        ):
            updated = True
            self._managerEmail = data["manager_email"]
        if (
            "manager_phone_number" in data
            and data["manager_phone_number"] != self._managerPhoneNumber
            and data["manager_phone_number"] is not None
        ):
            updated = True
            self._managerPhoneNumber = data["manager_phone_number"]
        if (
            "manager_avatar" in data
            and data["manager_avatar"] != self._managerAvatar
            and data["manager_avatar"] is not None
        ):
            updated = True
            self._managerAvatar = data["manager_avatar"]
        if updated:
            self.publishUpdate(old)

    def _isOrganizationType(self, organizationType: str) -> bool:
        return organizationType in OrganizationType._value2member_map_

    def publishDelete(self):
        from src.domain_model.organization.OrganizationDeleted import (
            OrganizationDeleted,
        )

        DomainPublishedEvents.addEventForPublishing(OrganizationDeleted(self))

    def publishUpdate(self, old):
        from src.domain_model.organization.OrganizationUpdated import (
            OrganizationUpdated,
        )

        DomainPublishedEvents.addEventForPublishing(OrganizationUpdated(old, self))

    def toMap(self) -> dict:
        return {
            "organization_id": self.id(),
            "name": self.name(),
            "website_url": self.websiteUrl(),
            "organization_type": self.organizationType(),
            "address_one": self.addressOne(),
            "address_two": self.addressTwo(),
            "postal_code": self.postalCode(),
            "country_id": self.countryId(),
            "city_id": self.cityId(),
            "country_state_name": self.countryStateName(),
            "manager_first_name": self.managerFirstName(),
            "manager_last_name": self.managerLastName(),
            "manager_email": self.managerEmail(),
            "manager_phone_number": self.managerPhoneNumber(),
            "manager_avatar": self.managerAvatar(),
        }

    def __repr__(self):
        return f"<{self.__module__} object at {hex(id(self))}> {self.toMap()}"

    def __str__(self) -> str:
        return f"<{self.__module__} object at {hex(id(self))}> {self.toMap()}"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Organization):
            raise NotImplementedError(
                f"other: {other} can not be compared with User class"
            )
        return (
            self.id() == other.id()
            and self.name() == other.name()
            and self.websiteUrl() == other.websiteUrl()
            and self.organizationType() == other.organizationType()
            and self.addressOne() == other.addressOne()
            and self.addressTwo() == other.addressTwo()
            and self.postalCode() == other.postalCode()
            and self.countryId() == other.countryId()
            and self.cityId() == other.cityId()
            and self.countryStateName() == other.countryStateName()
            and self.managerFirstName() == other.managerFirstName()
            and self.managerLastName() == other.managerLastName()
            and self.managerEmail() == other.managerEmail()
            and self.managerPhoneNumber() == other.managerPhoneNumber()
            and self.managerAvatar() == other.managerAvatar()
        )
