"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from sqlalchemy.sql.expression import desc, text

from src.application.lifecycle.ApplicationServiceLifeCycle import ApplicationServiceLifeCycle
from src.domain_model.project.building.level.room.BuildingLevelRoom import (
    BuildingLevelRoom,
)
from src.domain_model.project.building.level.room.BuildingLevelRoomRepository import (
    BuildingLevelRoomRepository,
)
from src.domain_model.resource.exception.BuildingLevelRoomDoesNotExistException import (
    BuildingLevelRoomDoesNotExistException,
)
from src.domain_model.token.TokenData import TokenData
from src.port_adapter.repository.common.DbUtil import DbUtil
from src.port_adapter.repository.db_model.BuildingLevelRoom import (
    BuildingLevelRoom as DbBuildingLevelRoom,
)
from src.resource.logging.decorator import debugLogger


class BuildingLevelRoomRepositoryImpl(BuildingLevelRoomRepository):
    @debugLogger
    def save(self, obj: BuildingLevelRoom, tokenData: TokenData = None):
        dbSession = ApplicationServiceLifeCycle.dbContext()
        dbObject = dbSession.query(DbBuildingLevelRoom).filter_by(id=obj.id()).first()
        if dbObject is not None:
            self.updateBuildingLevelRoom(obj=obj, dbObject=dbObject, tokenData=tokenData)
        else:
            self.createBuildingLevelRoom(obj=obj, tokenData=tokenData)

    @debugLogger
    def bulkSave(self, objList: List[BuildingLevelRoom], tokenData: TokenData = None):
        dbSession = ApplicationServiceLifeCycle.dbContext()
        for obj in objList:
            dbObject = dbSession.query(DbBuildingLevelRoom).filter_by(id=obj.id()).first()
            if dbObject is not None:
                dbObject = self._updateDbObjectByObj(dbObject=dbObject, obj=obj)
            else:
                dbObject = self._createDbObjectByObj(obj=obj)
            dbSession.add(dbObject)


    @debugLogger
    def bulkDelete(
            self, objList: List[BuildingLevelRoom], tokenData: TokenData = None
    ) -> None:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        for obj in objList:
            dbObject = dbSession.query(DbBuildingLevelRoom).filter_by(id=obj.id()).first()
            if dbObject is not None:
                dbSession.delete(dbObject)

    @debugLogger
    def removeBuildingLevelRoom(self,
                                buildingLevelRoom: BuildingLevelRoom,
                                tokenData: TokenData,
                                ignoreRelations: bool):
        dbSession = ApplicationServiceLifeCycle.dbContext()
        if ignoreRelations:
            DbUtil.disableForeignKeyChecks(dbSession=dbSession)
        dbSession.execute(
            text(f'''
                DELETE FROM building_level_room 
                    WHERE id = "{buildingLevelRoom.id()}"
            '''))
        if ignoreRelations:
            DbUtil.enableForeignKeyChecks(dbSession=dbSession)


    @debugLogger
    def buildingLevelRoomsByBuildingLevelId(self, buildingLevelId: str, resultSize: int = 100) -> List[BuildingLevelRoom]:
        result = []
        dbSession = ApplicationServiceLifeCycle.dbContext()
        from sqlalchemy.engine import ResultProxy
        dbResult: ResultProxy = dbSession.execute(
            text(f"""
                SELECT id FROM building_level_room 
                    WHERE building_level_id = "{buildingLevelId}" LIMIT {resultSize}
            """))
        for row in dbResult:
            obj = self.buildingLevelRoomById(id=row['id'])
            if obj is not None:
                result.append(obj)
        return result


    @debugLogger
    def createBuildingLevelRoom(self, obj: BuildingLevelRoom, tokenData: TokenData):
        dbSession = ApplicationServiceLifeCycle.dbContext()
        dbObject = self._createDbObjectByObj(obj=obj)
        dbSession.add(dbObject)


    @debugLogger
    def deleteBuildingLevelRoom(
        self, obj: BuildingLevelRoom, tokenData: TokenData = None
    ) -> None:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        dbObject = (
            dbSession.query(DbBuildingLevelRoom).filter_by(id=obj.id()).first()
        )
        if dbObject is not None:
            dbSession.delete(dbObject)
    

    @debugLogger
    def updateBuildingLevelRoom(
        self, obj: BuildingLevelRoom, dbObject: DbBuildingLevelRoom = None, tokenData: TokenData = None
    ) -> None:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        if dbObject is None:
            raise BuildingLevelRoomDoesNotExistException(
                f"building level room id = {obj.id()}"
            )
        dbObject = self._updateDbObjectByObj(dbObject=dbObject, obj=obj)
        dbSession.add(dbObject)

    @debugLogger
    def buildingLevelRooms(
        self,
        tokenData: TokenData = None,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
        buildingLevelId: str = None,
    ) -> dict:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        db = DbBuildingLevelRoom
        q = dbSession.query(db)
        if order is not None:
            for item in order:
                if item["orderBy"] == "id":
                    if item["direction"] == "desc":
                        q = q.order_by(desc(db.id))
                    else:
                        q = q.order_by(db.id)
                if item["orderBy"] == "name":
                    if item["direction"] == "desc":
                        q = q.order_by(desc(db.name))
                    else:
                        q = q.order_by(db.name)
                if item["orderBy"] == "description":
                    if item["direction"] == "desc":
                        q = q.order_by(desc(db.description))
                    else:
                        q = q.order_by(db.description)
                if item["orderBy"] == "index":
                    if item["direction"] == "desc":
                        q = q.order_by(desc(db.index))
                    else:
                        q = q.order_by(db.index)

        items = (
            q.filter(DbBuildingLevelRoom.buildingLevelId == buildingLevelId)
            .limit(resultSize)
            .offset(resultFrom)
            .all()
        )
        itemsCount = (
            dbSession.query(DbBuildingLevelRoom)
            .filter(DbBuildingLevelRoom.buildingLevelId == buildingLevelId)
            .count()
        )
        if items is None:
            return {"items": [], "totalItemCount": 0}

        result = []
        for room in items:
            result.append(
                BuildingLevelRoom.createFrom(
                    id=room.id,
                    name=room.name,
                    index=room.index,
                    description=room.description,
                    buildingLevelId=room.buildingLevelId,
                )
            )

        return {"items": result, "totalItemCount": itemsCount}

    @debugLogger
    def buildingLevelRoomById(
        self, id: str, tokenData: TokenData = None
    ) -> BuildingLevelRoom:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        dbObject = dbSession.query(DbBuildingLevelRoom).filter_by(id=id).first()
        if dbObject is None:
            raise BuildingLevelRoomDoesNotExistException(
                f"building level room id = {id}"
            )
        return BuildingLevelRoom.createFrom(
            id=dbObject.id,
            name=dbObject.name,
            description=dbObject.description,
            buildingLevelId=dbObject.buildingLevelId,
        )

    def _updateDbObjectByObj(self, dbObject: DbBuildingLevelRoom, obj: BuildingLevelRoom):
        dbObject.name = obj.name() if obj.name() is not None else dbObject.name
        dbObject.description = obj.description() if obj.description() is not None else dbObject.description
        return dbObject

    def _createDbObjectByObj(self, obj: BuildingLevelRoom):
        return DbBuildingLevelRoom(id=obj.id(),
                                   name=obj.name(),
                                   description=obj.description(),
                                   index=obj.index(),
                                   buildingLevelId=obj.buildingLevelId())