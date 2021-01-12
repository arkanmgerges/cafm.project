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


class CommonCommandConstant(Enum):
    CREATE_PROJECT = 'create_project'
    DELETE_PROJECT = 'delete_project'
    UPDATE_PROJECT = 'update_project'
    CREATE_USER = 'create_user'
    DELETE_USER = 'delete_user'
    UPDATE_USER = 'update_user'
    CREATE_ORGANIZATION = 'create_organization'
    DELETE_ORGANIZATION = 'delete_organization'
    UPDATE_ORGANIZATION = 'update_organization'

@extendEnum(CommonCommandConstant)
class ApiCommandConstant(Enum):
    pass


@extendEnum(CommonCommandConstant)
class IdentityCommandConstant(Enum):
    pass
