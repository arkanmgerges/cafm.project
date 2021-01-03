"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from copy import copy
from uuid import uuid4

from src.domain_model.event.DomainPublishedEvents import DomainPublishedEvents
from src.resource.logging.logger import logger


class User:
    def __init__(self, id: str = None, email: str = '', firstName: str = '', lastName: str = '',
                 addressOne: str = '', addressTwo: str = '', postalCode: str = '', avatarImage: str = ''):
        anId = str(uuid4()) if id is None or id == '' else id
        self._id = anId
        self._email = email
        self._firstName = firstName
        self._lastName = lastName
        self._addressOne = addressOne
        self._addressTwo = addressTwo
        self._postalCode = postalCode
        self._avatarImage = avatarImage

    @classmethod
    def createFrom(cls, id: str = None, email: str = '', firstName: str = '', lastName: str = '',
                   addressOne: str = '', addressTwo: str = '', postalCode: str = '', avatarImage: str = '',
                   publishEvent: bool = False):
        user: User = User(id=id, email=email, firstName=firstName, lastName=lastName,
                          addressOne=addressOne, addressTwo=addressTwo, postalCode=postalCode, avatarImage=avatarImage)
        logger.debug(f'[{User.createFrom.__qualname__}] - data: {user.toMap()}')
        if publishEvent:
            logger.debug(f'[{User.createFrom.__qualname__}] - publish UserCreated event')
            from src.domain_model.event.DomainPublishedEvents import DomainPublishedEvents
            from src.domain_model.user.UserCreated import UserCreated
            DomainPublishedEvents.addEventForPublishing(UserCreated(user))
        return user

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

    def avatarImage(self) -> str:
        return self._avatarImage

    def update(self, data: dict):
        updated = False
        old = copy(self)
        if 'email' in data and data['email'] != self._email and data['email'] is not None:
            updated = True
            self._email = data['email']
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

    def publishDelete(self):
        from src.domain_model.user.UserDeleted import UserDeleted
        DomainPublishedEvents.addEventForPublishing(UserDeleted(self))

    def publishUpdate(self, old):
        from src.domain_model.user.UserUpdated import UserUpdated
        DomainPublishedEvents.addEventForPublishing(UserUpdated(old, self))

    def toMap(self) -> dict:
        return {"id": self.id(), "email": self.email(),
                "first_name": self.firstName(), "last_name": self.lastName(), "address_one": self.addressOne(),
                "address_two": self.addressTwo(), "postal_code": self.postalCode(), "avatar_image": self.avatarImage()}

    def __repr__(self):
        return f'<{self.__module__} object at {hex(id(self))}> {self.toMap()}'

    def __str__(self) -> str:
        return f'<{self.__module__} object at {hex(id(self))}> {self.toMap()}'

    def __eq__(self, other) -> bool:
        if not isinstance(other, User):
            raise NotImplementedError(f'other: {other} can not be compared with User class')
        return self.id() == other.id() and self.email() == other.email() and self.firstName() == other.firstName() and \
               self.lastName() == other.lastName() and self.addressOne() == other.addressOne() and \
               self.addressTwo() == other.addressTwo() and self.postalCode() == other.postalCode() and \
               self.avatarImage() == other.avatarImage()
