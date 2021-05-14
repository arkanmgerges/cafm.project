"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import Any


class BaseApplicationService:
    APPLICATION_SERVICE_CLASS = '_application_service_class'

    def _constructObject(self, *args, **kwargs) -> Any:
        appServiceClass = kwargs[BaseApplicationService.APPLICATION_SERVICE_CLASS]
        del kwargs[BaseApplicationService.APPLICATION_SERVICE_CLASS]
        kwargs["skipValidation"] = kwargs["skipValidation"] if "skipValidation" in kwargs else False
        if "token" in kwargs:
            del kwargs["token"]
        if "_sourceObject" in kwargs and kwargs["_sourceObject"] is not None:
            objArgs = {}
            for k, v in kwargs.items():
                objArgs[k] = kwargs[k] if kwargs[k] is not None else getattr(kwargs["_sourceObject"], k)()
            del kwargs["_sourceObject"]
            return appServiceClass.createFrom(**kwargs)
        else:
            return appServiceClass.createFrom(**kwargs)
