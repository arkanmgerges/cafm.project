"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import Any

from src.resource.common.Util import Util


class BaseApplicationService:
    APPLICATION_SERVICE_CLASS = "_application_service_class"

    def _constructObject(self, *args, **kwargs) -> Any:
        appServiceClass = kwargs[BaseApplicationService.APPLICATION_SERVICE_CLASS]
        del kwargs[BaseApplicationService.APPLICATION_SERVICE_CLASS]
        kwargs["skipValidation"] = kwargs["skipValidation"] if "skipValidation" in kwargs else False
        if "token" in kwargs:
            del kwargs["token"]
        if "_sourceObject" in kwargs and kwargs["_sourceObject"] is not None:
            objArgs = {}
            # Get the source object
            _sourceObject = kwargs["_sourceObject"]
            # Get all the key, values of the source object
            sourceObjectAttributes = _sourceObject.toMap()
            # Concatenate the class name with id, e.g. for Unit class it will be unit_id
            lowerCamelClassName = f"{appServiceClass.__qualname__.lower()}_id"
            # Modify all the keys of the source object, and make them lower camel case, and convert snake case class
            # name with id, to be only 'id'.
            # e.g. {'unit_id': 1234, 'name': 'unit_1', 'some_param': 'xyz'} this will be:
            # {'id': 1234, 'name': 'unit_1, 'someParam': 'xyz'}
            modifiedSourceAttributes = dict(
                ("id" if k == lowerCamelClassName else Util.snakeCaseToLowerCameCaseString(k), v)
                for k, v in sourceObjectAttributes.items()
            )
            # Loop through the modified items and prepare new dictionary with default values from source object, and
            # use the values from kwargs only if they exist
            for k, v in modifiedSourceAttributes.items():
                objArgs[k] = kwargs[k] if k in kwargs and kwargs[k] is not None else getattr(_sourceObject, k)()
            del kwargs["_sourceObject"]
            # Create the object with the new key, value pairs
            return appServiceClass.createFrom(**kwargs)
        else:
            return appServiceClass.createFrom(**kwargs)
