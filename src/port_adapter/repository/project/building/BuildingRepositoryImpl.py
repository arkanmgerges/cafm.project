"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from sqlalchemy import desc
from sqlalchemy.inspection import inspect

from src.application.lifecycle.ApplicationServiceLifeCycle import ApplicationServiceLifeCycle
from src.domain_model.project.building.Building import Building
from src.domain_model.project.building.BuildingRepository import BuildingRepository
from src.domain_model.project.building.level.BuildingLevel import BuildingLevel
from src.domain_model.project.building.level.BuildingLevelRepository import (
    BuildingLevelRepository,
)
from src.domain_model.project.building.level.room.BuildingLevelRoom import (
    BuildingLevelRoom,
)
from src.domain_model.resource.exception.BuildingDoesNotExistException import (
    BuildingDoesNotExistException,
)
from src.domain_model.token.TokenData import TokenData
from src.port_adapter.repository.common.DbUtil import DbUtil
from src.port_adapter.repository.db_model.Building import Building as DbBuilding
from src.port_adapter.repository.db_model.BuildingLevel import (
    BuildingLevel as DbBuildingLevel,
)
from src.port_adapter.repository.db_model.BuildingLevelRoom import (
    BuildingLevelRoom as DbBuildingLevelRoom,
)
from src.resource.logging.decorator import debugLogger


class BuildingRepositoryImpl(BuildingRepository):
    def __init__(self):
        import src.port_adapter.AppDi as AppDi

        self._buildingLevelRepo: BuildingLevelRepository = AppDi.instance.get(
            BuildingLevelRepository
        )
        self._dbBuildingColumnsMapping = inspect(DbBuilding).c
        self._dbBuildingLevelColumnsMapping = inspect(DbBuildingLevel).c
        self._dbBuildingLevelRoomColumnsMapping = inspect(DbBuildingLevelRoom).c

    @debugLogger
    def addLevelToBuilding(
        self,
        buildingLevel: BuildingLevel,
        building: Building,
        tokenData: TokenData = None,
    ):
        self._buildingLevelRepo.save(obj=buildingLevel)
        dbSession = ApplicationServiceLifeCycle.dbContext()
        dbObject = (
            dbSession.query(DbBuildingLevel)
            .filter_by(id=buildingLevel.id())
            .first()
        )
        buildingHasLevel = False
        for dbBuilding in dbObject.buildings:
            if dbBuilding.id == building.id():
                buildingHasLevel = True
                break

        if not buildingHasLevel:
            dbBuilding = (
                dbSession.query(DbBuilding).filter_by(id=building.id()).first()
            )
            dbObject.buildings.append(dbBuilding)
            dbSession.add(dbObject)
    

    @debugLogger
    def removeLevelFromBuilding(
        self,
        buildingLevel: BuildingLevel,
        building: Building,
        tokenData: TokenData = None,
    ):
        dbSession = ApplicationServiceLifeCycle.dbContext()
        dbObject = (
            dbSession.query(DbBuildingLevel)
            .filter_by(id=buildingLevel.id())
            .first()
        )
        buildingHasLevel = False
        for dbBuilding in dbObject.buildings:
            if dbBuilding.id == building.id():
                buildingHasLevel = True
                break

        if buildingHasLevel:
            dbSession.delete(dbObject)
    

    @debugLogger
    def save(self, obj: Building, tokenData: TokenData = None):
        dbSession = ApplicationServiceLifeCycle.dbContext()
        dbObject = dbSession.query(DbBuilding).filter_by(id=obj.id()).first()
        if dbObject is not None:
            self.updateBuilding(obj=obj, dbObject=dbObject, tokenData=tokenData)
        else:
            self.createBuilding(obj=obj, tokenData=tokenData)

    @debugLogger
    def createBuilding(self, obj: Building, tokenData: TokenData):
        dbSession = ApplicationServiceLifeCycle.dbContext()
        dbObject = self._createDbObjectByObj(obj=obj)
        dbSession.query(DbBuilding).filter_by(id=obj.id()).first()
        dbSession.add(dbObject)


    @debugLogger
    def deleteBuilding(self, obj: Building, tokenData: TokenData = None, ignoreRelations: bool = False) -> None:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        if ignoreRelations:
            DbUtil.disableForeignKeyChecks(dbSession=dbSession)
        dbObject = dbSession.query(DbBuilding).filter_by(id=obj.id()).first()
        if dbObject is not None:
            dbSession.delete(dbObject)
        if ignoreRelations:
            DbUtil.enableForeignKeyChecks(dbSession=dbSession)


    @debugLogger
    def updateBuilding(self, obj: Building, dbObject: DbBuilding = None, tokenData: TokenData = None) -> None:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        if dbObject is None:
            raise BuildingDoesNotExistException(f"building id = {obj.id()}")
        dbObject = self._updateDbObjectByObj(dbObject=dbObject, obj=obj)
        dbSession.add(dbObject)

    @debugLogger
    def bulkSave(self, objList: List[Building], tokenData: TokenData = None):
        dbSession = ApplicationServiceLifeCycle.dbContext()
        for obj in objList:
            dbObject = dbSession.query(DbBuilding).filter_by(id=obj.id()).first()
            if dbObject is not None:
                dbObject = self._updateDbObjectByObj(dbObject=dbObject, obj=obj)
            else:
                dbObject = self._createDbObjectByObj(obj=obj)
            dbSession.add(dbObject)


    @debugLogger
    def bulkDelete(
            self, objList: List[Building], tokenData: TokenData = None
    ) -> None:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        for obj in objList:
            dbObject = dbSession.query(DbBuilding).filter_by(id=obj.id()).first()
            if dbObject is not None:
                dbSession.delete(dbObject)

    @debugLogger
    def buildings(
        self,
        tokenData: TokenData,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
        include: List[str] = None,
        projectId: str = None,
    ) -> dict:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        include = [] if include is None else include
        q = dbSession.query(DbBuilding)
        if order is not None:
            for item in order:
                if item["orderBy"] == "id":
                    if item["direction"] == "desc":
                        q = q.order_by(desc(DbBuilding.id))
                    else:
                        q = q.order_by(DbBuilding.id)
                if item["orderBy"] == "name":
                    if item["direction"] == "desc":
                        q = q.order_by(desc(DbBuilding.name))
                    else:
                        q = q.order_by(DbBuilding.name)
                if item["orderBy"] == "project_id":
                    if item["direction"] == "desc":
                        q = q.order_by(desc(DbBuilding.projectId))
                    else:
                        q = q.order_by(DbBuilding.projectId)

        items = (
            q.filter(DbBuilding.projectId == projectId)
            .limit(resultSize)
            .offset(resultFrom)
            .all()
        )
        itemsCount = (
            dbSession.query(DbBuilding)
            .filter(DbBuilding.projectId == projectId)
            .count()
        )
        if items is None:
            return {"items": [], "totalItemCount": 0}
        result = []
        for building in items:
            buildingLevels = []
            if "buildingLevel" in include:
                for level in building.levels:
                    buildingLevelRooms = []
                    if "buildingLevelRoom" in include:
                        for room in level.rooms:
                            buildingLevelRooms.append(
                                BuildingLevelRoom.createFrom(
                                    id=room.id,
                                    name=room.name,
                                    index=room.index,
                                    description=room.description,
                                    buildingLevelId=room.buildingLevelId,
                                )
                            )
                    buildingLevels.append(
                        BuildingLevel.createFrom(
                            id=level.id,
                            name=level.name,
                            isSubLevel=level.isSubLevel,
                            rooms=buildingLevelRooms,
                            buildingIds=[x.id for x in level.buildings],
                        )
                    )

            result.append(
                Building.createFrom(
                    id=building.id,
                    projectId=building.projectId,
                    name=building.name,
                    buildingLevels=buildingLevels,
                )
            )

        return {"items": result, "totalItemCount": itemsCount}

    @debugLogger
    def buildingById(
        self, id: str, include: List[str] = None, tokenData: TokenData = None
    ) -> Building:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        include = [] if include is None else include
        dbObject = dbSession.query(DbBuilding).filter_by(id=id).first()
        if dbObject is None:
            raise BuildingDoesNotExistException(f"building id = {id}")

        buildingLevels = []
        if "buildingLevel" in include:
            for level in dbObject.levels:
                buildingLevelRooms = []
                if "buildingLevelRoom" in include:
                    for room in level.rooms:
                        buildingLevelRooms.append(
                            BuildingLevelRoom.createFrom(
                                id=room.id,
                                name=room.name,
                                index=room.index,
                                description=room.description,
                                buildingLevelId=room.buildingLevelId,
                            )
                        )
                buildingLevels.append(
                    BuildingLevel.createFrom(
                        id=level.id,
                        name=level.name,
                        isSubLevel=level.isSubLevel,
                        rooms=buildingLevelRooms,
                        buildingIds=[x.id for x in level.buildings],
                    )
                )

        return Building.createFrom(
            id=dbObject.id,
            projectId=dbObject.projectId,
            name=dbObject.name,
            buildingLevels=buildingLevels,
        )

    def _updateDbObjectByObj(self, dbObject: DbBuilding, obj: Building):
        dbObject.name = obj.name() if obj.name() is not None else dbObject.name
        dbObject.projectId = obj.projectId() if obj.projectId() is not None else dbObject.projectId
        return dbObject

    def _createDbObjectByObj(self, obj: Building):
        return DbBuilding(id=obj.id(), name=obj.name(),
                          projectId=obj.projectId())