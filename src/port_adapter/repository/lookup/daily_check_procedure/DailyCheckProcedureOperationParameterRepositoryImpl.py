"""
The file is generated by scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""







import os

from elasticsearch_dsl import UpdateByQuery, Q, Search
from elasticsearch_dsl.connections import connections
from sqlalchemy import create_engine

from src.application.lookup.daily_check_procedure.DailyCheckProcedureOperationParameterRepository import DailyCheckProcedureOperationParameterRepository
from src.domain_model.project.daily_check.procedure.operation.parameter.DailyCheckProcedureOperationParameter import DailyCheckProcedureOperationParameter
from src.port_adapter.repository.es_model.lookup.daily_check_procedure.DailyCheckProcedure import (DailyCheckProcedure as EsDailyCheckProcedure,)
from src.resource.logging.decorator import debugLogger
from src.resource.logging.logger import logger


class DailyCheckProcedureOperationParameterRepositoryImpl(DailyCheckProcedureOperationParameterRepository):
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
                f"[{DailyCheckProcedureOperationParameterRepositoryImpl.__init__.__qualname__}] Could not connect to the db, message: {e}"
            )
            raise Exception(f"Could not connect to the db, message: {e}")


    
           
    @debugLogger
    def delete(self, obj: DailyCheckProcedureOperationParameter):
        if obj is not None:
            UpdateByQuery(index=EsDailyCheckProcedure.alias()).using(self._es) \
                .filter('nested', path="daily_check_procedure_operations.daily_check_procedure_operation_parameters",
                        query=Q("term",
                                **{"daily_check_procedure_operations.daily_check_procedure_operation_parameters.id": obj.id()})) \
                .script(
                source="""                        
                        if (ctx._source.daily_check_procedure_operations instanceof List) {
                         for (int i=ctx._source.daily_check_procedure_operations.length - 1; i >= 0; i--) {                        
                                if (ctx._source.daily_check_procedure_operations[i].daily_check_procedure_operation_parameters instanceof List) {
                                 for (int j=ctx._source.daily_check_procedure_operations[i].daily_check_procedure_operation_parameters.length - 1; j >= 0; j--) {
                                        if (ctx._source.daily_check_procedure_operations[i].daily_check_procedure_operation_parameters[j].id == params.id) {
                                            ctx._source.daily_check_procedure_operations[i].daily_check_procedure_operation_parameters.remove(j);
                                        }
                        
                                        }
                                }    
                        }
                        }
                            """,
                params={"id": obj.id()}).execute()

    @debugLogger
    def save(self, obj: DailyCheckProcedureOperationParameter):
        if obj is not None: 
                result = EsDailyCheckProcedure.search().filter("nested", path="daily_check_procedure_operations.daily_check_procedure_operation_parameters", query=Q("term", **{
                        "daily_check_procedure_operations.daily_check_procedure_operation_parameters.id": obj.id()})).execute()
                if result.hits.total.value > 0:
                    # Update
                    UpdateByQuery(index=EsDailyCheckProcedure.alias()).using(self._es) \
                        .filter("nested", path="daily_check_procedure_operations.daily_check_procedure_operation_parameters", query=Q("term", **{
                            "daily_check_procedure_operations.daily_check_procedure_operation_parameters.id": obj.id()})) \
                        .script(source="""
                             if (ctx._source.daily_check_procedure_operations instanceof List) {
                             for (int i=ctx._source.daily_check_procedure_operations.length - 1; i >= 0; i--) {
                                         if (ctx._source.daily_check_procedure_operations[i].daily_check_procedure_operation_parameters instanceof List) {
                                         for (int j=ctx._source.daily_check_procedure_operations[i].daily_check_procedure_operation_parameters.length - 1; j >= 0; j--) {
                                                 if (ctx._source.daily_check_procedure_operations[i].daily_check_procedure_operation_parameters[j].id != null) {
                                                 if (ctx._source.daily_check_procedure_operations[i].daily_check_procedure_operation_parameters[j].id == params.obj.id) {
                                                          if (params.obj.name != null) {
                                                              ctx._source.daily_check_procedure_operations[i].daily_check_procedure_operation_parameters[j].name = params.obj.name;
                                                         }
                                                          if (params.obj.min_value != null) {
                                                              ctx._source.daily_check_procedure_operations[i].daily_check_procedure_operation_parameters[j].min_value = params.obj.min_value;
                                                         }
                                                          if (params.obj.max_value != null) {
                                                              ctx._source.daily_check_procedure_operations[i].daily_check_procedure_operation_parameters[j].max_value = params.obj.max_value;
                                                         }

                                                     }
                                                 }   
                                         }
                                         }   
                             }
                             }
                    """, params={
                            "obj": {
                                "id": obj.id(),
                                "name": obj.name(),
                                "min_value": obj.minValue(),
                                "max_value": obj.maxValue(),
                            }
                        }) \
                    .execute() 
                else:
                    # Create 
                        UpdateByQuery(index=EsDailyCheckProcedure.alias()).using(self._es) \
                            .filter("nested", path="daily_check_procedure_operations", query=Q("term", **{
                                "daily_check_procedure_operations.id": obj.dailyCheckProcedureOperationId()})) \
                            .script(source="""                            
                                    if (ctx._source.daily_check_procedure_operations instanceof List) {
                                        for (int i=ctx._source.daily_check_procedure_operations.length - 1; i >= 0; i--) {
                                            if (ctx._source.daily_check_procedure_operations[i].id == obj.daily_check_procedure_operation_id) {
                                                ctx._source.daily_check_procedure_operations.add(params.obj);
                                            }                        
                                    }
                                    }
                                """, params={
                                "obj": {
                                        "id": obj.id(),
                                        "name": obj.name(),
                                        "min_value": obj.minValue(),
                                        "max_value": obj.maxValue(),
                                },                            
                                "daily_check_procedure_operation_id": obj.dailyCheckProcedureOperationId(),
                            }) \
                        .execute()
