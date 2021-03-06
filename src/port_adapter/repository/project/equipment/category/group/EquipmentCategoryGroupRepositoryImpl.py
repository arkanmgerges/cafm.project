"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from typing import List

from sqlalchemy.sql.expression import text, desc

from src.application.lifecycle.ApplicationServiceLifeCycle import ApplicationServiceLifeCycle
from src.domain_model.project.equipment.category.group.EquipmentCategoryGroup import (
    EquipmentCategoryGroup,
)
from src.domain_model.project.equipment.category.group.EquipmentCategoryGroupRepository import (
    EquipmentCategoryGroupRepository,
)
from src.domain_model.resource.exception.EquipmentCategoryGroupDoesNotExistException import (
    EquipmentCategoryGroupDoesNotExistException,
)
from src.domain_model.token.TokenData import TokenData
from src.port_adapter.repository.db_model.EquipmentCategoryGroup import (
    EquipmentCategoryGroup as DbEquipmentCategoryGroup,
)
from src.resource.logging.decorator import debugLogger
from src.resource.logging.logger import logger



class EquipmentCategoryGroupRepositoryImpl(EquipmentCategoryGroupRepository):
    @debugLogger
    def save(self, obj: EquipmentCategoryGroup, tokenData: TokenData = None):
        dbSession = ApplicationServiceLifeCycle.dbContext()
        dbObject = (
            dbSession.query(DbEquipmentCategoryGroup).filter_by(id=obj.id()).first()
        )
        if dbObject is not None:
            self.updateEquipmentCategoryGroup(obj=obj, dbObject=dbObject, tokenData=tokenData)
        else:
            self.createEquipmentCategoryGroup(obj=obj, tokenData=tokenData)

    @debugLogger
    def createEquipmentCategoryGroup(
        self, obj: EquipmentCategoryGroup, tokenData: TokenData = None
    ):
        dbSession = ApplicationServiceLifeCycle.dbContext()
        dbObject = self._createDbObjectByObj(obj=obj)
        result = (
            dbSession.query(DbEquipmentCategoryGroup).filter_by(id=obj.id()).first()
        )
        if result is None:
            dbSession.add(dbObject)


    @debugLogger
    def deleteEquipmentCategoryGroup(
        self, obj: EquipmentCategoryGroup, tokenData: TokenData = None
    ) -> None:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        dbObject = (
            dbSession.query(DbEquipmentCategoryGroup).filter_by(id=obj.id()).first()
        )
        if dbObject is not None:
            dbSession.delete(dbObject)


    @debugLogger
    def updateEquipmentCategoryGroup(
        self, obj: EquipmentCategoryGroup, dbObject: DbEquipmentCategoryGroup = None, tokenData: TokenData = None
    ) -> None:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        if dbObject is None:
            raise EquipmentCategoryGroupDoesNotExistException(f"id = {obj.id()}")
        dbObject = self._updateDbObjectByObj(dbObject=dbObject, obj=obj)
        dbSession.add(dbObject)

    @debugLogger
    def bulkSave(self, objList: List[EquipmentCategoryGroup], tokenData: TokenData = None):
        dbSession = ApplicationServiceLifeCycle.dbContext()
        for obj in objList:
            dbObject = dbSession.query(DbEquipmentCategoryGroup).filter_by(id=obj.id()).first()
            if dbObject is not None:
                dbObject = self._updateDbObjectByObj(dbObject=dbObject, obj=obj)
            else:
                dbObject = self._createDbObjectByObj(obj=obj)
            dbSession.add(dbObject)


    @debugLogger
    def bulkDelete(
            self, objList: List[EquipmentCategoryGroup], tokenData: TokenData = None
    ) -> None:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        for obj in objList:
            dbObject = dbSession.query(DbEquipmentCategoryGroup).filter_by(id=obj.id()).first()
            if dbObject is not None:
                dbSession.delete(dbObject)


    @debugLogger
    def equipmentCategoryGroupById(self, id: str) -> EquipmentCategoryGroup:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        dbObject = (
            dbSession.query(DbEquipmentCategoryGroup).filter_by(id=id).first()
        )
        if dbObject is None:
            raise EquipmentCategoryGroupDoesNotExistException(f"id = {id}")
        return EquipmentCategoryGroup(
            id=dbObject.id,
            name=dbObject.name,
            projectId=dbObject.projectId,
            equipmentProjectCategoryId=dbObject.equipmentProjectCategoryId,

        )

    @debugLogger
    def equipmentCategoryGroupByNameAndProjectIdAndEquipmentProjectCategoryId(self, name: str, projectId: str, equipmentProjectCategoryId: str) -> EquipmentCategoryGroup:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        dbObject = (
            dbSession.query(DbEquipmentCategoryGroup).filter_by(name=name, projectId=projectId, equipmentProjectCategoryId=equipmentProjectCategoryId).first()
        )
        if dbObject is None:
            return None
        return EquipmentCategoryGroup(
            id=dbObject.id,
            name=dbObject.name,
            projectId=dbObject.projectId,
            equipmentProjectCategoryId=dbObject.equipmentProjectCategoryId,
        )

    @debugLogger
    def equipmentCategoryGroups(
        self,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
        tokenData: TokenData = None,
    ) -> dict:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        sortData = ""
        if order is not None:
            for item in order:
                sortData = f'{sortData}, {item["orderBy"]} {item["direction"]}'
            sortData = sortData[2:]
        items = (
            dbSession.query(DbEquipmentCategoryGroup)
            .order_by(text(sortData))
            .limit(resultSize)
            .offset(resultFrom)
            .all()
        )
        itemsCount = dbSession.query(DbEquipmentCategoryGroup).count()

        if items is None:
            return {"items": [], "totalItemCount": 0}
        return {
            "items": [
                EquipmentCategoryGroup.createFrom(
                    id=x.id, name=x.name, projectId=x.projectId, equipmentProjectCategoryId=x.equipmentProjectCategoryId,
                )
                for x in items
            ],
            "totalItemCount": itemsCount,
        }

    @debugLogger
    def equipmentCategoryGroupsByEquipmentProjectCategoryId(
        self,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
        equipmentProjectCategoryId: str = None,
        tokenData: TokenData = None,
    ) -> dict:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        sortData = ""
        if order is not None:
            for item in order:
                sortData = f'{sortData}, {item["orderBy"]} {item["direction"]}'
            sortData = sortData[2:]
        items = (
            dbSession.query(DbEquipmentCategoryGroup)
            .filter_by(equipmentProjectCategoryId=equipmentProjectCategoryId)
            .order_by(text(sortData))
            .limit(resultSize)
            .offset(resultFrom)
            .all()
        )
        itemsCount = dbSession.query(DbEquipmentCategoryGroup).filter_by(equipmentProjectCategoryId=equipmentProjectCategoryId).count()

        if items is None:
            return {"items": [], "totalItemCount": 0}
        return {
            "items": [
                EquipmentCategoryGroup.createFrom(
                    id=x.id, name=x.name, projectId=x.projectId, equipmentProjectCategoryId=x.equipmentProjectCategoryId,
                )
                for x in items
            ],
            "totalItemCount": itemsCount,
        }


    @debugLogger
    def equipmentCategoryGroupsByProjectId(
        self,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
        projectId: str = None,
        tokenData: TokenData = None,
    ) -> dict:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        sortData = ""
        if order is not None:
            for item in order:
                sortData = f'{sortData}, {item["orderBy"]} {item["direction"]}'
            sortData = sortData[2:]
        items = (
            dbSession.query(DbEquipmentCategoryGroup)
            .filter_by(projectId=projectId)
            .order_by(text(sortData))
            .limit(resultSize)
            .offset(resultFrom)
            .all()
        )
        itemsCount = dbSession.query(DbEquipmentCategoryGroup).filter_by(projectId=projectId).count()

        if items is None:
            return {"items": [], "totalItemCount": 0}
        return {
            "items": [
                EquipmentCategoryGroup.createFrom(
                    id=x.id, name=x.name, projectId=x.projectId, equipmentProjectCategoryId=x.equipmentProjectCategoryId,
                )
                for x in items
            ],
            "totalItemCount": itemsCount,
        }


    def _updateDbObjectByObj(self, dbObject: DbEquipmentCategoryGroup, obj: EquipmentCategoryGroup):
        dbObject.name = obj.name() if obj.name() is not None else dbObject.name
        dbObject.projectId = obj.projectId() if obj.projectId() is not None else dbObject.projectId
        dbObject.equipmentProjectCategoryId = obj.equipmentProjectCategoryId() if obj.equipmentProjectCategoryId() is not None else dbObject.equipmentProjectCategoryId
        return dbObject


    def _createDbObjectByObj(self, obj: EquipmentCategoryGroup):
        return DbEquipmentCategoryGroup(id=obj.id(), name=obj.name(), projectId=obj.projectId(), equipmentProjectCategoryId=obj.equipmentProjectCategoryId())
