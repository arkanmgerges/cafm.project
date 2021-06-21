"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from copy import copy
from uuid import uuid4

from src.domain_model.common.HasToMap import HasToMap
from src.domain_model.event.DomainPublishedEvents import DomainPublishedEvents
from src.resource.logging.logger import logger


class User(HasToMap):
    def __init__(
        self,
        id: str = None,
        email: str = None,
        firstName: str = None,
        lastName: str = None,
        addressOne: str = None,
        addressTwo: str = None,
        postalCode: str = None,
        phoneNumber: str = None,
        avatarImage: str = None,
        countryId: int = 69543,
        cityId: int = 49747,
        countryStateName: str = None,
        countryStateIsoCode: str = None,
        startDate: int = None,
        skipValidation: bool = False,
        **_kwargs
    ):
        anId = str(uuid4()) if id is None else id
        self._id = anId
        self._email = email
        self._firstName = firstName
        self._lastName = lastName
        self._addressOne = addressOne
        self._addressTwo = addressTwo
        self._postalCode = postalCode
        self._phoneNumber = phoneNumber
        self._avatarImage = avatarImage
        self._countryId = (
            countryId if countryId is not None or countryId == 0 else 69543
        )
        self._cityId = cityId if cityId is not None or cityId == 0 else 49747
        self._countryStateName = countryStateName
        self._countryStateIsoCode = countryStateIsoCode
        self._startDate = startDate

    @classmethod
    def createFrom(
        cls,
        id: str = None,
        email: str = None,
        firstName: str = None,
        lastName: str = None,
        addressOne: str = None,
        addressTwo: str = None,
        postalCode: str = None,
        phoneNumber: str = None,
        avatarImage: str = None,
        countryId: int = None,
        cityId: int = None,
        countryStateName: str = None,
        countryStateIsoCode: str = None,
        startDate: float = None,
        publishEvent: bool = False,
        skipValidation: bool = False,
        **_kwargs,
    ):
        obj: User = User(
            id=id,
            email=email,
            firstName=firstName,
            lastName=lastName,
            addressOne=addressOne,
            addressTwo=addressTwo,
            postalCode=postalCode,
            phoneNumber=phoneNumber,
            avatarImage=avatarImage,
            countryId=countryId,
            cityId=cityId,
            startDate=startDate,
            countryStateName=countryStateName,
            countryStateIsoCode=countryStateIsoCode,
            skipValidation=skipValidation,
        )
        logger.debug(f"[{User.createFrom.__qualname__}] - data: {obj.toMap()}")
        if publishEvent:
            logger.debug(
                f"[{User.createFrom.__qualname__}] - publish UserCreated event"
            )
            from src.domain_model.event.DomainPublishedEvents import (
                DomainPublishedEvents,
            )
            from src.domain_model.user.UserCreated import UserCreated

            DomainPublishedEvents.addEventForPublishing(UserCreated(obj))
        return obj

    @classmethod
    def createFromObject(
        cls, obj: "User", publishEvent: bool = False, generateNewId: bool = False
    ):
        logger.debug(f"[{User.createFromObject.__qualname__}]")
        id = None if generateNewId else obj.id()
        return cls.createFrom(
            id=id,
            email=obj.email(),
            firstName=obj.firstName(),
            lastName=obj.lastName(),
            addressOne=obj.addressOne(),
            addressTwo=obj.addressTwo(),
            postalCode=obj.postalCode(),
            phoneNumber=obj.phoneNumber(),
            avatarImage=obj.avatarImage(),
            countryId=obj.countryId(),
            cityId=obj.cityId(),
            countryStateName=obj.countryStateName(),
            countryStateIsoCode=obj.countryStateIsoCode(),
            startDate=obj.startDate(),
            publishEvent=publishEvent,
        )

    def id(self) -> str:
        return self._id

    def email(self) -> str:
        return self._email

    def firstName(self) -> str:
        return self._firstName

    def lastName(self) -> str:
        return self._lastName

    def addressOne(self) -> str:
        return self._addressOne

    def addressTwo(self) -> str:
        return self._addressTwo

    def postalCode(self) -> str:
        return self._postalCode

    def phoneNumber(self) -> str:
        return self._phoneNumber

    def avatarImage(self) -> str:
        return self._avatarImage

    def countryId(self) -> int:
        return self._countryId

    def cityId(self) -> int:
        return self._cityId

    def countryStateName(self) -> str:
        return self._countryStateName

    def countryStateIsoCode(self) -> str:
        return self._countryStateIsoCode

    def startDate(self) -> int:
        return self._startDate

    def update(self, data: dict):
        updated = False
        old = copy(self)
        if (
            "email" in data
            and data["email"] != self._email
            and data["email"] is not None
        ):
            updated = True
            self._email = data["email"]
        if (
            "first_name" in data
            and data["first_name"] != self._firstName
            and data["first_name"] is not None
        ):
            updated = True
            self._firstName = data["first_name"]
        if (
            "last_name" in data
            and data["last_name"] != self._lastName
            and data["last_name"] is not None
        ):
            updated = True
            self._lastName = data["last_name"]
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
            "phone_number" in data
            and data["phone_number"] != self._phoneNumber
            and data["phone_number"] is not None
        ):
            updated = True
            self._phoneNumber = data["phone_number"]
        if (
            "avatar_image" in data
            and data["avatar_image"] != self._avatarImage
            and data["avatar_image"] is not None
        ):
            updated = True
            self._avatarImage = data["avatar_image"]
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
            "country_state_iso_code" in data
            and data["country_state_iso_code"] != self._countryStateIsoCode
            and data["country_state_iso_code"] is not None
        ):
            updated = True
            self._countryStateIsoCode = data["country_state_iso_code"]
        if (
            "start_date" in data
            and data["start_date"] != self._startDate
            and data["start_date"] is not None
        ):
            updated = True
            self._startDate = data["start_date"]
        if updated:
            self.publishUpdate(old)

    def publishDelete(self):
        from src.domain_model.user.UserDeleted import UserDeleted

        DomainPublishedEvents.addEventForPublishing(UserDeleted(self))

    def publishUpdate(self, old):
        from src.domain_model.user.UserUpdated import UserUpdated

        DomainPublishedEvents.addEventForPublishing(UserUpdated(old, self))

    def toMap(self) -> dict:
        return {
            "user_id": self.id(),
            "email": self.email(),
            "first_name": self.firstName(),
            "last_name": self.lastName(),
            "address_one": self.addressOne(),
            "address_two": self.addressTwo(),
            "postal_code": self.postalCode(),
            "phone_number": self.phoneNumber(),
            "avatar_image": self.avatarImage(),
            "country_id": self.countryId(),
            "city_id": self.cityId(),
            "country_state_name": self.countryStateName(),
            "country_state_iso_code": self.countryStateIsoCode(),
            "start_date": self.startDate(),
        }

    def __repr__(self):
        return f"<{self.__module__} object at {hex(id(self))}> {self.toMap()}"

    def __str__(self) -> str:
        return f"<{self.__module__} object at {hex(id(self))}> {self.toMap()}"

    def __eq__(self, other) -> bool:
        if not isinstance(other, User):
            raise NotImplementedError(
                f"other: {other} can not be compared with User class"
            )
        return (
            self.id() == other.id()
            and self.email() == other.email()
            and self.firstName() == other.firstName()
            and self.lastName() == other.lastName()
            and self.addressOne() == other.addressOne()
            and self.addressTwo() == other.addressTwo()
            and self.postalCode() == other.postalCode()
            and self.phoneNumber() == other.phoneNumber()
            and self.avatarImage() == other.avatarImage()
            and self.countryId() == other.countryId()
            and self.cityId() == other.cityId()
            and self.countryStateName() == other.countryStateName()
            and self.countryStateIsoCode() == other.countryStateIsoCode()
            and self.startDate() == other.startDate()
        )
