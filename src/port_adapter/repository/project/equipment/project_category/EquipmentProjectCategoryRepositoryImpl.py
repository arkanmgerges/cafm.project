"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from sqlalchemy.sql.expression import text

from src.application.lifecycle.ApplicationServiceLifeCycle import ApplicationServiceLifeCycle
from src.domain_model.project.equipment.category.group.EquipmentCategoryGroup import (
    EquipmentCategoryGroup,
)
from src.domain_model.project.equipment.project_category.EquipmentProjectCategory import (
    EquipmentProjectCategory,
)
from src.domain_model.project.equipment.project_category.EquipmentProjectCategoryRepository import (
    EquipmentProjectCategoryRepository,
)
from src.domain_model.resource.exception.EquipmentProjectCategoryDoesNotExistException import (
    EquipmentProjectCategoryDoesNotExistException,
)
from src.domain_model.token.TokenData import TokenData
from src.port_adapter.repository.db_model.EquipmentCategoryGroup import (
    EquipmentCategoryGroup as DbEquipmentCategoryGroup,
)
from src.port_adapter.repository.db_model.EquipmentProjectCategory import (
    EquipmentProjectCategory as DbEquipmentProjectCategory,
)
from src.resource.logging.decorator import debugLogger


class EquipmentProjectCategoryRepositoryImpl(EquipmentProjectCategoryRepository):
    @debugLogger
    def save(self, obj: EquipmentProjectCategory, tokenData: TokenData = None):
        dbSession = ApplicationServiceLifeCycle.dbContext()
        dbObject = (
            dbSession.query(DbEquipmentProjectCategory)
            .filter_by(id=obj.id())
            .first()
        )
        if dbObject is not None:
            self.updateEquipmentProjectCategory(obj=obj, dbObject=dbObject, tokenData=tokenData)
        else:
            self.createEquipmentProjectCategory(obj=obj, tokenData=tokenData)

    @debugLogger
    def createEquipmentProjectCategory(
        self, obj: EquipmentProjectCategory, tokenData: TokenData = None
    ):
        dbSession = ApplicationServiceLifeCycle.dbContext()
        dbObject = self._createDbObjectByObj(obj=obj)
        result = (
            dbSession.query(DbEquipmentProjectCategory)
            .filter_by(id=obj.id())
            .first()
        )
        if result is None:
            dbSession.add(dbObject)

    @debugLogger
    def deleteEquipmentProjectCategory(
        self, obj: EquipmentProjectCategory, tokenData: TokenData = None
    ) -> None:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        dbObject = (
            dbSession.query(DbEquipmentProjectCategory)
            .filter_by(id=obj.id())
            .first()
        )
        if dbObject is not None:
            dbSession.delete(dbObject)


    @debugLogger
    def updateEquipmentProjectCategory(
        self, obj: EquipmentProjectCategory, dbObject: DbEquipmentProjectCategory = None, tokenData: TokenData = None
    ) -> None:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        if dbObject is None:
            raise EquipmentProjectCategoryDoesNotExistException(f"id = {obj.id()}")
        dbObject = self._updateDbObjectByObj(dbObject=dbObject, obj=obj)
        dbSession.add(dbObject)

    @debugLogger
    def bulkSave(self, objList: List[EquipmentProjectCategory], tokenData: TokenData = None):
        dbSession = ApplicationServiceLifeCycle.dbContext()
        for obj in objList:
            dbObject = dbSession.query(DbEquipmentProjectCategory).filter_by(id=obj.id()).first()
            if dbObject is not None:
                dbObject = self._updateDbObjectByObj(dbObject=dbObject, obj=obj)
            else:
                dbObject = self._createDbObjectByObj(obj=obj)
            dbSession.add(dbObject)

    @debugLogger
    def bulkDelete(
            self, objList: List[EquipmentProjectCategory], tokenData: TokenData = None
    ) -> None:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        for obj in objList:
            dbObject = dbSession.query(DbEquipmentProjectCategory).filter_by(id=obj.id()).first()
            if dbObject is not None:
                dbSession.delete(dbObject)

    @debugLogger
    def equipmentProjectCategoryByName(self, name: str) -> EquipmentProjectCategory:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        dbObject = (
            dbSession.query(DbEquipmentProjectCategory).filter_by(name=name).first()
        )
        if dbObject is None:
            raise EquipmentProjectCategoryDoesNotExistException(f"name = {name}")
        return EquipmentProjectCategory(id=dbObject.id, name=dbObject.name)

    @debugLogger
    def equipmentProjectCategoryById(self, id: str) -> EquipmentProjectCategory:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        dbObject = (
            dbSession.query(DbEquipmentProjectCategory).filter_by(id=id).first()
        )
        if dbObject is None:
            raise EquipmentProjectCategoryDoesNotExistException(f"id = {id}")
        return EquipmentProjectCategory(id=dbObject.id, name=dbObject.name)

    @debugLogger
    def equipmentProjectCategories(
        self,
        tokenData: TokenData,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
    ) -> dict:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        sortData = ""
        if order is not None:
            for item in order:
                sortData = f'{sortData}, {item["orderBy"]} {item["direction"]}'
            sortData = sortData[2:]
        items = (
            dbSession.query(DbEquipmentProjectCategory)
            .order_by(text(sortData))
            .limit(resultSize)
            .offset(resultFrom)
            .all()
        )
        itemsCount = dbSession.query(DbEquipmentProjectCategory).count()
        if items is None:
            return {"items": [], "totalItemCount": 0}
        return {
            "items": [
                EquipmentProjectCategory.createFrom(id=x.id, name=x.name)
                for x in items
            ],
            "totalItemCount": itemsCount,
        }

    @debugLogger
    def linkEquipmentProjectCategoryGroup(
        self, category: EquipmentProjectCategory, group: EquipmentCategoryGroup
    ) -> None:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        dbCategoryObject: DbEquipmentProjectCategory = (
            dbSession.query(DbEquipmentProjectCategory)
            .filter_by(id=category.id())
            .first()
        )
        if dbCategoryObject is not None:
            dbGroupObject: DbEquipmentCategoryGroup = (
                dbSession.query(DbEquipmentCategoryGroup)
                .filter_by(id=group.id())
                .first()
            )
            if dbGroupObject is not None:
                dbCategoryObject.equipmentCategoryGroups.append(dbGroupObject)
        

    @debugLogger
    def unLinkEquipmentProjectCategoryGroup(
        self, category: EquipmentProjectCategory, group: EquipmentCategoryGroup
    ) -> None:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        dbCategoryObject: DbEquipmentProjectCategory = (
            dbSession.query(DbEquipmentProjectCategory)
            .filter_by(id=category.id())
            .first()
        )
        if dbCategoryObject is not None:
            dbGroupObject: DbEquipmentCategoryGroup = (
                dbSession.query(DbEquipmentCategoryGroup)
                .filter_by(id=group.id())
                .first()
            )
            if dbGroupObject is not None:
                for obj in dbCategoryObject.equipmentCategoryGroups:
                    if obj.id == group.id():
                        dbCategoryObject.equipmentCategoryGroups.remove(obj)
        

    @debugLogger
    def equipmentCategoryGroupsByEquipmentProjectCategoryId(
        self,
        id: str,
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
            .join(DbEquipmentCategoryGroup.equipmentProjectCategories)
            .filter(DbEquipmentProjectCategory.id == id)
            .order_by(text(sortData))
            .limit(resultSize)
            .offset(resultFrom)
            .all()
        )
        itemsCount = (
            dbSession.query(DbEquipmentCategoryGroup)
            .join(DbEquipmentCategoryGroup.equipmentProjectCategories)
            .filter(DbEquipmentProjectCategory.id == id)
            .count()
        )
        if items is None:
            return {"items": [], "totalItemCount": 0}
        return {
            "items": [
                EquipmentCategoryGroup.createFrom(
                    id=x.id, name=x.name, equipmentCategoryId=x.equipmentCategoryId
                )
                for x in items
            ],
            "totalItemCount": itemsCount,
        }

    def _updateDbObjectByObj(self, dbObject: DbEquipmentProjectCategory, obj: EquipmentProjectCategory):
        dbObject.name = obj.name() if obj.name() is not None else dbObject.name
        return dbObject

    def _createDbObjectByObj(self, obj: EquipmentProjectCategory):
        return DbEquipmentProjectCategory(id=obj.id(), name=obj.name())