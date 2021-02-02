"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from enum import Enum


def extendEnum(inheritedEnum):
    def wrapper(addedEnum):
        joined = {}
        for item in inheritedEnum:
            joined[item.name] = item.value
        for item in addedEnum:
            joined[item.name] = item.value
        return Enum(addedEnum.__name__, joined)

    return wrapper


class CommonEventConstant(Enum):
    OU_CREATED = 'ou_created'
    OU_DELETED = 'ou_deleted'
    OU_UPDATED = 'ou_updated'
    PERMISSION_CREATED = 'permission_created'
    PERMISSION_DELETED = 'permission_deleted'
    PERMISSION_UPDATED = 'permission_updated'
    PERMISSION_CONTEXT_CREATED = 'permission_context_created'
    PERMISSION_CONTEXT_DELETED = 'permission_context_deleted'
    PERMISSION_CONTEXT_UPDATED = 'permission_context_updated'
    PROJECT_CREATED = 'project_created'
    PROJECT_DELETED = 'project_deleted'
    PROJECT_UPDATED = 'project_updated'
    PROJECT_STATE_CHANGED = 'project_state_changed'
    REALM_CREATED = 'realm_created'
    REALM_DELETED = 'realm_deleted'
    REALM_UPDATED = 'realm_updated'
    ROLE_CREATED = 'role_created'
    ROLE_DELETED = 'role_deleted'
    ROLE_UPDATED = 'role_updated'
    USER_CREATED = 'user_created'
    USER_DELETED = 'user_deleted'
    USER_UPDATED = 'user_updated'
    ORGANIZATION_CREATED = 'organization_created'
    ORGANIZATION_DELETED = 'organization_deleted'
    ORGANIZATION_UPDATED = 'organization_updated'
    USER_GROUP_CREATED = 'user_group_created'
    USER_GROUP_DELETED = 'user_group_deleted'
    USER_GROUP_UPDATED = 'user_group_updated'
    ROLE_TO_USER_ASSIGNED = 'role_to_user_assigned'
    ROLE_TO_USER_ASSIGNMENT_REVOKED = 'role_to_user_assignment_revoked'
    USER_TO_REALM_ASSIGNED = 'user_to_realm_assigned'
    USER_TO_REALM_ASSIGNMENT_REVOKED = 'user_to_realm_assignment_revoked'
    USER_TO_ORGANIZATION_ASSIGNED = 'user_to_organization_assigned'
    USER_TO_ORGANIZATION_ASSIGNMENT_REVOKED = 'user_to_organization_assignment_revoked'
