"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

import pytest

from src.domain_model.event.DomainPublishedEvents import DomainPublishedEvents
from src.domain_model.project.maintenance.procedure.operation.MaintenanceProcedureOperation import (
    MaintenanceProcedureOperation,
)


def setup_function(function):
    DomainPublishedEvents.cleanup()


def test_create_object():
    # Act
    obj = _create_object()
    # Assert
    assert isinstance(obj, MaintenanceProcedureOperation)


def test_name():
    # Act
    obj = _create_object()
    # Assert
    assert obj.name() == "name"


def test_description():
    # Act
    obj = _create_object()
    # Assert
    assert obj.description() == "description"


def test_type():
    # Act
    obj = _create_object()
    # Assert
    assert obj.type() == "visual"


def test_maintenance_procedure_id():
    # Act
    obj = _create_object()
    # Assert
    assert obj.maintenanceProcedureId() == "maintenance_procedure_id"


def test_create_from_object():
    # Act
    obj = _create_object()
    obj2 = MaintenanceProcedureOperation.createFromObject(obj=obj)
    # Assert
    assert obj == obj2


def test_toMap():
    # Arrange
    obj = _create_object(
        id="1",
        name="name",
        description="description",
        type="visual",
        maintenanceProcedureId="maintenance_procedure_id",
    )
    currentMap = {
        "maintenance_procedure_operation_id": "1",
        "name": "name",
        "description": "description",
        "type": "visual",
        "maintenance_procedure_id": "maintenance_procedure_id",
    }
    # Act
    objectMap = obj.toMap()

    # Assert
    assert objectMap == currentMap
    assert len(objectMap.keys()) == len(currentMap.keys())


def _create_object(
    id: str = None,
    name: str = None,
    description: str = None,
    type: str = None,
    maintenanceProcedureId: str = None,
    skipValidation: bool = False,
):
    id = "1" if id is None else id
    name = "name" if name is None else name
    description = "description" if description is None else description
    type = "visual" if type is None else type
    maintenanceProcedureId = (
        "maintenance_procedure_id"
        if maintenanceProcedureId is None
        else maintenanceProcedureId
    )

    return MaintenanceProcedureOperation.createFrom(
        id=id,
        name=name,
        description=description,
        type=type,
        maintenanceProcedureId=maintenanceProcedureId,
        skipValidation=skipValidation,
    )
