"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
@collaborator: Mohammad S. moso<moso@develoop.run>
"""
from src.domain_model.event.DomainPublishedEvents import DomainPublishedEvents
from src.domain_model.project.ProjectState import ProjectState
from src.domain_model.project.ProjectStateChanged import ProjectStateChanged
from src.domain_model.resource.exception.ProjectStateException import ProjectStateException
from src.resource.logging.logger import logger
from uuid import uuid4


class Project:
    def __init__(self,
                 id: str = None,
                 name: str = None,
                 cityId: int = 0,
                 countryId: int = 0,
                 addressLine: str = None,
                 beneficiaryId: str = None,
                 state: ProjectState = ProjectState.DRAFT,
                 startDate: int = None,
                 skipValidation: bool = False):
        self._id = str(uuid4()) if id is None else id
        self._name = name
        self._cityId = cityId
        self._countryId = countryId
        self._startDate = startDate
        self._addressLine = addressLine if addressLine is not None else ''
        self._beneficiaryId = beneficiaryId if addressLine is not None else ''
        if type(state) is str:
            state = self.stateStringToProjectState(state=state)
        self._state: ProjectState = state if isinstance(state, ProjectState) else ProjectState.DRAFT

    @classmethod
    def createFrom(cls, id: str = None, name: str = None, cityId: int = 0, countryId: int = 0, addressLine: str = None,
                   beneficiaryId: str = None, state: ProjectState = ProjectState.DRAFT, startDate: int = None,
                   publishEvent: bool = False, skipValidation: bool = False):
        from src.domain_model.project.ProjectCreated import ProjectCreated
        obj = Project(id, name, cityId, countryId, addressLine, beneficiaryId, state, startDate, skipValidation=skipValidation)
        if publishEvent:
            from src.domain_model.event.DomainPublishedEvents import DomainPublishedEvents
            logger.debug(
                f'[{Project.createFrom.__qualname__}] - Create Project with name: {name}, id: {id}, cityId: {cityId}, \
                countryId: {countryId}, addressLine: {addressLine}, beneficiaryId: {beneficiaryId}, state: {state}, startDate: {startDate}')
            DomainPublishedEvents.addEventForPublishing(ProjectCreated(obj))
        return obj

    @classmethod
    def createFromObject(cls, obj: 'Project', publishEvent: bool = False, generateNewId: bool = False, skipValidation: bool = False):
        logger.debug(f'[{Project.createFromObject.__qualname__}]')
        id = None if generateNewId else obj.id()
        return cls.createFrom(id=id, name=obj.name(), cityId=obj.cityId(),
                              countryId=obj.countryId(), addressLine=obj.addressLine(),
                              beneficiaryId=obj.beneficiaryId(),
                              startDate=obj.startDate(),
                              state=obj.state(), publishEvent=publishEvent, skipValidation=skipValidation)

    def changeState(self, state: ProjectState):
        if self.state() is not ProjectState.DRAFT and state is ProjectState.DRAFT:
            raise ProjectStateException(f'Can not change state from {self.state().value} to {state.value}')
        if self.state() == state:
            raise ProjectStateException(
                f'Could not update the state, the old and new states are identical. state: {state.value}')
        self._state = state
        if state is ProjectState.ACTIVE:
            from src.resource.common.DateTimeHelper import DateTimeHelper
            self._startDate = DateTimeHelper.utcNowInSecond()
        DomainPublishedEvents.addEventForPublishing(
            ProjectStateChanged(oldState=self.state(), newState=state, startDate=self.startDate()))

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

    def beneficiaryId(self) -> str:
        return self._beneficiaryId

    def state(self) -> ProjectState:
        return self._state

    def startDate(self) -> int:
        return self._startDate

    @staticmethod
    def stateStringToProjectState(state: str = '') -> ProjectState:
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
        if 'name' in data and data['name'] != self._name:
            updated = True
            self._name = data['name']
        if 'city_id' in data and data['city_id'] != self._cityId:
            updated = True
            self._cityId = data['city_id']
        if 'country_id' in data and data['country_id'] != self._countryId:
            updated = True
            self._countryId = data['country_id']
        if 'beneficiary_id' in data and data['beneficiary_id'] != self._beneficiaryId:
            updated = True
            self._beneficiaryId = data['beneficiary_id']
        if 'address_line' in data and data['address_line'] != self._addressLine:
            updated = True
            self._addressLine = data['address_line']
        if 'start_date' in data and data['start_date'] != self._startDate:
            updated = True
            self._startDate = data['start_date']
        if updated:
            self.publishUpdate(old)

    def publishDelete(self):
        from src.domain_model.project.ProjectDeleted import ProjectDeleted
        DomainPublishedEvents.addEventForPublishing(ProjectDeleted(self))

    def publishUpdate(self, old):
        from src.domain_model.project.ProjectUpdated import ProjectUpdated
        DomainPublishedEvents.addEventForPublishing(ProjectUpdated(old, self))

    def toMap(self) -> dict:
        return {"project_id": self.id(), "name": self.name(), "city_id": self.cityId(), "country_id": self.countryId(),
                "address_line": self.addressLine(),
                "start_date": self.startDate(),
                "beneficiary_id": self.beneficiaryId(), "state": self.state().value}

    def __repr__(self):
        return f'<{self.__module__} object at {hex(id(self))}> {self.toMap()}'

    def __str__(self) -> str:
        return f'<{self.__module__} object at {hex(id(self))}> {self.toMap()}'

    def __eq__(self, other):
        if not isinstance(other, Project):
            raise NotImplementedError(f'other: {other} can not be compared with Project class')
        return self.id() == other.id() and self.name() == other.name() and self.cityId() == other.cityId() and \
               self.countryId() == other.countryId() and self.beneficiaryId() == other.beneficiaryId() and \
               self.addressLine() == other.addressLine() and self.state() == other.state() and \
               self.startDate() == other.startDate()
