"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""



from elasticsearch_dsl import InnerDoc, Keyword, Nested

from src.port_adapter.repository.es_model.lookup.equipment.MaintenanceProcedureOperationParameter import \
    MaintenanceProcedureOperationParameter


class MaintenanceProcedureOperation(InnerDoc):
    id = Keyword()
    name = Keyword()
    description = Keyword()
    type = Keyword()
    maintenance_procedure_operation_parameters = Nested(MaintenanceProcedureOperationParameter)
