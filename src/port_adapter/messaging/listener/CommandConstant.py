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

@extendEnum(CommonCommandConstant)
class ApiCommandConstant(Enum):
    pass


@extendEnum(CommonCommandConstant)
class IdentityCommandConstant(Enum):
    pass
