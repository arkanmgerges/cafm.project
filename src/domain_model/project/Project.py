"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
@collaborator: Mohammad S. moso<moso@develoop.run>
"""
from src.domain_model.common.HasToMap import HasToMap
from src.domain_model.event.DomainPublishedEvents import DomainPublishedEvents
from src.domain_model.project.ProjectState import ProjectState
from src.domain_model.project.ProjectStateChanged import ProjectStateChanged
from src.domain_model.resource.exception.ProjectStateException import (
    ProjectStateException,
)
from src.resource.logging.logger import logger
from uuid import uuid4


class Project(HasToMap):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        cityId: int = None,
        countryId: int = None,
        addressLine: str = None,
        addressLineTwo: str = None,
        beneficiaryId: str = None,
        postalCode: str = None,
        countryStateName: str = None,
        countryStateIsoCode: str = None,
        state: ProjectState = ProjectState.DRAFT,
        startDate: int = None,
        skipValidation: bool = False,
        developerName: str = None,
        developerCityId: int = None,
        developerCountryId: int = None,
        developerAddressLineOne: str = None,
        developerAddressLineTwo: str = None,
        developerContact: str = None,
        developerEmail: str = None,
        developerPhoneNumber: str = None,
        developerWarranty: str = None,
        developerPostalCode: str = None,
        developerCountryStateName: str = None,
        developerCountryStateIsoCode: str = None,
        modifiedAt: int = None,
        createdAt: int = None,
    ):
        self._id = str(uuid4()) if id is None else id
        self._name = name
        self._cityId = cityId if cityId is not None and cityId > 0 else None
        self._countryId = countryId if countryId is not None and countryId > 0 else None
        self._startDate = startDate
        self._addressLine = addressLine
        self._addressLineTwo = addressLineTwo
        self._beneficiaryId = beneficiaryId
        self._postalCode = postalCode
        self._countryStateName = countryStateName
        self._countryStateIsoCode = countryStateIsoCode
        self._state: ProjectState = (
            state if isinstance(state, ProjectState) else ProjectState.DRAFT
        )
        self._developerName = developerName
        self._developerCityId = developerCityId if developerCityId is not None and developerCityId > 0 else None
        self._developerCountryId = developerCountryId if developerCountryId is not None and developerCountryId > 0 else None
        self._developerAddressLineOne = developerAddressLineOne
        self._developerAddressLineTwo = developerAddressLineTwo
        self._developerContact = developerContact
        self._developerEmail = developerEmail
        self._developerPhoneNumber = developerPhoneNumber
        self._developerWarranty = developerWarranty
        self._developerPostalCode = developerPostalCode
        self._developerCountryStateName = developerCountryStateName
        self._developerCountryStateIsoCode = developerCountryStateIsoCode
        self._modifiedAt = modifiedAt
        self._createdAt = createdAt

    @classmethod
    def createFrom(
        cls,
        id: str = None,
        name: str = None,
        cityId: int = None,
        countryId: int = None,
        addressLine: str = None,
        addressLineTwo: str = None,
        beneficiaryId: str = None,
        postalCode: str = None,
        countryStateName: str = None,
        countryStateIsoCode: str = None,
        state: ProjectState = ProjectState.DRAFT,
        startDate: int = None,
        publishEvent: bool = False,
        skipValidation: bool = False,
        developerName: str = None,
        developerCityId: int = None,
        developerCountryId: int = None,
        developerAddressLineOne: str = None,
        developerAddressLineTwo: str = None,
        developerContact: str = None,
        developerEmail: str = None,
        developerPhoneNumber: str = None,
        developerWarranty: str = None,
        developerPostalCode: str = None,
        developerCountryStateName: str = None,
        developerCountryStateIsoCode: str = None,
        modifiedAt: int = None,
        createdAt: int = None,
        **_kwargs,
    ):

        obj = Project(
            id=id,
            name=name,
            cityId=cityId,
            countryId=countryId,
            addressLine=addressLine,
            addressLineTwo=addressLineTwo,
            beneficiaryId=beneficiaryId,
            postalCode=postalCode,
            countryStateName=countryStateName,
            countryStateIsoCode=countryStateIsoCode,
            state=state,
            startDate=startDate,
            skipValidation=skipValidation,
            developerName=developerName,
            developerCityId=developerCityId,
            developerCountryId=developerCountryId,
            developerAddressLineOne=developerAddressLineOne,
            developerAddressLineTwo=developerAddressLineTwo,
            developerContact=developerContact,
            developerEmail=developerEmail,
            developerPhoneNumber=developerPhoneNumber,
            developerWarranty=developerWarranty,
            developerPostalCode=developerPostalCode,
            developerCountryStateName=developerCountryStateName,
            developerCountryStateIsoCode=developerCountryStateIsoCode,
            modifiedAt=modifiedAt,
            createdAt=createdAt,
        )
        if publishEvent:
            from src.domain_model.event.DomainPublishedEvents import (
                DomainPublishedEvents,
            )
            from src.domain_model.project.ProjectCreated import ProjectCreated

            logger.debug(
                f"[{Project.createFrom.__qualname__}] - Create Project with name: {name}, id: {id}, cityId: {cityId}, \
                countryId: {countryId}, addressLine: {addressLine}, addressLineTwo: {addressLineTwo}, \
                beneficiaryId: {beneficiaryId}, state: {state}, startDate: {startDate}"
            )
            DomainPublishedEvents.addEventForPublishing(ProjectCreated(obj))
        return obj

    @classmethod
    def createFromObject(
        cls,
        obj: "Project",
        publishEvent: bool = False,
        generateNewId: bool = False,
        skipValidation: bool = False,
    ):
        logger.debug(f"[{Project.createFromObject.__qualname__}]")
        id = None if generateNewId else obj.id()
        return cls.createFrom(
            id=id,
            name=obj.name(),
            cityId=obj.cityId(),
            countryId=obj.countryId(),
            addressLine=obj.addressLine(),
            addressLineTwo=obj.addressLineTwo(),
            beneficiaryId=obj.beneficiaryId(),
            postalCode=obj.postalCode(),
            countryStateName=obj.countryStateName(),
            countryStateIsoCode=obj.countryStateIsoCode(),
            startDate=obj.startDate(),
            state=obj.state(),
            createdAt=obj.createdAt(),
            modifiedAt=obj.modifiedAt(),
            publishEvent=publishEvent,
            skipValidation=skipValidation,
        )

    def changeState(self, state: ProjectState):
        if self.state() is not ProjectState.DRAFT and state is ProjectState.DRAFT:
            raise ProjectStateException(
                f"Can not change state from {self.state().value} to {state.value}"
            )
        if self.state() == state:
            raise ProjectStateException(
                f"Could not update the state, the old and new states are identical. state: {state.value}"
            )
        self._state = state
        if state is ProjectState.ACTIVE:
            from src.resource.common.DateTimeHelper import DateTimeHelper

            self._startDate = DateTimeHelper.utcNowInSecond()
        DomainPublishedEvents.addEventForPublishing(
            ProjectStateChanged(
                oldState=self.state(), newState=state, startDate=self.startDate()
            )
        )

    def id(self) -> str:
        return self._id

    def name(self) -> str:
        return self._name

    def cityId(self) -> int:
        return self._cityId

    def countryId(self) -> int:
        return self._countryId

    def addressLine(self) -> str:
        return self._addressLine

    def addressLineTwo(self) -> str:
        return self._addressLineTwo

    def beneficiaryId(self) -> str:
        return self._beneficiaryId

    def postalCode(self) -> str:
        return self._postalCode

    def countryStateName(self) -> str:
        return self._countryStateName

    def countryStateIsoCode(self) -> str:
        return self._countryStateIsoCode

    def state(self) -> ProjectState:
        return self._state

    def startDate(self) -> int:
        return self._startDate

    def developerName(self) -> str:
        return self._developerName

    def developerCityId(self) -> int:
        return self._developerCityId

    def developerCountryId(self) -> int:
        return self._developerCountryId

    def developerAddressLineOne(self) -> str:
        return self._developerAddressLineOne

    def developerAddressLineTwo(self) -> str:
        return self._developerAddressLineTwo

    def developerContact(self) -> str:
        return self._developerContact

    def developerEmail(self) -> str:
        return self._developerEmail

    def developerPhoneNumber(self) -> str:
        return self._developerPhoneNumber

    def developerWarranty(self) -> str:
        return self._developerWarranty

    def developerPostalCode(self) -> str:
        return self._developerPostalCode

    def developerCountryStateName(self) -> str:
        return self._developerCountryStateName

    def developerCountryStateIsoCode(self) -> str:
        return self._developerCountryStateIsoCode

    def modifiedAt(self) -> int:
        return self._modifiedAt

    def createdAt(self) -> int:
        return self._createdAt

    @staticmethod
    def stateStringToProjectState(state: str = "") -> ProjectState:
        if state == ProjectState.DRAFT.value:
            return ProjectState.DRAFT
        if state == ProjectState.ACTIVE.value:
            return ProjectState.ACTIVE
        if state == ProjectState.ARCHIVED.value:
            return ProjectState.ARCHIVED
        # Else
        return ProjectState.DRAFT

    def update(self, data: dict):
        from copy import copy

        updated = False
        old = copy(self)
        if "name" in data and data["name"] != self._name:
            updated = True
            self._name = data["name"]
        if "city_id" in data and data["city_id"] != self._cityId:
            updated = True
            self._cityId = data["city_id"]
        if "country_id" in data and data["country_id"] != self._countryId:
            updated = True
            self._countryId = data["country_id"]
        if "beneficiary_id" in data and data["beneficiary_id"] != self._beneficiaryId:
            updated = True
            self._beneficiaryId = data["beneficiary_id"]
        if "postal_code" in data and data["postal_code"] != self._postalCode:
            updated = True
            self._postalCode = data["postal_code"]
        if "country_state_name" in data and data["country_state_name"] != self._countryStateName:
            updated = True
            self._countryStateName = data["country_state_name"]
        if "country_state_iso_code" in data and data["country_state_iso_code"] != self._countryStateIsoCode:
            updated = True
            self._countryStateIsoCode = data["country_state_iso_code"]

        if "developer_country_state_name" in data and data["developer_country_state_name"] != self._developerCountryStateName:
            updated = True
            self._developerCountryStateName = data["developer_country_state_name"]
        if "developer_country_state_iso_code" in data and data["developer_country_state_iso_code"] != self._developerCountryStateIsoCode:
            updated = True
            self._developerCountryStateIsoCode = data["developer_country_state_iso_code"]

        if "address_line" in data and data["address_line"] != self._addressLine:
            updated = True
            self._addressLine = data["address_line"]
        if "start_date" in data and data["start_date"] != self._startDate:
            updated = True
            self._startDate = data["start_date"]
        if updated:
            self.publishUpdate(old)

    def publishDelete(self):
        if self.state() != ProjectState.DRAFT:
            from src.domain_model.resource.exception.NotAllowedActionException import NotAllowedActionException
            raise NotAllowedActionException(
                f'Can not delete the project, current project state is {self.state().value}')

        from src.domain_model.project.ProjectDeleted import ProjectDeleted

        DomainPublishedEvents.addEventForPublishing(ProjectDeleted(self))

    def publishUpdate(self, old):
        if old.state() != self.state() and self.state() == ProjectState.DRAFT:
            from src.domain_model.resource.exception.NotAllowedActionException import NotAllowedActionException
            raise NotAllowedActionException(
                f'Can not update the project, current project state is {self.state().value}')

        from src.domain_model.project.ProjectUpdated import ProjectUpdated

        DomainPublishedEvents.addEventForPublishing(ProjectUpdated(old, self))

    def toMap(self) -> dict:
        return {
            "project_id": self.id(),
            "name": self.name(),
            "city_id": self.cityId(),
            "country_id": self.countryId(),
            "address_line": self.addressLine(),
            "address_line_two": self.addressLineTwo(),
            "start_date": self.startDate(),
            "beneficiary_id": self.beneficiaryId(),
            "postal_code": self.postalCode(),
            "country_state_name": self.countryStateName(),
            "country_state_iso_code": self.countryStateIsoCode(),
            "state": self.state().value,
            "developer_name": self.developerName(),
            "developer_city_id": self.developerCityId(),
            "developer_country_id": self.developerCountryId(),
            "developer_address_line_one": self.developerAddressLineOne(),
            "developer_address_line_two": self.developerAddressLineTwo(),
            "developer_contact": self.developerContact(),
            "developer_email": self.developerEmail(),
            "developer_phone_number": self.developerPhoneNumber(),
            "developer_warranty": self.developerWarranty(),
            "developer_postal_code": self.developerPostalCode(),
            "developer_country_state_name": self.developerCountryStateName(),
            "developer_country_state_iso_code": self.developerCountryStateIsoCode(),
            "modified_at": self.modifiedAt(),
            "created_at": self.createdAt(),
        }

    def __repr__(self):
        return f"<{self.__module__} object at {hex(id(self))}> {self.toMap()}"

    def __str__(self) -> str:
        return f"<{self.__module__} object at {hex(id(self))}> {self.toMap()}"

    def __eq__(self, other):
        if not isinstance(other, Project):
            raise NotImplementedError(
                f"other: {other} can not be compared with Project class"
            )
        return (
            self.id() == other.id()
            and self.name() == other.name()
            and self.cityId() == other.cityId()
            and self.countryId() == other.countryId()
            and self.beneficiaryId() == other.beneficiaryId()
            and self.postalCode() == other.postalCode()
            and self.countryStateName() == other.countryStateName()
            and self.countryStateIsoCode() == other.countryStateIsoCode()
            and self.addressLine() == other.addressLine()
            and self.addressLineTwo() == other.addressLineTwo()
            and self.state() == other.state()
            and self.startDate() == other.startDate()
            and self.developerName() == other.developerName()
            and self.developerCityId() == other.developerCityId()
            and self.developerCountryId() == other.developerCountryId()
            and self.developerAddressLineOne() == other.developerAddressLineOne()
            and self.developerAddressLineTwo() == other.developerAddressLineTwo()
            and self.developerContact() == other.developerContact()
            and self.developerEmail() == other.developerEmail()
            and self.developerPhoneNumber() == other.developerPhoneNumber()
            and self.developerWarranty() == other.developerWarranty()
            and self.developerPostalCode() == other.developerPostalCode()
            and self.developerCountryStateName() == other.developerCountryStateName()
            and self.developerCountryStateIsoCode() == other.developerCountryStateIsoCode()
        )
