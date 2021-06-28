"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

import src.port_adapter.AppDi as AppDi
from src.application.lookup.daily_check_procedure.DailyCheckProcedureApplicationService import \
    DailyCheckProcedureApplicationService
from src.application.lookup.daily_check_procedure.DailyCheckProcedureOperation import DailyCheckProcedureOperation
from src.application.lookup.daily_check_procedure.DailyCheckProcedureOperationParameter import \
    DailyCheckProcedureOperationParameter
from src.application.lookup.daily_check_procedure.EquipmentCategoryGroup import EquipmentCategoryGroup
from src.application.lookup.daily_check_procedure.Unit import Unit
from src.port_adapter.api.grpc.listener.lookup.BaseLookupListener import BaseLookupListener
from src.resource.proto._generated.project.lookup.daily_check_procedure.daily_check_procedure_lookup_app_service_pb2 import \
    DailyCheckProcedureLookupAppService_lookupResponse
from src.resource.proto._generated.project.lookup.daily_check_procedure.daily_check_procedure_lookup_app_service_pb2_grpc import \
    DailyCheckProcedureLookupAppServiceServicer

from src.resource.proto._generated.project.lookup.daily_check_procedure.daily_check_procedure_operation_parameter_pb2 import \
    DailyCheckProcedureOperationParameter as ProtoDailyCheckProcedureOperationParameter
from src.resource.proto._generated.project.lookup.daily_check_procedure.daily_check_procedure_operation_pb2 import \
    DailyCheckProcedureOperation as ProtoDailyCheckProcedureOperation
from src.resource.proto._generated.project.lookup.daily_check_procedure.equipment_category_group_pb2 import \
    EquipmentCategoryGroup as ProtoEquipmentCategoryGroup
from src.resource.proto._generated.project.lookup.daily_check_procedure.unit_pb2 import \
    Unit as ProtoUnit


class DailyCheckProcedureLookupAppServiceListener(BaseLookupListener, DailyCheckProcedureLookupAppServiceServicer):
    """The listener function implements the rpc call as described in the .proto file"""

    def __init__(self):
        super().__init__()
        self._appService: DailyCheckProcedureApplicationService = AppDi.instance.get(
            DailyCheckProcedureApplicationService
        )
        self._lookupResponse = DailyCheckProcedureLookupAppService_lookupResponse
        self._responseAttribute = 'daily_check_procedures'

    def __str__(self):
        return self.__class__.__name__


    def _lookupModelDataTypeToGrpcType(self, modelDataType):
        mapping = {
            EquipmentCategoryGroup: ProtoEquipmentCategoryGroup,
            DailyCheckProcedureOperation: ProtoDailyCheckProcedureOperation,
            DailyCheckProcedureOperationParameter: ProtoDailyCheckProcedureOperationParameter,
            Unit: ProtoUnit,
        }

        return mapping[modelDataType] if modelDataType in mapping else None
