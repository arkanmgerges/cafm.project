"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import pytest

from src.domain_model.event.DomainPublishedEvents import DomainPublishedEvents
from src.domain_model.resource.exception.InvalidArgumentException import InvalidArgumentException
from src.domain_model.manufacturer.Manufacturer import Manufacturer


def setup_function(function):
    DomainPublishedEvents.cleanup()


def test_create_object():
    # Act
    obj = _create_object()
    # Assert
    assert isinstance(obj, Manufacturer)


def test_name():
    # Act
    obj = _create_object()
    # Assert
    assert obj.name() == 'name-1'


def test_create_from_object():
    # Act
    obj = _create_object()
    obj2 = Manufacturer.createFromObject(obj=obj)
    # Assert
    assert obj == obj2


def test_invalid_name():
    # Act, Assert
    with pytest.raises(InvalidArgumentException):
        Manufacturer.createFrom(name=None)
    with pytest.raises(InvalidArgumentException):
        Manufacturer.createFrom(name='')


def test_toMap():
    # Arrange
    obj = _create_object(id='1', name='name-1')
    currentMap = {'id': '1', 'name': 'name-1'}
    # Act
    objectMap = obj.toMap()

    # Assert
    assert objectMap == currentMap
    assert len(objectMap.keys()) == len(currentMap.keys())


def _create_object(id: str = None, name: str = None, skipValidation: bool = False):
    id = '1' if id is None else id
    name = 'name-1' if name is None else name

    return Manufacturer.createFrom(id=id, name=name, skipValidation=skipValidation)
