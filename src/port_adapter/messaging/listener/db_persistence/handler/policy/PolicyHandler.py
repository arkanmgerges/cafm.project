"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import json
from typing import Callable, List

from src.domain_model.event.EventConstant import CommonEventConstant
from src.domain_model.organization.OrganizationRepository import OrganizationRepository
from src.domain_model.policy.PolicyRepository import PolicyRepository
from src.domain_model.role.RoleRepository import RoleRepository
from src.domain_model.user.UserRepository import UserRepository
from src.port_adapter.messaging.listener.common.handler.Handler import Handler
from src.resource.logging.logger import logger


class PolicyHandler(Handler):
    def __init__(self):
        # Events to handle
        self._eventConstants = [
            CommonEventConstant.ROLE_TO_USER_ASSIGNED.value,
            CommonEventConstant.ROLE_TO_USER_ASSIGNMENT_REVOKED.value,
            CommonEventConstant.USER_TO_ORGANIZATION_ASSIGNED.value,
            CommonEventConstant.USER_TO_ORGANIZATION_ASSIGNMENT_REVOKED.value,
        ]

        # Repos
        import src.port_adapter.AppDi as AppDi
        self._roleRepository: RoleRepository = AppDi.instance.get(RoleRepository)
        self._organizationRepository: OrganizationRepository = AppDi.instance.get(OrganizationRepository)
        self._userRepository: UserRepository = AppDi.instance.get(UserRepository)
        self._repository: PolicyRepository = AppDi.instance.get(PolicyRepository)

    def canHandle(self, name: str) -> bool:
        return name in self._eventConstants

    def handleCommand(self, messageData: dict):
        name = messageData['name']
        data = messageData['data']
        metadata = messageData['metadata']

        logger.debug(
            f'[{PolicyHandler.handleCommand.__qualname__}] - received args:\ntype(name): {type(name)}, name: {name}\ntype(data): {type(data)}, data: {data}\ntype(metadata): {type(metadata)}, metadata: {metadata}')
        dataDict = json.loads(data)
        # metadataDict = json.loads(metadata)
        #
        # if 'token' not in metadataDict:
        #     raise UnAuthorizedException()

        result = self.execute(name, **dataDict)
        return {'data': result, 'metadata': metadata}

    def execute(self, event, *args, **kwargs):
        funcSwitcher = {
            CommonEventConstant.ROLE_TO_USER_ASSIGNED.value: self._assignRoleToUser,
            CommonEventConstant.ROLE_TO_USER_ASSIGNMENT_REVOKED.value: self._revokeRoleToUserAssignment,
            CommonEventConstant.USER_TO_ORGANIZATION_ASSIGNED.value: self._assignUserToOrganization,
            CommonEventConstant.USER_TO_ORGANIZATION_ASSIGNMENT_REVOKED.value: self._revokeUserToOrganizationAssignment,
        }

        argSwitcher = {
            CommonEventConstant.ROLE_TO_USER_ASSIGNED.value: lambda: kwargs,
            CommonEventConstant.ROLE_TO_USER_ASSIGNMENT_REVOKED.value: lambda: kwargs,
            CommonEventConstant.USER_TO_ORGANIZATION_ASSIGNED.value: lambda: kwargs,
            CommonEventConstant.USER_TO_ORGANIZATION_ASSIGNMENT_REVOKED.value: lambda: kwargs,
        }
        func = funcSwitcher.get(event, None)
        if func is not None:
            # Execute the function with the arguments
            return func(*args, **(argSwitcher.get(event))())
        return None

    def _assignRoleToUser(self, *_args, **kwargs):
        role = self._roleRepository.roleById(id=kwargs['role_id'])
        user = self._userRepository.userById(id=kwargs['user_id'])
        self._repository.assignRoleToUser(role=role, user=user)
        return {'role_id': role.id(), 'user_id': user.id()}

    def _revokeRoleToUserAssignment(self, *_args, **kwargs):
        role = self._roleRepository.roleById(id=kwargs['role_id'])
        user = self._userRepository.userById(id=kwargs['user_id'])
        self._repository.assignRoleToUser(role=role, user=user)
        return {'role_id': role.id(), 'user_id': user.id()}

    def _assignUserToOrganization(self, *_args, **kwargs):
        organization = self._organizationRepository.organizationById(id=kwargs['organization_id'])
        user = self._userRepository.userById(id=kwargs['user_id'])
        self._repository.assignUserToOrganization(user=user, organization=organization)
        return {'organization_id': organization.id(), 'user_id': user.id()}

    def _revokeUserToOrganizationAssignment(self, *_args, **kwargs):
        organization = self._organizationRepository.organizationById(id=kwargs['organization_id'])
        user = self._userRepository.userById(id=kwargs['user_id'])
        self._repository.revokeUserToOrganizationAssignment(user=user, organization=organization)
        return {'organization_id': organization.id(), 'user_id': user.id()}

    @staticmethod
    def targetsOnSuccess() -> List[Callable]:
        return [Handler.targetOnSuccess]