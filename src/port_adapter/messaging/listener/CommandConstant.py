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
    CREATE_PROJECT = "create_project"
    DELETE_PROJECT = "delete_project"
    UPDATE_PROJECT = "update_project"
    CREATE_ROLE = "create_role"
    DELETE_ROLE = "delete_role"
    UPDATE_ROLE = "update_role"
    CREATE_USER = "create_user"
    DELETE_USER = "delete_user"
    UPDATE_USER = "update_user"
    CREATE_ORGANIZATION = "create_organization"
    DELETE_ORGANIZATION = "delete_organization"
    UPDATE_ORGANIZATION = "update_organization"
    ASSIGN_USER_TO_ORGANIZATION = "assign_user_to_organization"
    REVOKE_USER_TO_ORGANIZATION_ASSIGNMENT = "revoke_user_to_organization_assignment"
    ASSIGN_ROLE_TO_USER = "assign_role_to_user"
    REVOKE_ROLE_TO_USER_ASSIGNMENT = "revoke_role_to_user_assignment"
    CREATE_BUILDING = "create_building"
    DELETE_BUILDING = "delete_building"
    DELETE_BUILDINGS_BY_PROJECT_ID = "delete_buildings_by_project_id"
    UPDATE_BUILDING = "update_building"
    CREATE_BUILDING_LEVEL = "create_building_level"
    DELETE_BUILDING_LEVEL = "delete_building_level"
    DELETE_BUILDING_LEVELS_BY_BUILDING_ID = "delete_building_levels_by_building_id"
    UPDATE_BUILDING_LEVEL = "update_building_level"
    CREATE_BUILDING_LEVEL_ROOM = "create_building_level_room"
    DELETE_BUILDING_LEVEL_ROOM = "delete_building_level_room"
    DELETE_BUILDING_LEVEL_ROOMS_BY_BUILDING_LEVEL_ID = "delete_building_level_rooms_by_building_level_id"
    UPDATE_BUILDING_LEVEL_ROOM = "update_building_level_room"
    LINK_BUILDING_LEVEL_TO_BUILDING = "link_building_level_to_building"
    UNLINK_BUILDING_LEVEL_FROM_BUILDING = "unlink_building_level_from_building"
    UPDATE_BUILDING_LEVEL_ROOM_INDEX = "update_building_level_room_index"
    CREATE_MANUFACTURER = "create_manufacturer"
    UPDATE_MANUFACTURER = "update_manufacturer"
    DELETE_MANUFACTURER = "delete_manufacturer"
    CREATE_EQUIPMENT = "create_equipment"
    UPDATE_EQUIPMENT = "update_equipment"
    DELETE_EQUIPMENT = "delete_equipment"
    DELETE_EQUIPMENT_BY_PROJECT_ID = "delete_equipment_by_project_id"
    CREATE_EQUIPMENT_PROJECT_CATEGORY = "create_equipment_project_category"
    UPDATE_EQUIPMENT_PROJECT_CATEGORY = "update_equipment_project_category"
    DELETE_EQUIPMENT_PROJECT_CATEGORY = "delete_equipment_project_category"
    CREATE_EQUIPMENT_CATEGORY = "create_equipment_category"
    UPDATE_EQUIPMENT_CATEGORY = "update_equipment_category"
    DELETE_EQUIPMENT_CATEGORY = "delete_equipment_category"
    CREATE_EQUIPMENT_CATEGORY_GROUP = "create_equipment_category_group"
    UPDATE_EQUIPMENT_CATEGORY_GROUP = "update_equipment_category_group"
    DELETE_EQUIPMENT_CATEGORY_GROUP = "delete_equipment_category_group"
    CREATE_EQUIPMENT_MODEL = "create_equipment_model"
    UPDATE_EQUIPMENT_MODEL = "update_equipment_model"
    DELETE_EQUIPMENT_MODEL = "delete_equipment_model"
    CREATE_SUBCONTRACTOR = "create_subcontractor"
    UPDATE_SUBCONTRACTOR = "update_subcontractor"
    DELETE_SUBCONTRACTOR = "delete_subcontractor"
    ASSIGN_SUBCONTRACTOR_TO_ORGANIZATION = "assign_subcontractor_to_organization"
    REVOKE_ASSIGNMENT_SUBCONTRACTOR_TO_ORGANIZATION = (
        "revoke_assignment_subcontractor_to_organization"
    )
    CREATE_UNIT = "create_unit"
    UPDATE_UNIT = "update_unit"
    DELETE_UNIT = "delete_unit"
    CREATE_EQUIPMENT_INPUT = "create_equipment_input"
    UPDATE_EQUIPMENT_INPUT = "update_equipment_input"
    DELETE_EQUIPMENT_INPUT = "delete_equipment_input"
    CREATE_MAINTENANCE_PROCEDURE = "create_maintenance_procedure"
    UPDATE_MAINTENANCE_PROCEDURE = "update_maintenance_procedure"
    DELETE_MAINTENANCE_PROCEDURE = "delete_maintenance_procedure"
    CREATE_MAINTENANCE_PROCEDURE_OPERATION = "create_maintenance_procedure_operation"
    UPDATE_MAINTENANCE_PROCEDURE_OPERATION = "update_maintenance_procedure_operation"
    DELETE_MAINTENANCE_PROCEDURE_OPERATION = "delete_maintenance_procedure_operation"
    CREATE_MAINTENANCE_PROCEDURE_OPERATION_PARAMETER = (
        "create_maintenance_procedure_operation_parameter"
    )
    UPDATE_MAINTENANCE_PROCEDURE_OPERATION_PARAMETER = (
        "update_maintenance_procedure_operation_parameter"
    )
    DELETE_MAINTENANCE_PROCEDURE_OPERATION_PARAMETER = (
        "delete_maintenance_procedure_operation_parameter"
    )
    CREATE_DAILY_CHECK_PROCEDURE = "create_daily_check_procedure"
    UPDATE_DAILY_CHECK_PROCEDURE = "update_daily_check_procedure"
    DELETE_DAILY_CHECK_PROCEDURE = "delete_daily_check_procedure"
    CREATE_DAILY_CHECK_PROCEDURE_OPERATION = "create_daily_check_procedure_operation"
    UPDATE_DAILY_CHECK_PROCEDURE_OPERATION = "update_daily_check_procedure_operation"
    DELETE_DAILY_CHECK_PROCEDURE_OPERATION = "delete_daily_check_procedure_operation"
    CREATE_DAILY_CHECK_PROCEDURE_OPERATION_PARAMETER = (
        "create_daily_check_procedure_operation_parameter"
    )
    UPDATE_DAILY_CHECK_PROCEDURE_OPERATION_PARAMETER = (
        "update_daily_check_procedure_operation_parameter"
    )
    DELETE_DAILY_CHECK_PROCEDURE_OPERATION_PARAMETER = (
        "delete_daily_check_procedure_operation_parameter"
    )
    CHANGE_PROJECT_STATE = "change_project_state"
    LINK_EQUIPMENT_PROJECT_CATEGORY_GROUP = "link_equipment_project_category_group"
    UNLINK_EQUIPMENT_PROJECT_CATEGORY_GROUP = "unlink_equipment_project_category_group"
    CREATE_STANDARD_MAINTENANCE_PROCEDURE = "create_standard_maintenance_procedure"
    UPDATE_STANDARD_MAINTENANCE_PROCEDURE = "update_standard_maintenance_procedure"
    DELETE_STANDARD_MAINTENANCE_PROCEDURE = "delete_standard_maintenance_procedure"
    CREATE_SUBCONTRACTOR_CATEGORY = "create_subcontractor_category"
    UPDATE_SUBCONTRACTOR_CATEGORY = "update_subcontractor_category"
    DELETE_SUBCONTRACTOR_CATEGORY = "delete_subcontractor_category"
    CREATE_STANDARD_EQUIPMENT_CATEGORY = "create_standard_equipment_category"
    UPDATE_STANDARD_EQUIPMENT_CATEGORY = "update_standard_equipment_category"
    DELETE_STANDARD_EQUIPMENT_CATEGORY = "delete_standard_equipment_category"
    CREATE_STANDARD_EQUIPMENT_CATEGORY_GROUP = (
        "create_standard_equipment_category_group"
    )
    UPDATE_STANDARD_EQUIPMENT_CATEGORY_GROUP = (
        "update_standard_equipment_category_group"
    )
    DELETE_STANDARD_EQUIPMENT_CATEGORY_GROUP = (
        "delete_standard_equipment_category_group"
    )
    CREATE_STANDARD_EQUIPMENT = "create_standard_equipment"
    UPDATE_STANDARD_EQUIPMENT = "update_standard_equipment"
    DELETE_STANDARD_EQUIPMENT = "delete_standard_equipment"
    ASSIGN_ROLE_TO_ORGANIZATION = "assign_role_to_organization"
    REVOKE_ROLE_TO_ORGANIZATION_ASSIGNMENT = "revoke_role_to_organization_assignment"
    ASSIGN_ROLE_TO_PROJECT = "assign_role_to_project"
    REVOKE_ROLE_TO_PROJECT_ASSIGNMENT = "revoke_role_to_project_assignment"
    PROCESS_BULK = "process_bulk"
    VALIDATE_MAINTENANCE_PROCEDURE_OPERATION_TYPE = (
        "validate_maintenance_procedure_operation_type"
    )
    VALIDATE_DAILY_CHECK_PROCEDURE_OPERATION_TYPE = (
        "validate_daily_check_procedure_operation_type"
    )


@extendEnum(CommonCommandConstant)
class ApiCommandConstant(Enum):
    pass


@extendEnum(CommonCommandConstant)
class IdentityCommandConstant(Enum):
    pass
