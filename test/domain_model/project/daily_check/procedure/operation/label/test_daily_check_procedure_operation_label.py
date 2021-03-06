"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

import pytest

from src.domain_model.event.DomainPublishedEvents import DomainPublishedEvents
from src.domain_model.project.daily_check.procedure.operation.label.DailyCheckProcedureOperationLabel import DailyCheckProcedureOperationLabel


def setup_function(function):
    DomainPublishedEvents.cleanup()


def test_create_object():
    # Act
    obj = _create_object()
    # Assert
    assert isinstance(obj, DailyCheckProcedureOperationLabel)

def test_label():
    # Act
    obj = _create_object()
    # Assert
    assert obj.label() == 'label'
def test_generate_alert():
    # Act
    obj = _create_object()
    # Assert
    assert obj.generateAlert() == 0
def test_daily_check_procedure_operation_id():
    # Act
    obj = _create_object()
    # Assert
    assert obj.dailyCheckProcedureOperationId() == 'daily_check_procedure_operation_id'


def test_create_from_object():
    # Act
    obj = _create_object()
    obj2 = DailyCheckProcedureOperationLabel.createFromObject(obj=obj)
    # Assert
    assert obj == obj2


def test_toMap():
    # Arrange
    obj = _create_object(id='1',
        label = 'label',
        generateAlert = 1,
        dailyCheckProcedureOperationId = 'daily_check_procedure_operation_id',
    )
    currentMap = {'daily_check_procedure_operation_label_id': '1',
        'label': 'label',
        'generate_alert': 1,
        'daily_check_procedure_operation_id': 'daily_check_procedure_operation_id',
    }
    # Act
    objectMap = obj.toMap()

    # Assert
    assert objectMap == currentMap
    assert len(objectMap.keys()) == len(currentMap.keys())


def _create_object(id: str = None, label: str = None, generateAlert: int = 0, dailyCheckProcedureOperationId: str = None, skipValidation: bool = False):
    id = '1' if id is None else id
    label = 'label' if label is None else label
    generateAlert = 1 if generateAlert is None else generateAlert
    dailyCheckProcedureOperationId = 'daily_check_procedure_operation_id' if dailyCheckProcedureOperationId is None else dailyCheckProcedureOperationId

    return DailyCheckProcedureOperationLabel.createFrom(id=id, 
			label=label,
			generateAlert=generateAlert,
			dailyCheckProcedureOperationId=dailyCheckProcedureOperationId, skipValidation=skipValidation)
