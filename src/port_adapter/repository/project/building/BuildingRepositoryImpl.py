"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import os
from typing import List

from sqlalchemy import create_engine
from sqlalchemy.inspection import inspect
from sqlalchemy.sql.expression import text, desc

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
from src.domain_model.resource.exception.ObjectIdenticalException import (
    ObjectIdenticalException,
)
from src.domain_model.token.TokenData import TokenData
from src.port_adapter.repository.DbSession import DbSession
from src.port_adapter.repository.db_model.Building import Building as DbBuilding
from src.port_adapter.repository.db_model.BuildingLevel import (
    BuildingLevel as DbBuildingLevel,
)
from src.port_adapter.repository.db_model.BuildingLevelRoom import (
    BuildingLevelRoom as DbBuildingLevelRoom,
)
from src.port_adapter.repository.db_model.building__level__junction import (
    BUILDING__LEVEL__JUNCTION,
)
from src.resource.logging.decorator import debugLogger
from src.resource.logging.logger import logger


class BuildingRepositoryImpl(BuildingRepository):
    def __init__(self):
        import src.port_adapter.AppDi as AppDi

        self._buildingLevelRepo: BuildingLevelRepository = AppDi.instance.get(
            BuildingLevelRepository
        )
        try:
            self._db = create_engine(
                f"mysql+mysqlconnector://{os.getenv('CAFM_PROJECT_DB_USER', 'root')}:{os.getenv('CAFM_PROJECT_DB_PASSWORD', '1234')}@{os.getenv('CAFM_PROJECT_DB_HOST', '127.0.0.1')}:{os.getenv('CAFM_PROJECT_DB_PORT', '3306')}/{os.getenv('CAFM_PROJECT_DB_NAME', 'cafm-building')}"
            )
            self._dbBuildingColumnsMapping = inspect(DbBuilding).c
            self._dbBuildingLevelColumnsMapping = inspect(DbBuildingLevel).c
            self._dbBuildingLevelRoomColumnsMapping = inspect(DbBuildingLevelRoom).c
        except Exception as e:
            logger.warn(
                f"[{BuildingRepositoryImpl.__init__.__qualname__}] Could not connect to the db, message: {e}"
            )
            raise Exception(f"Could not connect to the db, message: {e}")

    @debugLogger
    def addLevelToBuilding(
        self,
        buildingLevel: BuildingLevel,
        building: Building,
        tokenData: TokenData = None,
    ):
        self._buildingLevelRepo.save(obj=buildingLevel)
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
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
                dbSession.commit()
        finally:
            dbSession.close()

    @debugLogger
    def removeLevelFromBuilding(
        self,
        buildingLevel: BuildingLevel,
        building: Building,
        tokenData: TokenData = None,
    ):
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
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
                dbSession.commit()
        finally:
            dbSession.close()

    @debugLogger
    def save(self, obj: Building, tokenData: TokenData = None):
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbBuilding).filter_by(id=obj.id()).first()
            if dbObject is not None:
                self.updateBuilding(obj=obj, dbObject=dbObject, tokenData=tokenData)
            else:
                self.createBuilding(obj=obj, tokenData=tokenData)
        finally:
            dbSession.close()

    @debugLogger
    def createBuilding(self, obj: Building, tokenData: TokenData):
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = self._createDbObjectByObj(obj=obj)
            dbSession.query(DbBuilding).filter_by(id=obj.id()).first()
            dbSession.add(dbObject)
            dbSession.commit()
        finally:
            dbSession.close()

    @debugLogger
    def deleteBuilding(self, obj: Building, tokenData: TokenData = None) -> None:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbBuilding).filter_by(id=obj.id()).first()
            if dbObject is not None:
                dbSession.delete(dbObject)
                dbSession.commit()
        finally:
            dbSession.close()

    @debugLogger
    def updateBuilding(self, obj: Building, dbObject: DbBuilding = None, tokenData: TokenData = None) -> None:
        from sqlalchemy import inspect
        dbSession = inspect(dbObject).session
        if dbObject is None:
            raise BuildingDoesNotExistException(f"building id = {obj.id()}")
        dbObject = self._updateDbObjectByObj(dbObject=dbObject, obj=obj)
        dbSession.add(dbObject)
        dbSession.commit()

    @debugLogger
    def bulkSave(self, objList: List[Building], tokenData: TokenData = None):
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            for obj in objList:
                dbObject = dbSession.query(DbBuilding).filter_by(id=obj.id()).first()
                if dbObject is not None:
                    dbObject = self._updateDbObjectByObj(dbObject=dbObject, obj=obj)
                else:
                    dbObject = self._createDbObjectByObj(obj=obj)
                dbSession.add(dbObject)
            dbSession.commit()
        finally:
            dbSession.close()

    @debugLogger
    def bulkDelete(
            self, objList: List[Building], tokenData: TokenData = None
    ) -> None:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            for obj in objList:
                dbObject = dbSession.query(DbBuilding).filter_by(id=obj.id()).first()
                if dbObject is not None:
                    dbSession.delete(dbObject)
            dbSession.commit()
        finally:
            dbSession.close()

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
        dbSession = DbSession.newSession(dbEngine=self._db)
        include = [] if include is None else include
        try:
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
        finally:
            dbSession.close()

    @debugLogger
    def buildingById(
        self, id: str, include: List[str] = None, tokenData: TokenData = None
    ) -> Building:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
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
        finally:
            dbSession.close()

    def _updateDbObjectByObj(self, dbObject: DbBuilding, obj: Building):
        dbObject.name = obj.name() if obj.name() is not None else dbObject.name
        dbObject.projectId = obj.projectId() if obj.projectId() is not None else dbObject.projectId
        return dbObject

    def _createDbObjectByObj(self, obj: Building):
        return DbBuilding(id=obj.id(), name=obj.name(),
                          projectId=obj.projectId())