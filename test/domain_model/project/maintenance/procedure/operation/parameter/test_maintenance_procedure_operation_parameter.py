"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

import pytest

from src.domain_model.event.DomainPublishedEvents import DomainPublishedEvents
from src.domain_model.project.maintenance.procedure.operation.parameter.MaintenanceProcedureOperationParameter import MaintenanceProcedureOperationParameter


def setup_function(function):
    DomainPublishedEvents.cleanup()


def test_create_object():
    # Act
    obj = _create_object()
    # Assert
    assert isinstance(obj, MaintenanceProcedureOperationParameter)

def test_name():
    # Act
    obj = _create_object()
    # Assert
    assert obj.name() == 'name'
def test_unit_id():
    # Act
    obj = _create_object()
    # Assert
    assert obj.unitId() == 'unit_id'
def test_maintenance_procedure_operation_id():
    # Act
    obj = _create_object()
    # Assert
    assert obj.maintenanceProcedureOperationId() == 'maintenance_procedure_operation_id'
def test_min_value():
    # Act
    obj = _create_object()
    # Assert
    assert obj.minValue() == 1
def test_max_value():
    # Act
    obj = _create_object()
    # Assert
    assert obj.maxValue() == 2


def test_create_from_object():
    # Act
    obj = _create_object()
    obj2 = MaintenanceProcedureOperationParameter.createFromObject(obj=obj)
    # Assert
    assert obj == obj2


def test_toMap():
    # Arrange
    obj = _create_object(id='1',
        name = 'name',
        unitId = 'unit_id',
        maintenanceProcedureOperationId = 'maintenance_procedure_operation_id',
        minValue = 1,
        maxValue = 2,
    )
    currentMap = {'id': '1',
        'name': 'name',
        'unit_id': 'unit_id',
        'maintenance_procedure_operation_id': 'maintenance_procedure_operation_id',
        'min_value': 1,
        'max_value': 2,
    }
    # Act
    objectMap = obj.toMap()

    # Assert
    assert objectMap == currentMap
    assert len(objectMap.keys()) == len(currentMap.keys())


def _create_object(id: str = None, name: str = None, unitId: str = None, maintenanceProcedureOperationId: str = None, minValue: float = None, maxValue: float = None, skipValidation: bool = False):
    id = '1' if id is None else id
    name = 'name' if name is None else name
    unitId = 'unit_id' if unitId is None else unitId
    maintenanceProcedureOperationId = 'maintenance_procedure_operation_id' if maintenanceProcedureOperationId is None else maintenanceProcedureOperationId
    minValue = 1 if minValue is None else minValue
    maxValue = 2 if maxValue is None else maxValue

    return MaintenanceProcedureOperationParameter.createFrom(id=id, name=name, unitId=unitId, maintenanceProcedureOperationId=maintenanceProcedureOperationId, minValue=minValue, maxValue=maxValue, skipValidation=skipValidation)
