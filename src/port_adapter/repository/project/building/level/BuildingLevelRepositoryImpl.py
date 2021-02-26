"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import os
from typing import List

from sqlalchemy import create_engine
from sqlalchemy.sql.expression import desc

from src.domain_model.project.building.Building import Building
from src.domain_model.project.building.level.BuildingLevel import BuildingLevel
from src.domain_model.project.building.level.BuildingLevelRepository import BuildingLevelRepository
from src.domain_model.project.building.level.room.BuildingLevelRoom import BuildingLevelRoom
from src.domain_model.project.building.level.room.BuildingLevelRoomRepository import BuildingLevelRoomRepository
from src.domain_model.resource.exception.BuildingLevelDoesNotExistException import BuildingLevelDoesNotExistException
from src.domain_model.token.TokenData import TokenData
from src.port_adapter.repository.DbSession import DbSession
from src.port_adapter.repository.db_model.Building import Building as DbBuilding
from src.port_adapter.repository.db_model.BuildingLevel import BuildingLevel as DbBuildingLevel
from src.port_adapter.repository.db_model.BuildingLevelRoom import BuildingLevelRoom as DbBuildingLevelRoom
from src.resource.logging.decorator import debugLogger
from src.resource.logging.logger import logger


class BuildingLevelRepositoryImpl(BuildingLevelRepository):
    def __init__(self):
        try:
            self._db = create_engine(
                f"mysql+mysqlconnector://{os.getenv('CAFM_PROJECT_DB_USER', 'root')}:{os.getenv('CAFM_PROJECT_DB_PASSWORD', '1234')}@{os.getenv('CAFM_PROJECT_DB_HOST', '127.0.0.1')}:{os.getenv('CAFM_PROJECT_DB_PORT', '3306')}/{os.getenv('CAFM_PROJECT_DB_NAME', 'cafm-building')}")

            import src.port_adapter.AppDi as AppDi
            self._buildingLevelRoomRepo: BuildingLevelRoomRepository = AppDi.instance.get(BuildingLevelRoomRepository)
        except Exception as e:
            logger.warn(
                f'[{BuildingLevelRepositoryImpl.__init__.__qualname__}] Could not connect to the db, message: {e}')
            raise Exception(f'Could not connect to the db, message: {e}')

    @debugLogger
    def save(self, obj: BuildingLevel, tokenData: TokenData = None):
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbBuildingLevel).filter_by(id=obj.id()).first()
            try:
                if dbObject is not None:
                    self.updateBuildingLevel(obj=obj, tokenData=tokenData)
                else:
                    self.createBuildingLevel(obj=obj, tokenData=tokenData)
            except Exception as e:
                logger.debug(e)
        finally:
            dbSession.close()

    @debugLogger
    def createBuildingLevel(self, obj: BuildingLevel, tokenData: TokenData):
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = DbBuildingLevel(id=obj.id(), name=obj.name())
            dbSession.query(DbBuildingLevel).filter_by(id=obj.id()).first()
            dbSession.add(dbObject)
            dbSession.commit()
        finally:
            dbSession.close()

    @debugLogger
    def deleteBuildingLevel(self, obj: BuildingLevel, tokenData: TokenData = None) -> None:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbBuildingLevel).filter_by(id=obj.id()).first()
            if dbObject is not None:
                dbSession.delete(dbObject)
                dbSession.commit()
        finally:
            dbSession.close()

    @debugLogger
    def updateBuildingLevel(self, obj: BuildingLevel, tokenData: TokenData = None) -> None:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbBuildingLevel).filter_by(id=obj.id()).first()
            if dbObject is None:
                raise BuildingLevelDoesNotExistException(f'building level id = {obj.id()}')
            dbObject.name = obj.name()

            # Update room indexes
            rooms = obj.rooms()
            for dbRoom in dbObject.rooms:
                for room in rooms:
                    if room.id() == dbRoom.id:
                        dbRoom.index = room.index()
                        rooms.remove(room)
            dbSession.add(dbObject)
            dbSession.commit()
        finally:
            dbSession.close()

    @debugLogger
    def linkBuildingLevelToBuilding(self, buildingLevel: BuildingLevel, building: Building,
                                    tokenData: TokenData = None):
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbBuildingLevel = dbSession.query(DbBuildingLevel).filter_by(id=buildingLevel.id()).first()
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
                    dbSession.commit()
        finally:
            dbSession.close()

    @debugLogger
    def unlinkBuildingLevelFromBuilding(self, buildingLevel: BuildingLevel, building: Building,
                                        tokenData: TokenData = None):
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbBuildingLevel = dbSession.query(DbBuildingLevel).filter_by(id=buildingLevel.id()).first()
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
                    dbSession.commit()
        finally:
            dbSession.close()

    @debugLogger
    def addBuildingLevelRoomToBuildingLevel(self, buildingLevelRoom: BuildingLevelRoom, buildingLevel: BuildingLevel,
                                            tokenData: TokenData = None):
        self._buildingLevelRoomRepo.save(obj=buildingLevelRoom)

    @debugLogger
    def removeBuildingLevelRoomFromBuildingLevel(self, buildingLevelRoom: BuildingLevelRoom,
                                                 buildingLevel: BuildingLevel, tokenData: TokenData = None):
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbBuildingLevelRoom).filter_by(id=buildingLevelRoom.id()).first()
            try:
                if dbObject.buildingLevelId == buildingLevel.id():
                    dbSession.delete(dbObject)
                    dbSession.commit()
            except Exception as e:
                logger.debug(e)
        finally:
            dbSession.close()

    @debugLogger
    def buildingLevels(self, tokenData: TokenData, resultFrom: int = 0, resultSize: int = 100,
                       order: List[dict] = None, include: List[str] = None, buildingId: str = None) -> dict:
        dbSession = DbSession.newSession(dbEngine=self._db)
        include = [] if include is None else include
        try:
            q = dbSession.query(DbBuildingLevel)
            if order is not None:
                for item in order:
                    if item['orderBy'] == 'id':
                        if item['direction'] == 'desc':
                            q = q.order_by(desc(DbBuildingLevel.id))
                        else:
                            q = q.order_by(DbBuildingLevel.id)
                    if item['orderBy'] == 'name':
                        if item['direction'] == 'desc':
                            q = q.order_by(desc(DbBuildingLevel.name))
                        else:
                            q = q.order_by(DbBuildingLevel.name)

            items = q.filter(DbBuildingLevel.buildings.any(id = buildingId)).limit(resultSize).offset(resultFrom).all()
            itemsCount = dbSession.query(DbBuildingLevel).filter(DbBuildingLevel.buildings.any(id = buildingId)).count()
            if items is None:
                return {"items": [], "itemCount": 0}

            result = []
            for level in items:
                buildingLevelRooms = []
                if 'buildingLevelRoom' in include:
                    for room in level.rooms:
                        buildingLevelRooms.append(
                            BuildingLevelRoom.createFrom(id=room.id, name=room.name, index=room.index,
                                                         description=room.description,
                                                         buildingLevelId=room.buildingLevelId))
                result.append(
                    BuildingLevel.createFrom(id=level.id, name=level.name, rooms=buildingLevelRooms,
                                             buildingIds=[x.id for x in level.buildings]))

            return {"items": result, "itemCount": itemsCount}
        finally:
            dbSession.close()

    @debugLogger
    def buildingLevelById(self, id: str, include: List[str] = None, tokenData: TokenData = None) -> BuildingLevel:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            include = [] if include is None else include
            dbObject = dbSession.query(DbBuildingLevel).filter_by(id=id).first()
            if dbObject is None:
                raise BuildingLevelDoesNotExistException(f'id = {id}')

            buildingLevelRooms = []
            if 'buildingLevelRoom' in include:
                for room in dbObject.rooms:
                    buildingLevelRooms.append(
                        BuildingLevelRoom.createFrom(id=room.id, name=room.name, index=room.index,
                                                     description=room.description,
                                                     buildingLevelId=room.buildingLevelId))
            return BuildingLevel.createFrom(id=dbObject.id, name=dbObject.name, rooms=buildingLevelRooms,
                                            buildingIds=[x.id for x in dbObject.buildings])

        finally:
            dbSession.close()
