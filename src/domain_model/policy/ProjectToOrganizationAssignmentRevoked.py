from uuid import uuid4

from src.domain_model.event.DomainEvent import DomainEvent
from src.domain_model.event.EventConstant import CommonEventConstant
from src.domain_model.organization.Organization import Organization
from src.domain_model.project.Project import Project


class ProjectToOrganizationAssignmentRevoked(DomainEvent):
    def __init__(self, organization: Organization, project: Project):
        super().__init__(
            id=str(uuid4()),
            name=CommonEventConstant.PROJECT_TO_ORGANIZATION_ASSIGNMENT_REVOKED.value,
        )
        self._data = {"project_id": project.id(), "organization_id": organization.id()}
