"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import os
import sys
from uuid import uuid4


sys.path.append("../../../")
from src.port_adapter.repository.db_model.StandardEquipmentProjectCategory import StandardEquipmentProjectCategory
from src.port_adapter.repository.db_model.StandardEquipmentCategoryGroup import StandardEquipmentCategoryGroup
from src.port_adapter.repository.db_model.StandardEquipmentCategory import StandardEquipmentCategory
from src.port_adapter.repository.db_model.StandardMaintenanceProcedure import StandardMaintenanceProcedure
from src.port_adapter.repository.db_model.StandardMaintenanceProcedureOperation import StandardMaintenanceProcedureOperation
from src.port_adapter.repository.db_model.StandardMaintenanceProcedureOperationParameter import StandardMaintenanceProcedureOperationParameter
from src.port_adapter.repository.db_model.StandardMaintenanceProcedureOperationLabel import StandardMaintenanceProcedureOperationLabel

from src.port_adapter.repository.db_model.Unit import Unit



import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import walk


def idByString(string: str) -> str:
    import hashlib
    import uuid
    return str(uuid.UUID(hashlib.md5(string.encode()).hexdigest()))

@click.group()
def cli():
    pass

@cli.command(help="Add std eq prj cat groups and associated values")
def add_standard_eq_project_category_group_and_associated_values():
    engine = create_engine(
        f"mysql+mysqlconnector://{os.getenv('CAFM_PROJECT_DB_USER', 'root')}:{os.getenv('CAFM_PROJECT_DB_PASSWORD', '1234')}@{os.getenv('CAFM_PROJECT_DB_HOST', '127.0.0.1')}/{os.getenv('CAFM_PROJECT_DB_NAME', 'cafm-project')}"
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    import json

    currentDir = os.path.dirname(os.path.realpath(__file__))
    baseProjectCategoryUUID = 'f1f9d810-81df-4ea4-81f9-1f3658761407'
    unitBaseUUID = '0f36caba-f236-416a-ab92-4585d69e044e'

    with open(
            f"{currentDir}/../cafm_sample_data/units/units.json", newline=""
        ) as jsonFile:
            data = json.load(jsonFile)
            for unitIndex, unit in enumerate(data["units"]):
                unitId = idByString(unitBaseUUID + "unit" + unit["name"])
                dbObject = session.query(Unit).filter_by(id=unitId).first()
                if dbObject is None:
                    session.add(Unit(
                        id=unitId,
                        name=unit["name"],
                    ))

    filenames = next(walk(f"{currentDir}/../cafm_sample_data/standard_procedures"), (None, None, []))[2]  # [] if no file

    for filename in filenames:
        with open(
            f"{currentDir}/../cafm_sample_data/standard_procedures/{filename}", newline=""
        ) as jsonFile:
            data = json.load(jsonFile)
            baseUUID = data["base_uuid"]
            category = data["category"]
            groupName = data["group_name"]
            projectCategoryId = idByString(baseProjectCategoryUUID + "projectCategoryId" + category)
            categoryId = idByString(baseProjectCategoryUUID + "categoryId" + category)

            #create standard equipment project category
            dbObject = session.query(StandardEquipmentProjectCategory).filter_by(id=projectCategoryId).first()
            if dbObject is None:
                session.add(StandardEquipmentProjectCategory(
                    id=projectCategoryId,
                    name=category,
                    organizationId='1' #missing in json
                ))

            #create standard equipment category
            dbObject = session.query(StandardEquipmentCategory).filter_by(id=categoryId).first()
            if dbObject is None:
                session.add(StandardEquipmentCategory(
                    id=categoryId,
                    name=category,
                ))

            #create standard equipment category group
            equipmentCategoryGroupId = idByString(baseUUID + groupName)
            dbObject = session.query(StandardEquipmentCategoryGroup).filter_by(id=equipmentCategoryGroupId).first()
            if dbObject is None:
                session.add(StandardEquipmentCategoryGroup(
                    id=equipmentCategoryGroupId,
                    name=groupName,
                    standardEquipmentCategoryId=categoryId
                ))

            procedures = data["procedures"]
            for procedureIndex, procedure in enumerate(procedures):
                procedureFrequency = procedure["frequency"]
                procedureType = procedure["type"]
                procedureSubtype = procedure["subtype"]
                procedureName = procedure["name"]
                operations = procedure["operations"]

                procedureId = idByString(baseUUID + "procedure" + str(procedureIndex))
                dbObject = session.query(StandardMaintenanceProcedure).filter_by(id=procedureId).first()
                if dbObject is None:
                    session.add(StandardMaintenanceProcedure(
                        id=procedureId,
                        name=procedureName,
                        type=procedureType,
                        subType=procedureSubtype,
                        frequency=procedureFrequency,
                        standardEquipmentCategoryGroupId=equipmentCategoryGroupId,
                        # startDate= Column("start_date", DateTime) #missing in json
                        # organizationId= Column("organization_id", String(40)) #missing in json
                    ))

                for operationIndex, operation in enumerate(operations):
                    operationType = operation["type"]
                    operationDescription = operation["description"]
                    operationName = operation["name"]

                    operationId = idByString(baseUUID + "operation" + str(procedureIndex) + str(operationIndex))
                    dbObject = session.query(StandardMaintenanceProcedureOperation).filter_by(id=operationId).first()
                    if dbObject is None:
                        session.add(StandardMaintenanceProcedureOperation(
                           id=operationId,
                           name=operationName,
                           description=operationDescription,
                           type=operationType,
                           standardMaintenanceProcedureId=procedureId
                        ))

                    if operationType == "visual":
                        labels = operation["labels"]
                        for labelIndex, label in enumerate(labels):
                            labelLabel = label["label"]
                            labelGenerateAlert = label["generates_alert"]

                            labelId = idByString(baseUUID + "label" + str(procedureIndex) + str(operationIndex) + str(labelIndex))
                            dbObject = session.query(StandardMaintenanceProcedureOperationLabel).filter_by(id=labelId).first()
                            if dbObject is None:
                                session.add(StandardMaintenanceProcedureOperationLabel(
                                    id=labelId,
                                    label=labelLabel,
                                    generateAlert=labelGenerateAlert,
                                    standardMaintenanceProcedureOperationId=operationId,
                                ))

                    if operationType == "parameter":
                        parameters = operation["parameters"]
                        for parameterIndex, parameter in enumerate(parameters):
                            parameterDescription = parameter["description"]
                            parameterUnit = parameter["unit"]

                            parameterId = idByString(baseUUID + "parameter" + str(procedureIndex) + str(operationIndex) + str(parameterIndex))
                            dbObject = session.query(StandardMaintenanceProcedureOperationParameter).filter_by(id=parameterId).first()
                            if dbObject is None:
                                session.add(StandardMaintenanceProcedureOperationParameter(
                                    id=parameterId,
                                    name=parameterDescription,
                                    unitId=idByString(unitBaseUUID + "unit" + parameterUnit),
                                    standardMaintenanceProcedureOperationId=operationId,
                                    minValue=0,#missing in json
                                    maxValue=100 #missing in json
                                ))
    session.commit()
    session.close()

if __name__ == "__main__":
    cli()
