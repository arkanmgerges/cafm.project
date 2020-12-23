"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from copy import copy
from uuid import uuid4

from src.domain_model.event.DomainPublishedEvents import DomainPublishedEvents
from src.resource.logging.logger import logger


class User:
    def __init__(self, id: str = None, name='', password='', firstName='', lastName='',
                 addressOne='', addressTwo='', postalCode='', avatarImage=''):
        anId = str(uuid4()) if id is None or id == '' else id
        self._id = anId
        self._name = name
        self._password = password
        self._firstName = firstName
        self._lastName = lastName
        self._addressOne = addressOne
        self._addressTwo = addressTwo
        self._postalCode = postalCode
        self._avatarImage = avatarImage

    @classmethod
    def createFrom(cls, id: str = None, name='', password='', firstName='', lastName='',
                   addressOne='', addressTwo='', postalCode='', avatarImage='', publishEvent: bool = False):
        logger.debug(f'[{User.createFrom.__qualname__}] - with name {name}')
        user = User(id, name, password, firstName, lastName,
                    addressOne, addressTwo, postalCode, avatarImage)
        if publishEvent:
            logger.debug(f'[{User.createFrom.__qualname__}] - publish UserCreated event')
            from src.domain_model.event.DomainPublishedEvents import DomainPublishedEvents
            from src.domain_model.user.UserCreated import UserCreated
            DomainPublishedEvents.addEventForPublishing(UserCreated(user))
        return user

    def id(self) -> str:
        return self._id

    def name(self) -> str:
        return self._name

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

    def avatarImage(self) -> str:
        return self._avatarImage

    def update(self, data: dict):
        updated = False
        old = copy(self)
        if 'name' in data and data['name'] != self._name and data['name'] is not None:
            updated = True
            self._name = data['name']
        if 'password' in data and data['password'] != self._password and data['password'] is not None:
            updated = True
            self._password = data['password']
        if 'first_name' in data and data['first_name'] != self._firstName and data['first_name'] is not None:
            updated = True
            self._firstName = data['first_name']
        if 'last_name' in data and data['last_name'] != self._lastName and data['last_name'] is not None:
            updated = True
            self._lastName = data['last_name']
        if 'address_one' in data and data['address_one'] != self._addressOne and data['address_one'] is not None:
            updated = True
            self._addressOne = data['address_one']
        if 'address_two' in data and data['address_two'] != self._addressTwo and data['address_two'] is not None:
            updated = True
            self._addressTwo = data['address_two']
        if 'postal_code' in data and data['postal_code'] != self._postalCode and data['postal_code'] is not None:
            updated = True
            self._postalCode = data['postal_code']
        if 'avatar_image' in data and data['avatar_image'] != self._avatarImage and data['avatar_image'] is not None:
            updated = True
            self._avatarImage = data['avatar_image']
        if updated:
            self.publishUpdate(old)

    def password(self) -> str:
        return self._password

    def publishDelete(self):
        from src.domain_model.user.UserDeleted import UserDeleted
        DomainPublishedEvents.addEventForPublishing(UserDeleted(self))

    def publishUpdate(self, old):
        from src.domain_model.user.UserUpdated import UserUpdated
        DomainPublishedEvents.addEventForPublishing(UserUpdated(old, self))

    def toMap(self) -> dict:
        return {"id": self.id(), "name": self.name(),
                "first_name": self.firstName(), "last_name": self.lastName(), "address_one": self.addressOne(),
                "address_two": self.addressTwo(), "postal_code": self.postalCode(), "avatar_image": self.avatarImage()}

    def __eq__(self, other):
        if not isinstance(other, User):
            raise NotImplementedError(f'other: {other} can not be compared with User class')
        return self.id() == other.id() and self.name() == other.name() and self.firstName() == other.firstName() and \
               self.lastName() == other.lastName() and self.addressOne() == other.addressOne() and self.addressTwo() == other.addressTwo() and \
               self.postalCode() == other.postalCode() and self.avatarImage() == other.avatarImage()
