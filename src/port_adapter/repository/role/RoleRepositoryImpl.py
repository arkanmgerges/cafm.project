"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import os
from typing import List

from sqlalchemy import create_engine
from sqlalchemy.sql.expression import text

from src.domain_model.resource.exception.RoleDoesNotExistException import (
    RoleDoesNotExistException,
)

# from src.domain_model.organization.OrganizationRepository import OrganizationRepository
from src.domain_model.role.Role import Role
from src.domain_model.role.RoleRepository import RoleRepository
from src.domain_model.token.TokenData import TokenData
from src.port_adapter.repository.DbSession import DbSession
from src.port_adapter.repository.db_model.Role import Role as DbRole
from src.port_adapter.repository.db_model.role__organization__junction import (
    ROLE__ORGANIZATION__JUNCTION,
)
from src.resource.logging.decorator import debugLogger
from src.resource.logging.logger import logger


class RoleRepositoryImpl(RoleRepository):
    def __init__(self):
        # import src.port_adapter.AppDi as AppDi

        # self._organizationRepo: OrganizationRepository = AppDi.instance.get(
        #     OrganizationRepository
        # )

        try:
            self._db = create_engine(
                f"mysql+mysqlconnector://{os.getenv('CAFM_PROJECT_DB_USER', 'root')}:{os.getenv('CAFM_PROJECT_DB_PASSWORD', '1234')}@{os.getenv('CAFM_PROJECT_DB_HOST', '127.0.0.1')}/{os.getenv('CAFM_PROJECT_DB_NAME', 'cafm-role')}"
            )
        except Exception as e:
            logger.warn(
                f"[{RoleRepositoryImpl.__init__.__qualname__}] Could not connect to the db, message: {e}"
            )
            raise Exception(f"Could not connect to the db, message: {e}")

    @debugLogger
    def save(self, obj: Role, tokenData: TokenData = None):
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbRole).filter_by(id=obj.id()).first()
            if dbObject is not None:
                self.updateRole(obj=obj, tokenData=tokenData)
            else:
                self.createRole(obj=obj, tokenData=tokenData)
        finally:
            dbSession.close()

    @debugLogger
    def createRole(self, obj: Role, tokenData: TokenData = None):
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = DbRole(id=obj.id(), name=obj.name(), title=obj.title())
            result = dbSession.query(DbRole).filter_by(id=obj.id()).first()
            if result is None:
                dbSession.add(dbObject)
                dbSession.commit()
        finally:
            dbSession.close()

    @debugLogger
    def deleteRole(self, obj: Role, tokenData: TokenData = None) -> None:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbRole).filter_by(id=obj.id()).first()
            if dbObject is not None:
                dbSession.delete(dbObject)
                dbSession.commit()
        finally:
            dbSession.close()

    @debugLogger
    def updateRole(self, obj: Role, tokenData: TokenData = None) -> None:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject: DbRole = dbSession.query(DbRole).filter_by(id=obj.id()).first()
            if dbObject is None:
                raise RoleDoesNotExistException(f"id = {obj.id()}")
            repoObj = self._roleFromDbObject(dbObject)
            if repoObj != obj:
                dbObject.name = obj.name()
                dbObject.title = obj.title()
                dbSession.add(dbObject)
                dbSession.commit()
        finally:
            dbSession.close()

    @debugLogger
    def roleByName(self, name: str) -> Role:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbRole).filter_by(name=name).first()
            if dbObject is None:
                raise RoleDoesNotExistException(f"name = {name}")
            return self._roleFromDbObject(dbObject=dbObject)
        finally:
            dbSession.close()

    # @debugLogger
    # def rolesByOrganizationId(
    #     self,
    #     organizationId: str,
    #     tokenData: TokenData,
    #     resultFrom: int = 0,
    #     resultSize: int = 100,
    #     order: List[dict] = None,
    # ) -> dict:
    #     dbSession = DbSession.newSession(dbEngine=self._db)
    #     try:
    #         sortData = ""
    #         if order is not None:
    #             for item in order:
    #                 sortData = f'{sortData}, {item["orderBy"]} {item["direction"]}'
    #             sortData = sortData[2:]

    #         dbItemsResult = self._db.execute(
    #             text(
    #                 f"""SELECT
    #                         role_id as id,
    #                         name as name,
    #                         title as title
    #                     FROM role
    #                     LEFT OUTER JOIN
    #                         {ROLE__ORGANIZATION__JUNCTION} role__org__junc ON role.id = role__org__junc.role_id
    #                     LEFT OUTER JOIN
    #                         organization ON organization.id = role__org__junc.organization_id
    #                     WHERE role__org__junc.organization_id = '{organizationId}'

    #                     {sortData}
    #                     LIMIT {resultSize} OFFSET {resultFrom}
    #                 """
    #             )
    #         )

    #         dbObjectsCount = self._db.execute(
    #             text(
    #                 f"""SELECT count(1) FROM role
    #                     LEFT OUTER JOIN
    #                         {ROLE__ORGANIZATION__JUNCTION} role__org__junc ON role.id = role__org__junc.role_id
    #                     LEFT OUTER JOIN
    #                         organization ON organization.id = role__org__junc.organization_id
    #                     WHERE role__org__junc.organization_id = '{organizationId}'
    #                 """
    #             )
    #         ).scalar()

    #         if dbItemsResult is None:
    #             return {"items": [], "totalItemCount": 0}
    #         return {
    #             "items": [self._roleFromDbObject(x) for x in dbItemsResult],
    #             "totalItemCount": dbObjectsCount,
    #         }
    #     finally:
    #         dbSession.close()

    @debugLogger
    def rolesByOrganizationType(
        self,
        organizationType: str,
        tokenData: TokenData,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
    ) -> dict:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            sortData = ""
            if order is not None:
                for item in order:
                    sortData = f'{sortData}, {item["orderBy"]} {item["direction"]}'
                sortData = sortData[2:]

            dbItemsResult = self._db.execute(
                text(
                    f"""SELECT
                            DISTINCT
                                role_id as id,
                                name as name,
                                title as title
                        FROM role
                        LEFT OUTER JOIN
                            {ROLE__ORGANIZATION__JUNCTION} role__org__junc ON role.id = role__org__junc.role_id
                        LEFT OUTER JOIN
                            organization ON organization.id = role__org__junc.organization_id
                        WHERE organization.organization_type = '{organizationType}'

                        {sortData}       
                        LIMIT {resultSize} OFFSET {resultFrom}                            
                    """
                )
            )

            dbObjectsCount = self._db.execute(
                text(
                    f"""SELECT count(1) FROM role
                        LEFT OUTER JOIN
                            {ROLE__ORGANIZATION__JUNCTION} role__org__junc ON role.id = role__org__junc.role_id
                        LEFT OUTER JOIN
                            organization ON organization.id = role__org__junc.organization_id
                        WHERE organization.organization_type = '{organizationType}'
                    """
                )
            ).scalar()

            if dbItemsResult is None:
                return {"items": [], "totalItemCount": 0}
            return {
                "items": [self._roleFromDbObject(x) for x in dbItemsResult],
                "totalItemCount": dbObjectsCount,
            }
        finally:
            dbSession.close()

    @debugLogger
    def roleById(self, id: str) -> Role:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbRole).filter_by(id=id).first()
            if dbObject is None:
                raise RoleDoesNotExistException(f"id = {id}")
            return self._roleFromDbObject(dbObject=dbObject)
        finally:
            dbSession.close()

    @debugLogger
    def _roleFromDbObject(self, dbObject: DbRole):
        return Role(
            id=dbObject.id,
            name=dbObject.name,
            title=dbObject.title,
        )

    @debugLogger
    def roles(
        self,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
        tokenData: TokenData = None,
    ) -> dict:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbRoles = dbSession.query(DbRole).all()
            if dbRoles is None:
                return {"items": [], "totalItemCount": 0}
            items = dbRoles
            totalItemCount = len(items)
            items = items[resultFrom : resultFrom + resultSize]
            return {
                "items": [self._roleFromDbObject(x) for x in items],
                "totalItemCount": totalItemCount,
            }
        finally:
            dbSession.close()
