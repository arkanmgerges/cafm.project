"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""



from elasticsearch_dsl import InnerDoc, Keyword, Date, Nested

from src.port_adapter.repository.es_model.lookup.equipment.MaintenanceProcedureOperation import \
    MaintenanceProcedureOperation


class MaintenanceProcedure(InnerDoc):
    id = Keyword()
    name = Keyword()
    type = Keyword()
    frequency = Keyword()
    start_date = Date()
    sub_type = Keyword()
    maintenance_procedure_operations = Nested(MaintenanceProcedureOperation)
