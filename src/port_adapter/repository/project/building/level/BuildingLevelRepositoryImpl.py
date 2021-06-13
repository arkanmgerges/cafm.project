"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from sqlalchemy.sql.expression import desc, text

from src.application.lifecycle.ApplicationServiceLifeCycle import ApplicationServiceLifeCycle
from src.application.lookup.equipment.BuildingLevelRoomRepository import BuildingLevelRoomRepository
from src.domain_model.project.building.Building import Building
from src.domain_model.project.building.level.BuildingLevel import BuildingLevel
from src.domain_model.project.building.level.BuildingLevelRepository import (
    BuildingLevelRepository,
)
from src.domain_model.project.building.level.room.BuildingLevelRoom import (
    BuildingLevelRoom,
)
from src.domain_model.resource.exception.BuildingLevelDoesNotExistException import (
    BuildingLevelDoesNotExistException,
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


class BuildingLevelRepositoryImpl(BuildingLevelRepository):
    def __init__(self):
        import src.port_adapter.AppDi as AppDi

        self._buildingLevelRoomRepo: BuildingLevelRoomRepository = (
            AppDi.instance.get(BuildingLevelRoomRepository)
        )

    @debugLogger
    def save(self, obj: BuildingLevel, tokenData: TokenData = None):
        dbSession = ApplicationServiceLifeCycle.dbContext()
        dbObject = dbSession.query(DbBuildingLevel).filter_by(id=obj.id()).first()
        if dbObject is not None:
            self.updateBuildingLevel(obj=obj, dbObject=dbObject, tokenData=tokenData)
        else:
            self.createBuildingLevel(obj=obj, tokenData=tokenData)

    @debugLogger
    def createBuildingLevel(self, obj: BuildingLevel, tokenData: TokenData):
        dbSession = ApplicationServiceLifeCycle.dbContext()
        dbObject = self._createDbObjectByObj(obj=obj)
        dbSession.add(dbObject)


    @debugLogger
    def deleteBuildingLevel(
        self, obj: BuildingLevel, tokenData: TokenData = None
    ) -> None:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        dbObject = dbSession.query(DbBuildingLevel).filter_by(id=obj.id()).first()
        if dbObject is not None:
            dbSession.delete(dbObject)
    

    @debugLogger
    def updateBuildingLevel(
        self, obj: BuildingLevel, dbObject: DbBuildingLevel = None, tokenData: TokenData = None
    ) -> None:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        if dbObject is None:
            raise BuildingLevelDoesNotExistException(
                f"building level id = {obj.id()}"
            )
        dbObject = self._updateDbObjectByObj(dbObject=dbObject, obj=obj)

        # Update room indexes
        rooms = obj.rooms()
        for dbRoom in dbObject.rooms:
            for room in rooms:
                if room.id() == dbRoom.id:
                    dbRoom.index = room.index()
                    rooms.remove(room)
        dbSession.add(dbObject)


    @debugLogger
    def bulkSave(self, objList: List[dict], tokenData: TokenData = None):
        dbSession = ApplicationServiceLifeCycle.dbContext()
        for obj in objList:
            buildingLevel = obj['buildingLevel']
            dbBuildingLevelObject = dbSession.query(DbBuildingLevel).filter_by(id=buildingLevel.id()).first()
            if dbBuildingLevelObject is not None:
                dbBuildingLevelObject = self._updateDbObjectByObj(dbObject=dbBuildingLevelObject, obj=buildingLevel)
            else:
                buildingId = obj['buildingId']
                dbBuildingLevelObject = self._createDbObjectByObj(obj=buildingLevel)
                # Link level with building
                buildingHasLevel = False
                for dbBuildingObject in dbBuildingLevelObject.buildings:
                    if dbBuildingObject.id == buildingId:
                        buildingHasLevel = True
                        break

                if not buildingHasLevel:
                    dbBuildingObject = (
                        dbSession.query(DbBuilding).filter_by(id=buildingId).first()
                    )
                    dbBuildingLevelObject.buildings.append(dbBuildingObject)
                    dbSession.add(dbBuildingObject)

            dbSession.add(dbBuildingLevelObject)

    def _addLevelToBuilding(
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

        if not buildingHasLevel:
            dbBuilding = (
                dbSession.query(DbBuilding).filter_by(id=building.id()).first()
            )
            dbObject.buildings.append(dbBuilding)
            dbSession.add(dbObject)
    

    @debugLogger
    def bulkDelete(
            self, objList: List[BuildingLevel], tokenData: TokenData = None
    ) -> None:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        for obj in objList:
            dbObject = dbSession.query(DbBuildingLevel).filter_by(id=obj.id()).first()
            if dbObject is not None:
                dbSession.delete(dbObject)


    @debugLogger
    def linkBuildingLevelToBuilding(
        self,
        buildingLevel: BuildingLevel,
        building: Building,
        tokenData: TokenData = None,
    ):
        dbSession = ApplicationServiceLifeCycle.dbContext()
        dbBuildingLevel = (
            dbSession.query(DbBuildingLevel)
            .filter_by(id=buildingLevel.id())
            .first()
        )
        dbBuilding = dbSession.query(DbBuilding).filter_by(id=building.id()).first()
        if dbBuilding is not None and dbBuildingLevel is not None:
            levelLinkedToBuilding = False
            for level in dbBuilding.levels:
                if level.id == buildingLevel.id():
                    levelLinkedToBuilding = True
                    break
            if not levelLinkedToBuilding:
                dbBuilding.levels.append(dbBuildingLevel)
                dbSession.add(dbBuilding)
        

    @debugLogger
    def unlinkBuildingLevelFromBuilding(
        self,
        buildingLevel: BuildingLevel,
        building: Building,
        tokenData: TokenData = None,
    ):
        dbSession = ApplicationServiceLifeCycle.dbContext()
        dbBuildingLevel = (
            dbSession.query(DbBuildingLevel)
            .filter_by(id=buildingLevel.id())
            .first()
        )
        dbBuilding = dbSession.query(DbBuilding).filter_by(id=building.id()).first()
        if dbBuilding is not None and dbBuildingLevel is not None:
            levelLinkedToBuilding = False
            for level in dbBuilding.levels:
                if level.id == buildingLevel.id():
                    levelLinkedToBuilding = True
                    break
            if levelLinkedToBuilding:
                # If this is the only building for this level, then delete the level
                if len(dbBuildingLevel.buildings) == 1:
                    dbSession.delete(dbBuildingLevel)
                else:
                    # In case there are more buildings that are linked to the level, then only unlink it
                    dbBuilding.levels.remove(dbBuildingLevel)
                    dbSession.add(dbBuilding)
        

    @debugLogger
    def addBuildingLevelRoomToBuildingLevel(
        self,
        buildingLevelRoom: BuildingLevelRoom,
        buildingLevel: BuildingLevel,
        tokenData: TokenData = None,
    ):
        self._buildingLevelRoomRepo.save(obj=buildingLevelRoom)

    @debugLogger
    def removeBuildingLevelRoomFromBuildingLevel(
        self,
        buildingLevelRoom: BuildingLevelRoom,
        buildingLevel: BuildingLevel,
        tokenData: TokenData = None,
    ):
        dbSession = ApplicationServiceLifeCycle.dbContext()
        dbObject = (
            dbSession.query(DbBuildingLevelRoom)
            .filter_by(id=buildingLevelRoom.id())
            .first()
        )
        if dbObject.buildingLevelId == buildingLevel.id():
            dbSession.delete(dbObject)

    @debugLogger
    def removeBuildingLevel(self,
                            buildingLevel: BuildingLevel,
                            tokenData: TokenData,
                            ignoreRelations: bool):
        dbSession = ApplicationServiceLifeCycle.dbContext()
        if ignoreRelations:
            DbUtil.disableForeignKeyChecks(dbSession=dbSession)
        dbSession.execute(
            text(f"""
                DELETE FROM building__level__junction building__level__junc 
                    WHERE building__level__junc.building_level_id = "{buildingLevel.id()}"
            """))
        dbSession.execute(
            text(f"""
                        DELETE FROM building_level 
                            WHERE id = "{buildingLevel.id()}"
                    """))
        if ignoreRelations:
            DbUtil.enableForeignKeyChecks(dbSession=dbSession)


    @debugLogger
    def buildingLevels(
        self,
        tokenData: TokenData,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
        include: List[str] = None,
        buildingId: str = None,
    ) -> dict:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        include = [] if include is None else include
        q = dbSession.query(DbBuildingLevel)
        if order is not None:
            for item in order:
                if item["orderBy"] == "id":
                    if item["direction"] == "desc":
                        q = q.order_by(desc(DbBuildingLevel.id))
                    else:
                        q = q.order_by(DbBuildingLevel.id)
                if item["orderBy"] == "name":
                    if item["direction"] == "desc":
                        q = q.order_by(desc(DbBuildingLevel.name))
                    else:
                        q = q.order_by(DbBuildingLevel.name)

        items = (
            q.filter(DbBuildingLevel.buildings.any(id=buildingId))
            .limit(resultSize)
            .offset(resultFrom)
            .all()
        )
        itemsCount = (
            dbSession.query(DbBuildingLevel)
            .filter(DbBuildingLevel.buildings.any(id=buildingId))
            .count()
        )
        if items is None:
            return {"items": [], "totalItemCount": 0}

        result = []
        for level in items:
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
            result.append(
                BuildingLevel.createFrom(
                    id=level.id,
                    name=level.name,
                    isSubLevel=level.isSubLevel,
                    rooms=buildingLevelRooms,
                    buildingIds=[x.id for x in level.buildings],
                )
            )

        return {"items": result, "totalItemCount": itemsCount}

    @debugLogger
    def buildingLevelsByBuildingId(self, buildingId: str, resultSize: int = 100) -> List[BuildingLevel]:
        result = []
        dbSession = ApplicationServiceLifeCycle.dbContext()
        from sqlalchemy.engine import ResultProxy
        dbResult: ResultProxy = dbSession.execute(
            text(f"""
                SELECT building_level.id FROM building_level building_level 
                    INNER JOIN building__level__junction building__level__junc ON building__level__junc.building_level_id = building_level.id 
                    WHERE building__level__junc.building_id = "{buildingId}" LIMIT {resultSize}
            """))
        for row in dbResult:
            obj = self.buildingLevelById(id=row['id'])
            if obj is not None:
                result.append(obj)
        return result

    @debugLogger
    def buildingLevelById(
        self, id: str, include: List[str] = None, tokenData: TokenData = None
    ) -> BuildingLevel:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        include = [] if include is None else include
        dbObject = dbSession.query(DbBuildingLevel).filter_by(id=id).first()
        if dbObject is None:
            raise BuildingLevelDoesNotExistException(f"building level id = {id}")

        buildingLevelRooms = []
        if "buildingLevelRoom" in include:
            for room in dbObject.rooms:
                buildingLevelRooms.append(
                    BuildingLevelRoom.createFrom(
                        id=room.id,
                        name=room.name,
                        index=room.index,
                        description=room.description,
                        buildingLevelId=room.buildingLevelId,
                    )
                )
        return BuildingLevel.createFrom(
            id=dbObject.id,
            name=dbObject.name,
            isSubLevel=dbObject.isSubLevel,
            rooms=buildingLevelRooms,
            buildingIds=[x.id for x in dbObject.buildings],
        )

    def _updateDbObjectByObj(self, dbObject: DbBuildingLevel, obj: BuildingLevel):
        dbObject.name = obj.name() if obj.name() is not None else dbObject.name
        dbObject.isSubLevel = obj.isSubLevel() if obj.isSubLevel() is not None else dbObject.isSubLevel
        return dbObject

    def _createDbObjectByObj(self, obj: BuildingLevel):
        return DbBuildingLevel(id=obj.id(), name=obj.name(),
                               isSubLevel=obj.isSubLevel())
