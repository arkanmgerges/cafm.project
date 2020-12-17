"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from src.domain_model.event.DomainPublishedEvents import DomainPublishedEvents
from src.domain_model.project.ProjectState import ProjectState
from src.domain_model.project.ProjectStateChanged import ProjectStateChanged
from src.domain_model.resource.exception.ProjectStateException import ProjectStateException

"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from uuid import uuid4


class Project:
    def __init__(self, id: str = None, name: str = '', cityId: int = 0, countryId: int = 0, addressLine: str = '',
                 beneficiaryId: str = '', state: ProjectState = ProjectState.DRAFT):
        self._id = str(uuid4()) if id is None or id == '' else id
        self._name = name
        self._cityId = cityId
        self._countryId = countryId
        self._addressLine = addressLine if addressLine is not None else ''
        self._beneficiaryId = beneficiaryId if addressLine is not None else ''
        self._state: ProjectState = state

    @classmethod
    def createFrom(cls, id: str = None, name: str = '', cityId: int = 0, countryId: int = 0, addressLine: str = '',
                   beneficiaryId: str = '', state: ProjectState = ProjectState.DRAFT, publishEvent: bool = False):
        from src.domain_model.project.ProjectCreated import ProjectCreated
        from src.resource.logging.logger import logger
        project = Project(id, name, cityId, countryId, addressLine, beneficiaryId, state)
        if publishEvent:
            from src.domain_model.event.DomainPublishedEvents import DomainPublishedEvents
            logger.debug(
                f'[{Project.createFrom.__qualname__}] - Create Project with name: {name}, id: {id}, cityId: {cityId}, \
                countryId: {countryId}, addressLine: {addressLine}, beneficiaryId: {beneficiaryId}, state: {state}')
            DomainPublishedEvents.addEventForPublishing(ProjectCreated(project))
        return project

    def changeState(self, state: ProjectState):
        if self.state() is not ProjectState.DRAFT and state is ProjectState.DRAFT:
            raise ProjectStateException(f'Can not change state from {self.state().value} to {state.value}')
        if self.state() == state:
            raise ProjectStateException(
                f'Could not update the state, the old and new states are identical. state: {state.value}')
        self._state = state
        DomainPublishedEvents.addEventForPublishing(ProjectStateChanged(oldState=self.state(), newState=state))

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
        if 'cityId' in data and data['cityId'] != self._cityId:
            updated = True
            self._cityId = data['cityId']
        if 'countryId' in data and data['countryId'] != self._countryId:
            updated = True
            self._countryId = data['countryId']
        if 'beneficiaryId' in data and data['beneficiaryId'] != self._beneficiaryId:
            updated = True
            self._beneficiaryId = data['beneficiaryId']
        if 'addressLine' in data and data['addressLine'] != self._addressLine:
            updated = True
            self._addressLine = data['addressLine']
        if updated:
            self.publishUpdate(old)

    def publishDelete(self):
        from src.domain_model.project.ProjectDeleted import ProjectDeleted
        DomainPublishedEvents.addEventForPublishing(ProjectDeleted(self))

    def publishUpdate(self, old):
        from src.domain_model.project.ProjectUpdated import ProjectUpdated
        DomainPublishedEvents.addEventForPublishing(ProjectUpdated(old, self))

    def toMap(self) -> dict:
        return {"id": self.id(), "name": self.name(), "city_id": self.cityId(), "country_id": self.countryId(),
                "address_line": self.addressLine(),
                "beneficiary_id": self.beneficiaryId(), "state": self.state().value}

    def __eq__(self, other):
        if not isinstance(other, Project):
            raise NotImplementedError(f'other: {other} can not be compared with Project class')
        return self.id() == other.id() and self.name() == other.name() and self.cityId() == other.cityId() and \
               self.countryId() == other.countryId() and self.beneficiaryId() == other.beneficiaryId() and \
               self.addressLine() == other.addressLine() and self.state() == other.state()
