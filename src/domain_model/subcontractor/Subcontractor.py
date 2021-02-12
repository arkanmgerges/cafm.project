"""
@author: Mohammad S. moso<moso@develoop.run>
"""
from uuid import uuid4

from src.resource.logging.logger import logger


class Subcontractor:
    def __init__(self, id: str = None, companyName: str = '', websiteUrl: str = '', contactPerson: str = '',
                 email: str = '', phoneNumber: str = '', addressOne: str = '', addressTwo: str = ''):
        anId = str(uuid4()) if id is None else id
        self._id = anId
        self._companyName = companyName
        self._websiteUrl = websiteUrl
        self._contactPerson = contactPerson
        self._email = email
        self._phoneNumber = phoneNumber
        self._addressOne = addressOne
        self._addressTwo = addressTwo

    @classmethod
    def createFrom(cls, id: str = None, companyName: str = '', websiteUrl: str = '', contactPerson: str = '',
                   email: str = '', phoneNumber: str = '', addressOne: str = '', addressTwo: str = '',
                   publishEvent: bool = False):

        subcontractor: Subcontractor = Subcontractor(id=id,
                                                     companyName=companyName,
                                                     websiteUrl=websiteUrl,
                                                     contactPerson=contactPerson,
                                                     email=email,
                                                     phoneNumber=phoneNumber,
                                                     addressOne=addressOne,
                                                     addressTwo=addressTwo)
        logger.debug(f'[{Subcontractor.createFrom.__qualname__}] - data: {subcontractor.toMap()} event: {publishEvent}')
        if publishEvent:
            logger.debug(f'[{Subcontractor.createFrom.__qualname__}] - publish OrganizationCreated event')
            from src.domain_model.event.DomainPublishedEvents import DomainPublishedEvents
            from src.domain_model.subcontractor.SubcontractorCreated import SubcontractorCreated
            DomainPublishedEvents.addEventForPublishing(SubcontractorCreated(subcontractor))
        return subcontractor

    @classmethod
    def createFromObject(cls, obj: 'Subcontractor', publishEvent: bool = False, generateNewId: bool = False):
        logger.debug(f'[{Subcontractor.createFromObject.__qualname__}]')
        id = None if generateNewId else obj.id()
        return cls.createFrom(id=id,
                              companyName=obj.companyName(),
                              websiteUrl=obj.websiteUrl(),
                              contactPerson=obj.contactPerson(),
                              email=obj.email(),
                              phoneNumber=obj.phoneNumber(),
                              addressOne=obj.addressOne(),
                              addressTwo=obj.addressTwo(),
                              publishEvent=publishEvent)

    def id(self) -> str:
        return self._id

    def companyName(self) -> str:
        return self._companyName

    def websiteUrl(self) -> str:
        return self._websiteUrl

    def contactPerson(self) -> str:
        return self._contactPerson

    def email(self) -> str:
        return self._email

    def phoneNumber(self) -> str:
        return self._phoneNumber

    def addressOne(self) -> str:
        return self._addressOne

    def addressTwo(self) -> str:
        return self._addressTwo

    def toMap(self) -> dict:
        return {"id": self.id(),
                "company_name": self.companyName(),
                "website_url": self.websiteUrl(),
                "contact_person": self.contactPerson(),
                "email": self.email(),
                "phone_number": self.phoneNumber(),
                "address_one": self.addressOne(),
                "address_two": self.addressTwo()}

    def __repr__(self):
        return f'<{self.__module__} object at {hex(id(self))}> {self.toMap()}'

    def __str__(self) -> str:
        return f'<{self.__module__} object at {hex(id(self))}> {self.toMap()}'

    def __eq__(self, other) -> bool:
        if not isinstance(other, Subcontractor):
            raise NotImplementedError(f'other: {other} can not be compared with User class')
        return self.id() == other.id() and self.companyName() == other.companyName() and self.websiteUrl() == other.websiteUrl() and \
               self.contactPerson() == other.contactPerson() and self.email() == other.email() and self.phoneNumber() == other.phoneNumber() and \
               self.addressOne() == other.addressOne() and self.addressTwo() == other.addressTwo()
