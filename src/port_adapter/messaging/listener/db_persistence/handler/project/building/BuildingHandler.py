"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import json
from typing import List, Callable

from src.domain_model.event.EventConstant import CommonEventConstant
from src.domain_model.project.building.Building import Building
from src.domain_model.project.building.BuildingRepository import BuildingRepository
from src.port_adapter.messaging.listener.common.handler.Handler import Handler
from src.port_adapter.messaging.listener.db_persistence.handler.common.Util import Util
from src.resource.logging.logger import logger


class BuildingHandler(Handler):
    def __init__(self):
        import src.port_adapter.AppDi as AppDi
        self._eventConstants = [
            CommonEventConstant.BUILDING_CREATED.value,
            CommonEventConstant.BUILDING_UPDATED.value,
            CommonEventConstant.BUILDING_DELETED.value,
        ]
        self._repository: BuildingRepository = AppDi.instance.get(BuildingRepository)

    def canHandle(self, name: str) -> bool:
        return name in self._eventConstants

    def handleCommand(self, messageData: dict):
        name = messageData['name']
        data = messageData['data']
        metadata = messageData['metadata']

        logger.debug(
            f'[{BuildingHandler.handleCommand.__qualname__}] - received args:\ntype(name): {type(name)}, name: {name}\ntype(data): {type(data)}, data: {data}\ntype(metadata): {type(metadata)}, metadata: {metadata}')
        dataDict = json.loads(data)
        # metadataDict = json.loads(metadata)
        #
        # if 'token' not in metadataDict:
        #     raise UnAuthorizedException()

        result = self.execute(name, **dataDict)
        return {'data': result, 'metadata': metadata}

    def execute(self, event, *args, **kwargs):
        funcSwitcher = {
            CommonEventConstant.BUILDING_CREATED.value: self._save,
            CommonEventConstant.BUILDING_UPDATED.value: self._save,
            CommonEventConstant.BUILDING_DELETED.value: self._delete,
        }

        argSwitcher = {
            CommonEventConstant.BUILDING_CREATED.value: lambda: {
                'obj': Building.createFrom(**Util.snakeCaseToLowerCameCaseDict(kwargs))},
            CommonEventConstant.BUILDING_UPDATED.value: lambda: {
                'obj': Building.createFrom(**Util.snakeCaseToLowerCameCaseDict(self._removeInnerKeys(kwargs['new'])))},
            CommonEventConstant.BUILDING_DELETED.value: lambda: {
                'obj': Building.createFrom(**Util.snakeCaseToLowerCameCaseDict(kwargs))},
        }
        func = funcSwitcher.get(event, None)
        if func is not None:
            # Execute the function with the arguments
            return func(*args, **(argSwitcher.get(event))())
        return None

    def _removeInnerKeys(self, argDict) -> dict:
        if 'building_levels' in argDict:
            del argDict['building_levels']
        return argDict

    def _save(self, *_args, obj: Building):
        self._repository.save(obj=obj)
        return self._removeInnerKeys(obj.toMap())

    def _delete(self, *_args, obj: Building):
        self._repository.deleteBuilding(obj=obj)
        return self._removeInnerKeys(obj.toMap())

    @staticmethod
    def targetsOnSuccess() -> List[Callable]:
        return [Handler.targetOnSuccess]
