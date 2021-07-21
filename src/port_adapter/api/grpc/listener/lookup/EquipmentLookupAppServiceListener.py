"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from src.application.lookup.equipment.MaintenanceProcedureOperationLabel import MaintenanceProcedureOperationLabel
import src.port_adapter.AppDi as AppDi
from src.application.lookup.equipment.Building import Building
from src.application.lookup.equipment.BuildingLevel import BuildingLevel
from src.application.lookup.equipment.BuildingLevelRoom import BuildingLevelRoom
from src.application.lookup.equipment.EquipmentCategoryGroup import (
    EquipmentCategoryGroup,
)
from src.application.lookup.equipment.EquipmentLookupApplicationService import (
    EquipmentLookupApplicationService,
)
from src.application.lookup.equipment.EquipmentModel import EquipmentModel
from src.application.lookup.equipment.EquipmentProjectCategory import (
    EquipmentProjectCategory,
)
from src.application.lookup.equipment.MaintenanceProcedure import MaintenanceProcedure
from src.application.lookup.equipment.MaintenanceProcedureOperation import (
    MaintenanceProcedureOperation,
)
from src.application.lookup.equipment.MaintenanceProcedureOperationParameter import (
    MaintenanceProcedureOperationParameter,
)
from src.application.lookup.equipment.Manufacturer import Manufacturer
from src.application.lookup.equipment.Subcontractor import Subcontractor
from src.application.lookup.equipment.Unit import Unit
from src.port_adapter.api.grpc.listener.lookup.BaseLookupListener import (
    BaseLookupListener,
)
from src.resource.proto._generated.project.lookup.equipment.building_level_pb2 import (
    BuildingLevel as ProtoBuildingLevel,
)
from src.resource.proto._generated.project.lookup.equipment.building_level_room_pb2 import (
    BuildingLevelRoom as ProtoBuildingLevelRoom,
)
from src.resource.proto._generated.project.lookup.equipment.building_pb2 import (
    Building as ProtoBuilding,
)
from src.resource.proto._generated.project.lookup.equipment.equipment_category_group_pb2 import (
    EquipmentCategoryGroup as ProtoEquipmentCategoryGroup,
)
from src.resource.proto._generated.project.lookup.equipment.equipment_lookup_app_service_pb2 import (
    EquipmentLookupAppService_lookupResponse,
)
from src.resource.proto._generated.project.lookup.equipment.equipment_lookup_app_service_pb2_grpc import (
    EquipmentLookupAppServiceServicer,
)
from src.resource.proto._generated.project.lookup.equipment.equipment_model_pb2 import (
    EquipmentModel as ProtoEquipmentModel,
)
from src.resource.proto._generated.project.lookup.equipment.equipment_project_category_pb2 import (
    EquipmentProjectCategory as ProtoEquipmentProjectCategory,
)
from src.resource.proto._generated.project.lookup.equipment.maintenance_procedure_operation_parameter_pb2 import (
    MaintenanceProcedureOperationParameter as ProtoMaintenanceProcedureOperationParameter,
)
from src.resource.proto._generated.project.lookup.equipment.maintenance_procedure_operation_label_pb2 import (
    MaintenanceProcedureOperationLabel as ProtoMaintenanceProcedureOperationLabel,
)
from src.resource.proto._generated.project.lookup.equipment.maintenance_procedure_operation_pb2 import (
    MaintenanceProcedureOperation as ProtoMaintenanceProcedureOperation,
)
from src.resource.proto._generated.project.lookup.equipment.maintenance_procedure_pb2 import (
    MaintenanceProcedure as ProtoMaintenanceProcedure,
)
from src.resource.proto._generated.project.lookup.equipment.manufacturer_pb2 import (
    Manufacturer as ProtoManufacturer,
)
from src.resource.proto._generated.project.lookup.equipment.subcontractor_pb2 import (
    Subcontractor as ProtoSubcontractor,
)
from src.resource.proto._generated.project.lookup.equipment.unit_pb2 import Unit as ProtoUnit


class EquipmentLookupAppServiceListener(
    BaseLookupListener, EquipmentLookupAppServiceServicer
):
    """The listener function implements the rpc call as described in the .proto file"""

    def __init__(self):
        super().__init__()
        self._appService: EquipmentLookupApplicationService = AppDi.instance.get(
            EquipmentLookupApplicationService
        )
        self._lookupResponse = EquipmentLookupAppService_lookupResponse
        self._responseAttribute = "equipments"

    def __str__(self):
        return self.__class__.__name__

    def _lookupModelDataTypeToGrpcType(self, modelDataType):
        mapping = {
            EquipmentProjectCategory: ProtoEquipmentProjectCategory,
            EquipmentCategoryGroup: ProtoEquipmentCategoryGroup,
            Building: ProtoBuilding,
            BuildingLevel: ProtoBuildingLevel,
            BuildingLevelRoom: ProtoBuildingLevelRoom,
            Manufacturer: ProtoManufacturer,
            EquipmentModel: ProtoEquipmentModel,
            MaintenanceProcedure: ProtoMaintenanceProcedure,
            MaintenanceProcedureOperation: ProtoMaintenanceProcedureOperation,
            MaintenanceProcedureOperationParameter: ProtoMaintenanceProcedureOperationParameter,
            MaintenanceProcedureOperationLabel: ProtoMaintenanceProcedureOperationLabel,
            Subcontractor: ProtoSubcontractor,
            Unit: ProtoUnit,
        }

        return mapping[modelDataType] if modelDataType in mapping else None
