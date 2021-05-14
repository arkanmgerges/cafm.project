"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import Any, Callable

from src.application.model.BaseApplicationServiceModelData import BaseApplicationServiceModelData
from src.application.model.BaseApplicationServiceBulkData import BaseApplicationServiceBulkData
from src.domain_model.resource.exception.DomainModelException import DomainModelException
from src.domain_model.resource.exception.ProcessBulkDomainException import ProcessBulkDomainException
from src.domain_model.token.TokenService import TokenService
from src.domain_model.util.DomainModelAttributeValidator import DomainModelAttributeValidator
from src.resource.common.Util import Util


class BaseApplicationService:
    APPLICATION_SERVICE_CLASS = "_application_service_class"

    def _constructObject(self, *args, **kwargs) -> Any:
        appServiceClass = kwargs[BaseApplicationService.APPLICATION_SERVICE_CLASS]
        del kwargs[BaseApplicationService.APPLICATION_SERVICE_CLASS]
        if "token" in kwargs:
            del kwargs["token"]
        if "_sourceObject" in kwargs and kwargs["_sourceObject"] is not None:
            kwargs["skipValidation"] = True
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
            kwargs["skipValidation"] = kwargs["skipValidation"] if "skipValidation" in kwargs else False
            return appServiceClass.createFrom(**kwargs)


    def _bulkCreate(self, baseBulkData: BaseApplicationServiceBulkData):
        objList = []
        exceptions = []
        for objListParamsItem in baseBulkData.objListParams:
            try:
                DomainModelAttributeValidator.validate(
                    domainModelObject=self._constructObject(skipValidation=True), attributeDictionary=objListParamsItem
                )
                objList.append(
                    self._constructObject(
                        **Util.snakeCaseToLowerCameCaseDict(
                            objListParamsItem, keyReplacements=[{"source": baseBulkData.sourceId, "target": "id"}]
                        )
                    )
                )
            except DomainModelException as e:
                exceptions.append({"reason": {"message": e.message, "code": e.code}})
        _tokenData = TokenService.tokenDataFromToken(token=baseBulkData.token)
        try:
            baseBulkData.domainService.bulkCreate(objList=objList)
            if len(exceptions) > 0:
                raise ProcessBulkDomainException(messages=exceptions)
        except DomainModelException as e:
            exceptions.append({"reason": {"message": e.message, "code": e.code}})
            raise ProcessBulkDomainException(messages=exceptions)

    def _bulkDelete(self, baseBulkData: BaseApplicationServiceBulkData):
        objList = []
        exceptions = []
        for objListParamsItem in baseBulkData.objListParams:
            try:
                DomainModelAttributeValidator.validate(
                    domainModelObject=self._constructObject(skipValidation=True), attributeDictionary=objListParamsItem
                )
                objList.append(
                    self._constructObject(id=objListParamsItem[baseBulkData.sourceId], skipValidation=True)
                )
            except DomainModelException as e:
                exceptions.append({"reason": {"message": e.message, "code": e.code}})
        _tokenData = TokenService.tokenDataFromToken(token=baseBulkData.token)
        try:
            baseBulkData.domainService.bulkDelete(objList=objList)
            if len(exceptions) > 0:
                raise ProcessBulkDomainException(messages=exceptions)
        except DomainModelException as e:
            exceptions.append({"reason": {"message": e.message, "code": e.code}})
            raise ProcessBulkDomainException(messages=exceptions)

    def _bulkUpdate(self, baseBulkData: BaseApplicationServiceBulkData):
        objList = []
        exceptions = []
        for objListParamsItem in baseBulkData.objListParams:
            try:
                DomainModelAttributeValidator.validate(
                    domainModelObject=self._constructObject(skipValidation=True), attributeDictionary=objListParamsItem
                )
                oldObject = baseBulkData.repositoryCallbackFunction(
                    id=objListParamsItem[baseBulkData.sourceId]
                )
                newObject = self._constructObject(
                    **Util.snakeCaseToLowerCameCaseDict(
                        objListParamsItem, keyReplacements=[{"source": baseBulkData.sourceId, "target": "id"}]
                    ),
                    _sourceObject=oldObject,
                )
                objList.append(
                    (newObject, oldObject),
                )
            except DomainModelException as e:
                exceptions.append({"reason": {"message": e.message, "code": e.code}})
        _tokenData = TokenService.tokenDataFromToken(token=baseBulkData.token)
        try:
            baseBulkData.domainService.bulkUpdate(objList=objList)
            if len(exceptions) > 0:
                raise ProcessBulkDomainException(messages=exceptions)
        except DomainModelException as e:
            exceptions.append({"reason": {"message": e.message, "code": e.code}})
            raise ProcessBulkDomainException(messages=exceptions)

    # Both the callFunction and this return value, because some function can change state but return feedback
    # code. And the naming is to express the intention of the function
    def callGetterFunction(self, modelData: BaseApplicationServiceModelData):
        return modelData.getterFunction(*modelData.args, **modelData.kwargs)

    # Both the callGetterFunction and this return value, because some function can change state but return feedback
    # code. And the naming is to express the intention of the function
    def callFunction(self, modelData: BaseApplicationServiceModelData):
        return modelData.function(*modelData.args, **modelData.kwargs)
