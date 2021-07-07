"""
The file is generated by scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""


import os

from elasticsearch_dsl import UpdateByQuery
from elasticsearch_dsl.connections import connections
from sqlalchemy import create_engine

from src.application.lookup.equipment.MaintenanceProcedureRepository import (
    MaintenanceProcedureRepository as EsMaintenanceProcedureRepository,
)
from src.domain_model.project.maintenance.procedure.MaintenanceProcedure import (
    MaintenanceProcedure,
)
from src.domain_model.project.maintenance.procedure.MaintenanceProcedureRepository import (
    MaintenanceProcedureRepository,
)
from src.domain_model.project.maintenance.procedure.operation.MaintenanceProcedureOperationRepository import (
    MaintenanceProcedureOperationRepository,
)
from src.domain_model.project.maintenance.procedure.operation.parameter.MaintenanceProcedureOperationParameterRepository import (
    MaintenanceProcedureOperationParameterRepository,
)
from src.domain_model.project.unit.UnitRepository import UnitRepository
from src.domain_model.subcontractor.SubcontractorRepository import (
    SubcontractorRepository,
)
from src.port_adapter.repository.es_model.lookup.equipment.Equipment import (
    Equipment as EsEquipment,
)
from src.port_adapter.repository.es_model.lookup.equipment.MaintenanceProcedure import (
    MaintenanceProcedure as EsMaintenanceProcedure,
)
from src.port_adapter.repository.es_model.lookup.equipment.MaintenanceProcedureOperation import (
    MaintenanceProcedureOperation as EsMaintenanceProcedureOperation,
)
from src.port_adapter.repository.es_model.lookup.equipment.MaintenanceProcedureOperationParameter import (
    MaintenanceProcedureOperationParameter as EsMaintenanceProcedureOperationParameter,
)
from src.port_adapter.repository.es_model.lookup.equipment.Subcontractor import (
    Subcontractor as EsSubcontractor,
)
from src.port_adapter.repository.es_model.lookup.equipment.Unit import Unit as EsUnit
from src.resource.common.DateTimeHelper import DateTimeHelper
from src.resource.logging.decorator import debugLogger
from src.resource.logging.logger import logger


class MaintenanceProcedureRepositoryImpl(EsMaintenanceProcedureRepository):
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
                f"[{MaintenanceProcedureRepositoryImpl.__init__.__qualname__}] Could not connect to the db, message: {e}"
            )
            raise Exception(f"Could not connect to the db, message: {e}")

    @debugLogger
    def delete(self, obj: MaintenanceProcedure):
        # We remove it first wherever it exists
        UpdateByQuery(index=EsEquipment.alias()).using(self._es).filter(
            "term", **{"maintenance_procedures.id": obj.id()}
        ).script(
            source="""
                        for (int i=ctx._source.maintenance_procedures.length - 1; i >= 0; i--) {
                            if (ctx._source.maintenance_procedures[i].id == params.id) {
                                ctx._source.maintenance_procedures.remove(i);
                            }
                        }
                        """,
            params={"id": obj.id()},
        ).execute()

    @debugLogger
    def save(self, obj: MaintenanceProcedure):

        # We remove it first wherever it exists
        UpdateByQuery(index=EsEquipment.alias()).using(self._es).filter(
            "term", **{"maintenance_procedures.id": obj.id()}
        ).script(
            source="""
                    for (int i=ctx._source.maintenance_procedures.length - 1; i >= 0; i--) {
                        if (ctx._source.maintenance_procedures[i].id == params.id) {
                            ctx._source.maintenance_procedures.remove(i);
                        }
                    }
                    """,
            params={"id": obj.id()},
        ).execute()

        dataFromRepo = self._collectFromRepo(id=obj.id())
        if dataFromRepo is not None:
            esDoc = EsEquipment.get(
                id=dataFromRepo["maintenance"].equipmentId(), ignore=404
            )
            if esDoc is not None:
                maintenance = dataFromRepo["maintenance"]
                operations = []
                for op in dataFromRepo["operations"][maintenance.id()]:
                    params = []
                    for param in dataFromRepo["params"][op.id()]:
                        params.append(
                            EsMaintenanceProcedureOperationParameter(
                                id=param.id(),
                                name=param.name(),
                                min_value=param.minValue(),
                                max_value=param.maxValue(),
                                unit=EsUnit(
                                    id=dataFromRepo["units"][op.id()].id(),
                                    name=dataFromRepo["units"][op.id()].name(),
                                ),
                            )
                        )
                    operations.append(
                        EsMaintenanceProcedureOperation(
                            id=op.id(),
                            name=op.name(),
                            description=op.description(),
                            type=op.type(),
                            maintenance_procedure_operation_parameters=params,
                        )
                    )
                subcontractor = dataFromRepo["subcontractor"]
                esDoc.maintenance_procedures.append(
                    EsMaintenanceProcedure(
                        id=maintenance.id(),
                        name=maintenance.name(),
                        type=maintenance.type(),
                        frequency=maintenance.frequency(),
                        start_date=DateTimeHelper.intToDateTime(
                            maintenance.startDate()
                        ),
                        sub_type=maintenance.subType(),
                        maintenance_procedure_operations=operations,
                        subcontractor=EsSubcontractor(
                            id=subcontractor.id(),
                            company_name=subcontractor.companyName(),
                        ) if subcontractor is not None else None,
                    )
                )
                esDoc.save()

    def _collectFromRepo(self, id=None):
        if id is None:
            return None
        import src.port_adapter.AppDi as AppDi

        maintenanceRepo = AppDi.instance.get(MaintenanceProcedureRepository)
        operationRepo = AppDi.instance.get(MaintenanceProcedureOperationRepository)
        paramRepo = AppDi.instance.get(MaintenanceProcedureOperationParameterRepository)
        unitRepo = AppDi.instance.get(UnitRepository)
        subcontractorRepo = AppDi.instance.get(SubcontractorRepository)

        maintenance = maintenanceRepo.maintenanceProcedureById(id=id)
        subcontractor = None
        try:
            subcontractor = subcontractorRepo.subcontractorById(
                id=maintenance.subcontractorId()
            )
        except:
            pass

        result = {
            "maintenance": maintenance,
            "operations": {
                id: operationRepo.maintenanceProcedureOperationsByMaintenanceProcedureId(
                    maintenanceProcedureId=id, resultSize=1000000
                )[
                    "items"
                ]
            },
            "params": {},
            "units": {},
            "subcontractor": subcontractor,
        }
        for ops in result["operations"][id]:
            result["params"][
                ops.id()
            ] = paramRepo.maintenanceProcedureOperationParametersByMaintenanceProcedureOperationId(
                maintenanceProcedureOperationId=ops.id(), resultSize=1000000
            )[
                "items"
            ]
            for param in result["params"][ops.id()]:
                result["units"][ops.id()] = unitRepo.unitById(param.unitId())
        return result
