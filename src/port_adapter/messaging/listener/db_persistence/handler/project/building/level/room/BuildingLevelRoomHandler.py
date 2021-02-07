"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import json
from typing import List, Callable

from src.domain_model.event.EventConstant import CommonEventConstant
from src.domain_model.project.building.level.room.BuildingLevelRoom import BuildingLevelRoom
from src.domain_model.project.building.level.room.BuildingLevelRoomRepository import BuildingLevelRoomRepository
from src.port_adapter.messaging.listener.common.handler.Handler import Handler
from src.port_adapter.messaging.listener.db_persistence.handler.common.Util import Util
from src.resource.logging.logger import logger


class BuildingLevelRoomHandler(Handler):
    def __init__(self):
        import src.port_adapter.AppDi as AppDi
        self._eventConstants = [
            CommonEventConstant.BUILDING_LEVEL_ROOM_CREATED.value,
            CommonEventConstant.BUILDING_LEVEL_ROOM_UPDATED.value,
            CommonEventConstant.BUILDING_LEVEL_ROOM_DELETED.value,
        ]
        self._repository: BuildingLevelRoomRepository = AppDi.instance.get(BuildingLevelRoomRepository)

    def canHandle(self, name: str) -> bool:
        return name in self._eventConstants

    def handleCommand(self, messageData: dict):
        name = messageData['name']
        data = messageData['data']
        metadata = messageData['metadata']

        logger.debug(
            f'[{BuildingLevelRoomHandler.handleCommand.__qualname__}] - received args:\ntype(name): {type(name)}, name: {name}\ntype(data): {type(data)}, data: {data}\ntype(metadata): {type(metadata)}, metadata: {metadata}')
        dataDict = json.loads(data)
        # metadataDict = json.loads(metadata)
        #
        # if 'token' not in metadataDict:
        #     raise UnAuthorizedException()

        result = self.execute(name, **dataDict)
        return {'data': result, 'metadata': metadata}

    def execute(self, event, *args, **kwargs):
        funcSwitcher = {
            CommonEventConstant.BUILDING_LEVEL_ROOM_CREATED.value: self._save,
            CommonEventConstant.BUILDING_LEVEL_ROOM_UPDATED.value: self._save,
            CommonEventConstant.BUILDING_LEVEL_ROOM_DELETED.value: self._delete,
        }

        argSwitcher = {
            CommonEventConstant.BUILDING_LEVEL_ROOM_CREATED.value: lambda: {
                'obj': BuildingLevelRoom.createFrom(**Util.snakeCaseToLowerCameCaseDict(kwargs))},
            CommonEventConstant.BUILDING_LEVEL_ROOM_UPDATED.value: lambda: {
                'obj': BuildingLevelRoom.createFrom(**Util.snakeCaseToLowerCameCaseDict(self._removeInnerKeys(kwargs['new'])))},
            CommonEventConstant.BUILDING_LEVEL_ROOM_DELETED.value: lambda: {
                'obj': BuildingLevelRoom.createFrom(**Util.snakeCaseToLowerCameCaseDict(kwargs))},
        }
        func = funcSwitcher.get(event, None)
        if func is not None:
            # Execute the function with the arguments
            return func(*args, **(argSwitcher.get(event))())
        return None

    def _removeInnerKeys(self, argDict) -> dict:
        if 'rooms' in argDict:
            del argDict['rooms']
        return argDict

    def _save(self, *_args, obj: BuildingLevelRoom):
        self._repository.save(obj=obj)
        return self._removeInnerKeys(obj.toMap())

    def _delete(self, *_args, obj: BuildingLevelRoom):
        self._repository.deleteBuildingLevelRoom(obj=obj)
        return self._removeInnerKeys(obj.toMap())

    @staticmethod
    def targetsOnSuccess() -> List[Callable]:
        return [Handler.targetOnSuccess]