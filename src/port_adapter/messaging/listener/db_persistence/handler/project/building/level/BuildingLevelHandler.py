"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import json
from typing import List, Callable

from src.domain_model.event.EventConstant import CommonEventConstant
from src.domain_model.project.building.Building import Building
from src.domain_model.project.building.BuildingRepository import BuildingRepository
from src.domain_model.project.building.level.BuildingLevel import BuildingLevel
from src.domain_model.project.building.level.BuildingLevelRepository import BuildingLevelRepository
from src.domain_model.project.building.level.room.BuildingLevelRoom import BuildingLevelRoom
from src.port_adapter.messaging.listener.common.handler.Handler import Handler
from src.port_adapter.messaging.listener.db_persistence.handler.common.Util import Util
from src.resource.logging.logger import logger


class BuildingLevelHandler(Handler):
    def __init__(self):
        import src.port_adapter.AppDi as AppDi
        self._eventConstants = [
            CommonEventConstant.BUILDING_LEVEL_TO_BUILDING_LINKED.value,
            CommonEventConstant.BUILDING_LEVEL_TO_BUILDING_UNLINKED.value,
            CommonEventConstant.BUILDING_LEVEL_ROOM_TO_BUILDING_LEVEL_ADDED.value,
            CommonEventConstant.BUILDING_LEVEL_ROOM_FROM_BUILDING_LEVEL_REMOVED.value,
            CommonEventConstant.BUILDING_LEVEL_UPDATED.value,
            CommonEventConstant.BUILDING_LEVEL_DELETED.value,
        ]
        self._repository: BuildingLevelRepository = AppDi.instance.get(BuildingLevelRepository)
        self._buildingRepository: BuildingRepository = AppDi.instance.get(BuildingRepository)

    def canHandle(self, name: str) -> bool:
        return name in self._eventConstants

    def handleCommand(self, messageData: dict):
        name = messageData['name']
        data = messageData['data']
        metadata = messageData['metadata']

        logger.debug(
            f'[{BuildingLevelHandler.handleCommand.__qualname__}] - received args:\ntype(name): {type(name)}, name: {name}\ntype(data): {type(data)}, data: {data}\ntype(metadata): {type(metadata)}, metadata: {metadata}')
        dataDict = json.loads(data)
        # metadataDict = json.loads(metadata)
        #
        # if 'token' not in metadataDict:
        #     raise UnAuthorizedException()

        result = self.execute(name, **dataDict)
        return {'data': result, 'metadata': metadata}

    def execute(self, event, *args, **kwargs):
        funcSwitcher = {
            CommonEventConstant.BUILDING_LEVEL_ROOM_TO_BUILDING_LEVEL_ADDED.value: self._addBuildingLevelRoomToBuildingLevel,
            CommonEventConstant.BUILDING_LEVEL_ROOM_FROM_BUILDING_LEVEL_REMOVED.value: self._removeBuildingLevelRoomFromBuildingLevel,
            CommonEventConstant.BUILDING_LEVEL_TO_BUILDING_LINKED.value: self._linkBuildingLevelToBuilding,
            CommonEventConstant.BUILDING_LEVEL_TO_BUILDING_UNLINKED.value: self._unlinkBuildingLevelFromBuilding,
            CommonEventConstant.BUILDING_LEVEL_UPDATED.value: self._save,
            CommonEventConstant.BUILDING_LEVEL_DELETED.value: self._delete,
        }

        argSwitcher = {
            CommonEventConstant.BUILDING_LEVEL_TO_BUILDING_LINKED.value: lambda: {
                'buildingId': kwargs['building_id'],
                'buildingLevelId': kwargs['building_level']['id']},
            CommonEventConstant.BUILDING_LEVEL_TO_BUILDING_UNLINKED.value: lambda: {
                'buildingId': kwargs['building_id'],
                'buildingLevelId': kwargs['building_level']['id']},
            CommonEventConstant.BUILDING_LEVEL_ROOM_TO_BUILDING_LEVEL_ADDED.value: lambda: {
                'buildingLevelRoom': BuildingLevelRoom.createFrom(
                    **Util.snakeCaseToLowerCameCaseDict(self._removeInnerData(kwargs['building_level_room']))),
                'buildingLevel': self._repository.buildingLevelById(kwargs['building_level']['id'])},
            CommonEventConstant.BUILDING_LEVEL_ROOM_FROM_BUILDING_LEVEL_REMOVED.value: lambda: {
                'buildingLevelRoom': BuildingLevelRoom.createFrom(id=kwargs['building_level_room']['id'], buildingLevelId=kwargs['building_level']['id']),
                'buildingLevel': BuildingLevel.createFrom(id=kwargs['building_level']['id'])},
            CommonEventConstant.BUILDING_LEVEL_UPDATED.value: lambda: {
                'obj': BuildingLevel.createFrom(
                    **Util.snakeCaseToLowerCameCaseDict(self._removeInnerData(kwargs['new'])))},
            CommonEventConstant.BUILDING_LEVEL_DELETED.value: lambda: {
                'obj': BuildingLevel.createFrom(**Util.snakeCaseToLowerCameCaseDict(kwargs))},
        }
        func = funcSwitcher.get(event, None)
        if func is not None:
            # Execute the function with the arguments
            return func(*args, **(argSwitcher.get(event))())
        return None

    def _removeInnerData(self, argDict) -> dict:
        if 'rooms' in argDict:
            del argDict['rooms']
        if 'building_ids' in argDict:
            del argDict['building_ids']
        return argDict

    def _linkBuildingLevelToBuilding(self, buildingLevelId, buildingId):
        building: Building = self._buildingRepository.buildingById(id=buildingId)
        buildingLevel: BuildingLevel = BuildingLevel.createFrom(id=buildingLevelId)
        self._repository.linkBuildingLevelToBuilding(buildingLevel=buildingLevel, building=building)
        return {'building_level_id': buildingLevelId, 'building_id': buildingId}

    def _unlinkBuildingLevelFromBuilding(self, buildingLevelId, buildingId):
        building: Building = self._buildingRepository.buildingById(id=buildingId)
        buildingLevel: BuildingLevel = BuildingLevel.createFrom(id=buildingLevelId)
        self._repository.unlinkBuildingLevelFromBuilding(buildingLevel=buildingLevel, building=building)
        return {'building_level_id': buildingLevelId, 'building_id': buildingId}

    def _removeBuildingLevelRoomFromBuildingLevel(self, buildingLevelRoom, buildingLevel):
        self._repository.removeBuildingLevelRoomFromBuildingLevel(buildingLevelRoom=buildingLevelRoom, buildingLevel=buildingLevel)
        return {'id': buildingLevelRoom.id()}

    def _addBuildingLevelRoomToBuildingLevel(self, buildingLevelRoom, buildingLevel):
        self._repository.addBuildingLevelRoomToBuildingLevel(buildingLevelRoom=buildingLevelRoom, buildingLevel=buildingLevel)
        return buildingLevelRoom.toMap()

    def _save(self, *_args, obj: BuildingLevel):
        self._repository.save(obj=obj)
        return obj.toMap(excludeInnerData=True)

    def _delete(self, *_args, obj: BuildingLevel):
        self._repository.deleteBuildingLevel(obj=obj)
        return obj.toMap(excludeInnerData=True)

    @staticmethod
    def targetsOnSuccess() -> List[Callable]:
        return [Handler.targetOnSuccess]
