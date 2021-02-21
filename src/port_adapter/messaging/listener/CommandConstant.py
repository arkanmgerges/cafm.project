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
    CREATE_ROLE = 'create_role'
    DELETE_ROLE = 'delete_role'
    UPDATE_ROLE = 'update_role'
    CREATE_USER = 'create_user'
    DELETE_USER = 'delete_user'
    UPDATE_USER = 'update_user'
    CREATE_ORGANIZATION = 'create_organization'
    DELETE_ORGANIZATION = 'delete_organization'
    UPDATE_ORGANIZATION = 'update_organization'
    ASSIGN_USER_TO_ORGANIZATION = 'assign_user_to_organization'
    REVOKE_USER_TO_ORGANIZATION_ASSIGNMENT = 'revoke_user_to_organization_assignment'
    ASSIGN_ROLE_TO_USER = 'assign_role_to_user'
    REVOKE_ROLE_TO_USER_ASSIGNMENT = 'revoke_role_to_user_assignment'
    CREATE_BUILDING = 'create_building'
    DELETE_BUILDING = 'delete_building'
    UPDATE_BUILDING = 'update_building'
    CREATE_BUILDING_LEVEL = 'create_building_level'
    DELETE_BUILDING_LEVEL = 'delete_building_level'
    UPDATE_BUILDING_LEVEL = 'update_building_level'
    CREATE_BUILDING_LEVEL_ROOM = 'create_building_level_room'
    DELETE_BUILDING_LEVEL_ROOM = 'delete_building_level_room'
    UPDATE_BUILDING_LEVEL_ROOM = 'update_building_level_room'
    LINK_BUILDING_LEVEL_TO_BUILDING = 'link_building_level_to_building'
    UNLINK_BUILDING_LEVEL_FROM_BUILDING = 'unlink_building_level_from_building'
    UPDATE_BUILDING_LEVEL_ROOM_INDEX = 'update_building_level_room_index'
    CREATE_MANUFACTURER = 'create_manufacturer'
    UPDATE_MANUFACTURER = 'update_manufacturer'
    DELETE_MANUFACTURER = 'delete_manufacturer'
    CREATE_EQUIPMENT = 'create_equipment'
    UPDATE_EQUIPMENT = 'update_equipment'
    DELETE_EQUIPMENT = 'delete_equipment'
    CREATE_EQUIPMENT_PROJECT_CATEGORY = 'create_equipment_project_category'
    UPDATE_EQUIPMENT_PROJECT_CATEGORY = 'update_equipment_project_category'
    DELETE_EQUIPMENT_PROJECT_CATEGORY = 'delete_equipment_project_category'
    CREATE_EQUIPMENT_CATEGORY = 'create_equipment_category'
    UPDATE_EQUIPMENT_CATEGORY = 'update_equipment_category'
    DELETE_EQUIPMENT_CATEGORY = 'delete_equipment_category'
    CREATE_EQUIPMENT_CATEGORY_GROUP = 'create_equipment_category_group'
    UPDATE_EQUIPMENT_CATEGORY_GROUP = 'update_equipment_category_group'
    DELETE_EQUIPMENT_CATEGORY_GROUP = 'delete_equipment_category_group'
    CREATE_EQUIPMENT_MODEL = 'create_equipment_model'
    UPDATE_EQUIPMENT_MODEL = 'update_equipment_model'
    DELETE_EQUIPMENT_MODEL = 'delete_equipment_model'
    CREATE_SUBCONTRACTOR = 'create_subcontractor'
    UPDATE_SUBCONTRACTOR = 'update_subcontractor'
    DELETE_SUBCONTRACTOR = 'delete_subcontractor'

@extendEnum(CommonCommandConstant)
class ApiCommandConstant(Enum):
    pass


@extendEnum(CommonCommandConstant)
class IdentityCommandConstant(Enum):
    pass
