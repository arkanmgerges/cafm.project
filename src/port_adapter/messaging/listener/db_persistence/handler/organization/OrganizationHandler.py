"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import json
from typing import Callable, List

from src.domain_model.event.EventConstant import CommonEventConstant
from src.domain_model.organization.Organization import Organization
from src.domain_model.organization.OrganizationRepository import OrganizationRepository
from src.port_adapter.messaging.listener.common.handler.Handler import Handler
from src.port_adapter.messaging.listener.db_persistence.handler.common.Util import Util
from src.resource.logging.logger import logger


class OrganizationHandler(Handler):
    def __init__(self):
        import src.port_adapter.AppDi as AppDi
        self._eventConstants = [
            CommonEventConstant.ORGANIZATION_CREATED.value,
            CommonEventConstant.ORGANIZATION_UPDATED.value,
            CommonEventConstant.ORGANIZATION_DELETED.value,
        ]
        self._repository: OrganizationRepository = AppDi.instance.get(OrganizationRepository)

    def canHandle(self, name: str) -> bool:
        return name in self._eventConstants

    def handleCommand(self, messageData: dict):
        name = messageData['name']
        data = messageData['data']
        metadata = messageData['metadata']

        logger.debug(
            f'[{OrganizationHandler.handleCommand.__qualname__}] - received args:\ntype(name): {type(name)}, name: {name}\ntype(data): {type(data)}, data: {data}\ntype(metadata): {type(metadata)}, metadata: {metadata}')
        dataDict = json.loads(data)
        # metadataDict = json.loads(metadata)
        #
        # if 'token' not in metadataDict:
        #     raise UnAuthorizedException()

        result = self.execute(name, **dataDict)
        return {'data': result, 'metadata': metadata}

    def execute(self, event, *args, **kwargs):
        funcSwitcher = {
            CommonEventConstant.ORGANIZATION_CREATED.value: self._save,
            CommonEventConstant.ORGANIZATION_UPDATED.value: self._save,
            CommonEventConstant.ORGANIZATION_DELETED.value: self._delete,
        }

        argSwitcher = {
            CommonEventConstant.ORGANIZATION_CREATED.value: lambda: {
                'obj': Organization.createFrom(**Util.snakeCaseToLowerCameCaseDict(kwargs))},
            CommonEventConstant.ORGANIZATION_UPDATED.value: lambda: {
                'obj': Organization.createFrom(**Util.snakeCaseToLowerCameCaseDict(kwargs['new']))},
            CommonEventConstant.ORGANIZATION_DELETED.value: lambda: {
                'obj': Organization.createFrom(**Util.snakeCaseToLowerCameCaseDict(kwargs))},
        }
        func = funcSwitcher.get(event, None)
        if func is not None:
            # Execute the function with the arguments
            return func(*args, **(argSwitcher.get(event))())
        return None

    def _save(self, *_args, obj: Organization):
        self._repository.save(obj=obj)
        return obj.toMap()

    def _delete(self, *_args, obj: Organization):
        self._repository.deleteOrganization(obj=obj)
        return obj.toMap()

    @staticmethod
    def targetsOnSuccess() -> List[Callable]:
        return [Handler.targetOnSuccess]
