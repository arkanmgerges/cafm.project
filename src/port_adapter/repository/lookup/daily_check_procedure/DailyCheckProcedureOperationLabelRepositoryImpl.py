"""
The file is generated by scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""







import os

from elasticsearch_dsl import UpdateByQuery, Q, Search
from elasticsearch_dsl.connections import connections
from sqlalchemy import create_engine

from src.application.lookup.daily_check_procedure.DailyCheckProcedureOperationLabelRepository import DailyCheckProcedureOperationLabelRepository
from src.domain_model.project.unit.UnitRepository import UnitRepository
from src.domain_model.project.daily_check.procedure.operation.label.DailyCheckProcedureOperationLabel import DailyCheckProcedureOperationLabel
from src.port_adapter.repository.es_model.lookup.daily_check_procedure.DailyCheckProcedure import (DailyCheckProcedure as EsDailyCheckProcedure,)
from src.port_adapter.repository.lookup.common.es.UpdateByQueryValidator import UpdateByQueryValidator
from src.resource.logging.decorator import debugLogger
from src.resource.logging.logger import logger


class DailyCheckProcedureOperationLabelRepositoryImpl(DailyCheckProcedureOperationLabelRepository):
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
                f"[{DailyCheckProcedureOperationLabelRepositoryImpl.__init__.__qualname__}] Could not connect to the db, message: {e}"
            )
            raise Exception(f"Could not connect to the db, message: {e}")




    @debugLogger
    def delete(self, obj: DailyCheckProcedureOperationLabel):
        if obj is not None:
            UpdateByQueryValidator.validate(UpdateByQuery(index=EsDailyCheckProcedure.alias()).using(self._es) \
                .filter("nested", path="daily_check_procedure_operations.daily_check_procedure_operation_labels", query=Q("term", **{
                            "daily_check_procedure_operations.daily_check_procedure_operation_labels.id": obj.id()})) \
                .script(
                source="""
                        if (ctx._source.daily_check_procedure_operations instanceof List) {
                         for (int i=ctx._source.daily_check_procedure_operations.length - 1; i >= 0; i--) {
                                if (ctx._source.daily_check_procedure_operations[i].daily_check_procedure_operation_labels instanceof List) {
                                 for (int j=ctx._source.daily_check_procedure_operations[i].daily_check_procedure_operation_labels.length - 1; j >= 0; j--) {
                                        if (ctx._source.daily_check_procedure_operations[i].daily_check_procedure_operation_labels[j].id == params.id) {
                                            ctx._source.daily_check_procedure_operations[i].daily_check_procedure_operation_labels.remove(j);
                                        }

                                        }
                                }
                        }
                        }
                            """,
                params={"id": obj.id()}).execute())

    @debugLogger
    def save(self, obj: DailyCheckProcedureOperationLabel):
        if obj is not None:
            UpdateByQueryValidator.validate(UpdateByQuery(index=EsDailyCheckProcedure.alias()).using(self._es) \
                .filter("nested", path="daily_check_procedure_operations", query=Q("term", **{
                            "daily_check_procedure_operations.id": obj.dailyCheckProcedureOperationId()})) \
                .script(
                source="""
                        if (ctx._source.daily_check_procedure_operations instanceof List) {
                            boolean found = false;
                            for (int i=ctx._source.daily_check_procedure_operations.length - 1; i >= 0; i--) {
                                if (ctx._source.daily_check_procedure_operations[i].daily_check_procedure_operation_labels instanceof List) {
                                    for (int j=ctx._source.daily_check_procedure_operations[i].daily_check_procedure_operation_labels.length - 1; j >= 0; j--) {
                                        if (ctx._source.daily_check_procedure_operations[i].daily_check_procedure_operation_labels[j].id != null) {
                                            if (ctx._source.daily_check_procedure_operations[i].daily_check_procedure_operation_labels[j].id == params.obj.id) {
                                                found = true;
                                                if (params.obj.label != null) {
                                                    ctx._source.daily_check_procedure_operations[i].daily_check_procedure_operation_labels[j].label = params.obj.label;
                                                }
                                                if (params.obj.generate_alert != null) {
                                                    ctx._source.daily_check_procedure_operations[i].daily_check_procedure_operation_labels[j].generate_alert = params.obj.generate_alert;
                                                }
                                            }
                                        }
                                    }
                                }
                            }

                            if (found == false) {
                                for (int i=ctx._source.daily_check_procedure_operations.length - 1; i >= 0; i--) {
                                    if (ctx._source.daily_check_procedure_operations[i].id == params.daily_check_procedure_operation_id) {
                                        if (!(ctx._source.daily_check_procedure_operations[i].daily_check_procedure_operation_labels instanceof List)) {
                                            ctx._source.daily_check_procedure_operations[i].daily_check_procedure_operation_labels = [];
                                        }
                                        ctx._source.daily_check_procedure_operations[i].daily_check_procedure_operation_labels.add(params.obj);
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
                    "daily_check_procedure_operation_id": obj.dailyCheckProcedureOperationId(),
                }).execute())
