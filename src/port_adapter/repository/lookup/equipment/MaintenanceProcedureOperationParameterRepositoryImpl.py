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
from src.port_adapter.repository.es_model.lookup.equipment.Equipment import Equipment as EsEquipment
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
        except Exception as e:
            logger.warn(
                f"[{MaintenanceProcedureOperationParameterRepositoryImpl.__init__.__qualname__}] Could not connect to the db, message: {e}"
            )
            raise Exception(f"Could not connect to the db, message: {e}")

    @debugLogger
    def delete(self, obj: MaintenanceProcedureOperationParameter):
        if obj is not None:
            UpdateByQuery(index=EsEquipment.alias()).using(self._es) \
                .filter('nested', path="maintenance_procedures.maintenance_procedure_operations",
                        query=Q("term",
                                **{"maintenance_procedures.maintenance_procedure_operations.id": obj.id()})) \
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
                params={"id": obj.id()}).execute()

    @debugLogger
    def save(self, obj: MaintenanceProcedureOperationParameter):
        if obj is not None:
            UpdateByQuery(index=EsEquipment.alias()).using(self._es) \
                .filter('nested', path="maintenance_procedures.maintenance_procedure_operations",
                        query=Q("term",
                                **{"maintenance_procedures.maintenance_procedure_operations.id": obj.id()})) \
                .script(
                source="""
                                for (int i=ctx._source.maintenance_procedures.length - 1; i >= 0; i--) {
                                    if (ctx._source.maintenance_procedures[i].maintenance_procedure_operations instanceof List) {
                                        for (int j=ctx._source.maintenance_procedures[i].maintenance_procedure_operations.length - 1; j >= 0; j--) {
                                            found = false;
                                            if (ctx._source.maintenance_procedures[i].maintenance_procedure_operations[j].maintenance_procedure_operation_parameters instanceof List) {
                                                for (int k=ctx._source.maintenance_procedures[i].maintenance_procedure_operations[j].maintenance_procedure_operation_parameters.length - 1; k >= 0; k--) {                                    
                                                    if (ctx._source.maintenance_procedures[i].maintenance_procedure_operations[j].maintenance_procedure_operation_parameters[k].id == params.id) {
                                                        found = true;
                                                        if (params.name != null) {
                                                            ctx._source.maintenance_procedures[i].maintenance_procedure_operations[j].maintenance_procedure_operation_parameters[k].name = params.name;
                                                        }
                                                        if (params.min_value != null) {
                                                            ctx._source.maintenance_procedures[i].maintenance_procedure_operations[j].maintenance_procedure_operation_parameters[k].min_value = params.min_value;
                                                        } 
                                                        if (params.max_value != null) {
                                                            ctx._source.maintenance_procedures[i].maintenance_procedure_operations[j].maintenance_procedure_operation_parameters[k].max_value = params.max_value;
                                                        }
                                                    }
                                                }
                                            }
                                            
                                            if (found == false) {
                                                    ctx._source.maintenance_procedures[i].maintenance_procedure_operations.add(
                                                        {
                                                            "id": params.id,
                                                            "name": params.name,
                                                            "min_value": params.min_value,
                                                            "max_value": params.max_value
                                                        }
                                                    );
                                            }    
                                        }
                                    }
                                }
                                """,
                params={
                    "id": obj.id(),
                    "name": obj.name(),
                    "min_value": obj.minValue(),
                    "max_value": obj.maxValue(),
                }).execute()