"""
The file is generated by scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""



from src.domain_model.resource.exception.InvalidStateException import InvalidStateException
import time
import os
from typing import Counter

from elasticsearch_dsl import UpdateByQuery, Q, Search
from elasticsearch_dsl.connections import connections
from sqlalchemy import create_engine

from src.application.lookup.equipment.MaintenanceProcedureOperationLabelRepository import MaintenanceProcedureOperationLabelRepository
from src.domain_model.project.maintenance.procedure.operation.label.MaintenanceProcedureOperationLabel import MaintenanceProcedureOperationLabel
from src.domain_model.project.unit.UnitRepository import UnitRepository
from src.port_adapter.repository.es_model.lookup.equipment.Equipment import Equipment as EsEquipment
from src.resource.logging.decorator import debugLogger
from src.resource.logging.logger import logger


class MaintenanceProcedureOperationLabelRepositoryImpl(MaintenanceProcedureOperationLabelRepository):
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
                f"[{MaintenanceProcedureOperationLabelRepositoryImpl.__init__.__qualname__}] Could not connect to the db, message: {e}"
            )
            raise Exception(f"Could not connect to the db, message: {e}")

    @debugLogger
    def delete(self, obj: MaintenanceProcedureOperationLabel):
        if obj is not None:
            UpdateByQuery(index=EsEquipment.alias()).using(self._es) \
                .filter('nested', path="maintenance_procedures.maintenance_procedure_operations",
                        query=Q("term",
                                **{"maintenance_procedures.maintenance_procedure_operations.id": obj.maintenanceProcedureOperationId()})) \
                .script(
                source="""
                            for (int i=ctx._source.maintenance_procedures.length - 1; i >= 0; i--) {
                                if (ctx._source.maintenance_procedures[i].maintenance_procedure_operations instanceof List) {
                                    for (int j=ctx._source.maintenance_procedures[i].maintenance_procedure_operations.length - 1; j >= 0; j--) {
                                        if (ctx._source.maintenance_procedures[i].maintenance_procedure_operations[j].maintenance_procedure_operation_labels instanceof List) {
                                            for (int k=ctx._source.maintenance_procedures[i].maintenance_procedure_operations[j].maintenance_procedure_operation_labels.length - 1; k >= 0; k--) {
                                                if (ctx._source.maintenance_procedures[i].maintenance_procedure_operations[j].maintenance_procedure_operation_labels[k].id == params.id) {
                                                    ctx._source.maintenance_procedures[i].maintenance_procedure_operations[j].maintenance_procedure_operation_labels.remove(k);
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                            """,
                params={"id": obj.id()}).execute()

    @debugLogger
    def save(self, obj: MaintenanceProcedureOperationLabel):
        if obj is not None:
            ubq = UpdateByQuery(index=EsEquipment.alias()).using(self._es) \
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
                                        if (ctx._source.maintenance_procedures[i].maintenance_procedure_operations[j].maintenance_procedure_operation_labels instanceof List) {
                                            for (int k=ctx._source.maintenance_procedures[i].maintenance_procedure_operations[j].maintenance_procedure_operation_labels.length - 1; k >= 0; k--) {
                                                if (ctx._source.maintenance_procedures[i].maintenance_procedure_operations[j].maintenance_procedure_operation_labels[k].id == params.obj.id) {
                                                    found = true;
                                                    if (params.obj.label != null) {
                                                        ctx._source.maintenance_procedures[i].maintenance_procedure_operations[j].maintenance_procedure_operation_labels[k].label = params.obj.label;
                                                    }
                                                    if (params.obj.generate_alert != null) {
                                                        ctx._source.maintenance_procedures[i].maintenance_procedure_operations[j].maintenance_procedure_operation_labels[k].generate_alert = params.obj.generate_alert;
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
                                                if (!(ctx._source.maintenance_procedures[i].maintenance_procedure_operations[j].maintenance_procedure_operation_labels instanceof List)) {
                                                    ctx._source.maintenance_procedures[i].maintenance_procedure_operations[j].maintenance_procedure_operation_labels = [];
                                                }
                                                ctx._source.maintenance_procedures[i].maintenance_procedure_operations[j].maintenance_procedure_operation_labels.add(params.obj);
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
                        "label": obj.label(),
                        "generate_alert": obj.generateAlert(),
                    },
                    "maintenance_procedure_operation_id": obj.maintenanceProcedureOperationId()
                })
            res = ubq.execute()
            resDict = res.to_dict()

            if resDict["updated"] == 0:
                raise Exception(f"{resDict}")