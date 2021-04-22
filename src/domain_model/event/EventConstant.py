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
    OU_CREATED = "ou_created"
    OU_DELETED = "ou_deleted"
    OU_UPDATED = "ou_updated"
    PERMISSION_CREATED = "permission_created"
    PERMISSION_DELETED = "permission_deleted"
    PERMISSION_UPDATED = "permission_updated"
    PERMISSION_CONTEXT_CREATED = "permission_context_created"
    PERMISSION_CONTEXT_DELETED = "permission_context_deleted"
    PERMISSION_CONTEXT_UPDATED = "permission_context_updated"
    PROJECT_CREATED = "project_created"
    PROJECT_DELETED = "project_deleted"
    PROJECT_UPDATED = "project_updated"
    PROJECT_STATE_CHANGED = "project_state_changed"
    REALM_CREATED = "realm_created"
    REALM_DELETED = "realm_deleted"
    REALM_UPDATED = "realm_updated"
    ROLE_CREATED = "role_created"
    ROLE_DELETED = "role_deleted"
    ROLE_UPDATED = "role_updated"
    USER_CREATED = "user_created"
    USER_DELETED = "user_deleted"
    USER_UPDATED = "user_updated"
    ORGANIZATION_CREATED = "organization_created"
    ORGANIZATION_DELETED = "organization_deleted"
    ORGANIZATION_UPDATED = "organization_updated"
    USER_GROUP_CREATED = "user_group_created"
    USER_GROUP_DELETED = "user_group_deleted"
    USER_GROUP_UPDATED = "user_group_updated"
    ROLE_TO_USER_ASSIGNED = "role_to_user_assigned"
    ROLE_TO_USER_ASSIGNMENT_REVOKED = "role_to_user_assignment_revoked"
    USER_TO_REALM_ASSIGNED = "user_to_realm_assigned"
    USER_TO_REALM_ASSIGNMENT_REVOKED = "user_to_realm_assignment_revoked"
    USER_TO_ORGANIZATION_ASSIGNED = "user_to_organization_assigned"
    USER_TO_ORGANIZATION_ASSIGNMENT_REVOKED = "user_to_organization_assignment_revoked"
    BUILDING_LEVEL_TO_BUILDING_LINKED = "building_level_to_building_linked"
    BUILDING_LEVEL_TO_BUILDING_UNLINKED = "building_level_to_building_unlinked"
    BUILDING_LEVEL_ROOM_CREATED = "building_level_room_created"
    BUILDING_LEVEL_ROOM_DELETED = "building_level_room_deleted"
    BUILDING_LEVEL_ROOM_UPDATED = "building_level_room_updated"
    BUILDING_LEVEL_ROOM_FROM_BUILDING_LEVEL_REMOVED = (
        "building_level_room_from_building_level_removed"
    )
    BUILDING_LEVEL_ROOM_INDEX_UPDATED = "building_level_room_index_updated"
    BUILDING_LEVEL_ROOM_DESCRIPTION_UPDATED = "building_level_room_description_changed"
    BUILDING_LEVEL_ROOM_TO_BUILDING_LEVEL_ADDED = (
        "building_level_room_to_building_level_added"
    )
    BUILDING_CREATED = "building_created"
    BUILDING_DELETED = "building_deleted"
    BUILDING_UPDATED = "building_updated"
    BUILDING_LEVEL_TO_BUILDING_ADDED = "building_level_to_building_added"
    BUILDING_LEVEL_TO_BUILDING_REMOVED = "building_level_to_building_removed"
    BUILDING_LEVEL_CREATED = "building_level_created"
    BUILDING_LEVEL_DELETED = "building_level_deleted"
    BUILDING_LEVEL_REMOVED = "building_level_removed"
    BUILDING_LEVEL_UPDATED = "building_level_updated"
    EQUIPMENT_CREATED = "equipment_created"
    EQUIPMENT_DELETED = "equipment_deleted"
    EQUIPMENT_UPDATED = "equipment_updated"
    MANUFACTURER_CREATED = "manufacturer_created"
    MANUFACTURER_DELETED = "manufacturer_deleted"
    MANUFACTURER_UPDATED = "manufacturer_updated"
    EQUIPMENT_MODEL_CREATED = "equipment_model_created"
    EQUIPMENT_MODEL_DELETED = "equipment_model_deleted"
    EQUIPMENT_MODEL_UPDATED = "equipment_model_updated"
    EQUIPMENT_PROJECT_CATEGORY_CREATED = "equipment_project_category_created"
    EQUIPMENT_PROJECT_CATEGORY_DELETED = "equipment_project_category_deleted"
    EQUIPMENT_PROJECT_CATEGORY_UPDATED = "equipment_project_category_updated"
    EQUIPMENT_CATEGORY_CREATED = "equipment_category_created"
    EQUIPMENT_CATEGORY_DELETED = "equipment_category_deleted"
    EQUIPMENT_CATEGORY_UPDATED = "equipment_category_updated"
    EQUIPMENT_CATEGORY_GROUP_CREATED = "equipment_category_group_created"
    EQUIPMENT_CATEGORY_GROUP_DELETED = "equipment_category_group_deleted"
    EQUIPMENT_CATEGORY_GROUP_UPDATED = "equipment_category_group_updated"
    SUBCONTRACTOR_CREATED = "subcontractor_created"
    SUBCONTRACTOR_UPDATED = "subcontractor_updated"
    SUBCONTRACTOR_DELETED = "subcontractor_deleted"
    SUBCONTRACTOR_REVOKED = "subcontractor_revoked"
    SUBCONTRACTOR_ASSIGNED = "subcontractor_assigned"
    UNIT_CREATED = "unit_created"
    UNIT_UPDATED = "unit_updated"
    UNIT_DELETED = "unit_deleted"
    EQUIPMENT_INPUT_CREATED = "equipment_input_created"
    EQUIPMENT_INPUT_UPDATED = "equipment_input_updated"
    EQUIPMENT_INPUT_DELETED = "equipment_input_deleted"
    MAINTENANCE_PROCEDURE_CREATED = "maintenance_procedure_created"
    MAINTENANCE_PROCEDURE_UPDATED = "maintenance_procedure_updated"
    MAINTENANCE_PROCEDURE_DELETED = "maintenance_procedure_deleted"
    MAINTENANCE_PROCEDURE_OPERATION_CREATED = "maintenance_procedure_operation_created"
    MAINTENANCE_PROCEDURE_OPERATION_UPDATED = "maintenance_procedure_operation_updated"
    MAINTENANCE_PROCEDURE_OPERATION_DELETED = "maintenance_procedure_operation_deleted"
    MAINTENANCE_PROCEDURE_OPERATION_PARAMETER_CREATED = (
        "maintenance_procedure_operation_parameter_created"
    )
    MAINTENANCE_PROCEDURE_OPERATION_PARAMETER_UPDATED = (
        "maintenance_procedure_operation_parameter_updated"
    )
    MAINTENANCE_PROCEDURE_OPERATION_PARAMETER_DELETED = (
        "maintenance_procedure_operation_parameter_deleted"
    )
    DAILY_CHECK_PROCEDURE_CREATED = "daily_check_procedure_created"
    DAILY_CHECK_PROCEDURE_UPDATED = "daily_check_procedure_updated"
    DAILY_CHECK_PROCEDURE_DELETED = "daily_check_procedure_deleted"
    DAILY_CHECK_PROCEDURE_OPERATION_CREATED = "daily_check_procedure_operation_created"
    DAILY_CHECK_PROCEDURE_OPERATION_UPDATED = "daily_check_procedure_operation_updated"
    DAILY_CHECK_PROCEDURE_OPERATION_DELETED = "daily_check_procedure_operation_deleted"
    DAILY_CHECK_PROCEDURE_OPERATION_PARAMETER_CREATED = (
        "daily_check_procedure_operation_parameter_created"
    )
    DAILY_CHECK_PROCEDURE_OPERATION_PARAMETER_UPDATED = (
        "daily_check_procedure_operation_parameter_updated"
    )
    DAILY_CHECK_PROCEDURE_OPERATION_PARAMETER_DELETED = (
        "daily_check_procedure_operation_parameter_deleted"
    )
    EQUIPMENT_PROJECT_CATEGORY_GROUP_LINKED = "equipment_project_category_group_linked"
    EQUIPMENT_PROJECT_CATEGORY_GROUP_UNLINKED = (
        "equipment_project_category_group_unlinked"
    )
    STANDARD_MAINTENANCE_PROCEDURE_CREATED = "standard_maintenance_procedure_created"
    STANDARD_MAINTENANCE_PROCEDURE_UPDATED = "standard_maintenance_procedure_updated"
    STANDARD_MAINTENANCE_PROCEDURE_DELETED = "standard_maintenance_procedure_deleted"
    SUBCONTRACTOR_CATEGORY_CREATED = "subcontractor_category_created"
    SUBCONTRACTOR_CATEGORY_UPDATED = "subcontractor_category_updated"
    SUBCONTRACTOR_CATEGORY_DELETED = "subcontractor_category_deleted"
    STANDARD_EQUIPMENT_CATEGORY_CREATED = "standard_equipment_category_created"
    STANDARD_EQUIPMENT_CATEGORY_UPDATED = "standard_equipment_category_updated"
    STANDARD_EQUIPMENT_CATEGORY_DELETED = "standard_equipment_category_deleted"
    STANDARD_EQUIPMENT_CATEGORY_GROUP_CREATED = (
        "standard_equipment_category_group_created"
    )
    STANDARD_EQUIPMENT_CATEGORY_GROUP_UPDATED = (
        "standard_equipment_category_group_updated"
    )
    STANDARD_EQUIPMENT_CATEGORY_GROUP_DELETED = (
        "standard_equipment_category_group_deleted"
    )
    STANDARD_EQUIPMENT_CREATED = "standard_equipment_created"
    STANDARD_EQUIPMENT_UPDATED = "standard_equipment_updated"
    STANDARD_EQUIPMENT_DELETED = "standard_equipment_deleted"
