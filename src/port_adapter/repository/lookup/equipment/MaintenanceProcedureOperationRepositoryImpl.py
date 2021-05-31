"""
The file is generated by scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""



import os

from elasticsearch_dsl import UpdateByQuery, Q
from elasticsearch_dsl.connections import connections
from sqlalchemy import create_engine

from src.application.lookup.equipment.MaintenanceProcedureOperationRepository import MaintenanceProcedureOperationRepository
from src.domain_model.project.maintenance.procedure.operation.MaintenanceProcedureOperation import MaintenanceProcedureOperation
from src.port_adapter.repository.es_model.lookup.equipment.Equipment import Equipment as EsEquipment
from src.resource.logging.decorator import debugLogger
from src.resource.logging.logger import logger


class MaintenanceProcedureOperationRepositoryImpl(MaintenanceProcedureOperationRepository):
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
                f"[{MaintenanceProcedureOperationRepositoryImpl.__init__.__qualname__}] Could not connect to the db, message: {e}"
            )
            raise Exception(f"Could not connect to the db, message: {e}")

    @debugLogger
    def delete(self, obj: MaintenanceProcedureOperation):
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
                                        if (ctx._source.maintenance_procedures[i].maintenance_procedure_operations[j].id == params.id) {
                                            ctx._source.maintenance_procedures[i].maintenance_procedure_operations.remove(j);
                                        }
                                    }
                                }
                            }
                            """,
            params={"id": obj.id()}).execute()

    @debugLogger
    def save(self, obj: MaintenanceProcedureOperation):
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
                                        if (ctx._source.maintenance_procedures[i].maintenance_procedure_operations[j].id == params.id) {
                                            if (params.name != null) {
                                                ctx._source.maintenance_procedures[i].maintenance_procedure_operations[j].name = params.name
                                            }
                                            if (params.description != null) {
                                                ctx._source.maintenance_procedures[i].maintenance_procedure_operations[j].description = params.description
                                            }
                                            if (params.type != null) {
                                                ctx._source.maintenance_procedures[i].maintenance_procedure_operations[j].type = params.type
                                            }
                                        }
                                    }
                                }
                            }
                            """,
                params={
                 "id": obj.id(),
                 "name": obj.name(),
                 "description": obj.description(),
                 "type": obj.type(),
                 }).execute()