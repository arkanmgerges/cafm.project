"""
The file is generated by scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""



import os

from elasticsearch_dsl import UpdateByQuery, Q
from elasticsearch_dsl.connections import connections
from sqlalchemy import create_engine

from src.application.lookup.equipment.MaintenanceProcedureOperationParameterRepository import MaintenanceProcedureOperationParameterRepository
from src.domain_model.project.maintenance.procedure.operation.parameter.MaintenanceProcedureOperationParameter import MaintenanceProcedureOperationParameter
from src.domain_model.project.unit.UnitRepository import UnitRepository
from src.port_adapter.repository.es_model.lookup.equipment.Equipment import Equipment as EsEquipment
from src.port_adapter.repository.lookup.common.es.UpdateByQueryValidator import UpdateByQueryValidator
from src.resource.logging.decorator import debugLogger
from src.resource.logging.logger import logger


class MaintenanceProcedureOperationParameterRepositoryImpl(MaintenanceProcedureOperationParameterRepository):
    def __init__(self):
        try:
            self._db = create_engine(
                f"mysql+mysqlconnector://{os.getenv('CAFM_PROJECT_DB_USER', 'root')}:{os.getenv('CAFM_PROJECT_DB_PASSWORD', '1234')}@{os.getenv('CAFM_PROJECT_DB_HOST', '127.0.0.1')}:{os.getenv('CAFM_PROJECT_DB_PORT', '3306')}/{os.getenv('CAFM_PROJECT_DB_NAME', 'cafm-project')}"
            )
            self._es = connections.create_connection(
                hosts=[
                    f'{os.getenv("CAFM_PROJECT_ELASTICSEARCH_HOST", "elasticsearch")}:{os.getenv("CAFM_PROJECT_ELASTICSEARCH_PORT", 9200)}'
                ]
            )
            import src.port_adapter.AppDi as AppDi
            self._unitRepo = AppDi.instance.get(UnitRepository)
        except Exception as e:
            logger.warn(
                f"[{MaintenanceProcedureOperationParameterRepositoryImpl.__init__.__qualname__}] Could not connect to the db, message: {e}"
            )
            raise Exception(f"Could not connect to the db, message: {e}")

    @debugLogger
    def delete(self, obj: MaintenanceProcedureOperationParameter):
        if obj is not None:
            UpdateByQueryValidator.validate(UpdateByQuery(index=EsEquipment.alias()).using(self._es) \
                .filter('nested', path="maintenance_procedures.maintenance_procedure_operations.maintenance_procedure_operation_parameters",
                        query=Q("term",
                                **{"maintenance_procedures.maintenance_procedure_operations.maintenance_procedure_operation_parameters.id": obj.id()})) \
                .script(
                source="""
                            for (int i=ctx._source.maintenance_procedures.length - 1; i >= 0; i--) {
                                if (ctx._source.maintenance_procedures[i].maintenance_procedure_operations instanceof List) {
                                    for (int j=ctx._source.maintenance_procedures[i].maintenance_procedure_operations.length - 1; j >= 0; j--) {
                                        if (ctx._source.maintenance_procedures[i].maintenance_procedure_operations[j].maintenance_procedure_operation_parameters instanceof List) {
                                            for (int k=ctx._source.maintenance_procedures[i].maintenance_procedure_operations[j].maintenance_procedure_operation_parameters.length - 1; k >= 0; k--) {
                                                if (ctx._source.maintenance_procedures[i].maintenance_procedure_operations[j].maintenance_procedure_operation_parameters[k].id == params.id) {
                                                    ctx._source.maintenance_procedures[i].maintenance_procedure_operations[j].maintenance_procedure_operation_parameters.remove(k);
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                            """,
                params={"id": obj.id()}).execute())

    @debugLogger
    def save(self, obj: MaintenanceProcedureOperationParameter):
        unit = None
        try:
            unit = self._unitRepo.unitById(obj.unitId())
        except: pass

        if obj is not None:
            UpdateByQueryValidator.validate(UpdateByQuery(index=EsEquipment.alias()).using(self._es) \
                .filter('nested', path="maintenance_procedures.maintenance_procedure_operations",
                        query=Q("term",
                                **{"maintenance_procedures.maintenance_procedure_operations.id": obj.maintenanceProcedureOperationId()})) \
                .script(
                source="""
                        if (ctx._source.maintenance_procedures instanceof List) {
                            boolean found = false;
                            for (int i=ctx._source.maintenance_procedures.length - 1; i >= 0; i--) {
                                if (ctx._source.maintenance_procedures[i].maintenance_procedure_operations instanceof List) {
                                    for (int j=ctx._source.maintenance_procedures[i].maintenance_procedure_operations.length - 1; j >= 0; j--) {
                                        if (ctx._source.maintenance_procedures[i].maintenance_procedure_operations[j].maintenance_procedure_operation_parameters instanceof List) {
                                            for (int k=ctx._source.maintenance_procedures[i].maintenance_procedure_operations[j].maintenance_procedure_operation_parameters.length - 1; k >= 0; k--) {
                                                if (ctx._source.maintenance_procedures[i].maintenance_procedure_operations[j].maintenance_procedure_operation_parameters[k].id == params.obj.id) {
                                                    found = true;
                                                    if (params.obj.name != null) {
                                                        ctx._source.maintenance_procedures[i].maintenance_procedure_operations[j].maintenance_procedure_operation_parameters[k].name = params.obj.name;
                                                    }
                                                    if (params.obj.min_value != null) {
                                                        ctx._source.maintenance_procedures[i].maintenance_procedure_operations[j].maintenance_procedure_operation_parameters[k].min_value = params.obj.min_value;
                                                    }
                                                    if (params.obj.max_value != null) {
                                                        ctx._source.maintenance_procedures[i].maintenance_procedure_operations[j].maintenance_procedure_operation_parameters[k].max_value = params.obj.max_value;
                                                    }
                                                    if (params.obj.unit != null) {
                                                        ctx._source.maintenance_procedures[i].maintenance_procedure_operations[j].maintenance_procedure_operation_parameters[k].unit = params.obj.unit;
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                            if (found == false) {
                                for (int i=ctx._source.maintenance_procedures.length - 1; i >= 0; i--) {
                                    if (ctx._source.maintenance_procedures[i].maintenance_procedure_operations instanceof List) {
                                        for (int j=ctx._source.maintenance_procedures[i].maintenance_procedure_operations.length - 1; j >= 0; j--) {
                                            if (ctx._source.maintenance_procedures[i].maintenance_procedure_operations[j].id == params.maintenance_procedure_operation_id) {
                                                if (!(ctx._source.maintenance_procedures[i].maintenance_procedure_operations[j].maintenance_procedure_operation_parameters instanceof List)) {
                                                    ctx._source.maintenance_procedures[i].maintenance_procedure_operations[j].maintenance_procedure_operation_parameters = [];
                                                }
                                                ctx._source.maintenance_procedures[i].maintenance_procedure_operations[j].maintenance_procedure_operation_parameters.add(params.obj);
                                            }
                                        }
                                    }
                                }
                            }
                        }
                        """,
                params={
                    "obj": {
                        "id": obj.id(),
                        "name": obj.name(),
                        "min_value": obj.minValue(),
                        "max_value": obj.maxValue(),
                        "unit": {
                            "id": unit.id() if unit is not None else None,
                            "name": unit.name() if unit is not None else None
                        }
                    },
                    "maintenance_procedure_operation_id": obj.maintenanceProcedureOperationId()
                }).execute())