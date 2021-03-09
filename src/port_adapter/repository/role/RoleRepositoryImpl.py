"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import os
from typing import List

from sqlalchemy import create_engine

from src.domain_model.resource.exception.ObjectIdenticalException import ObjectIdenticalException
from src.domain_model.resource.exception.RoleDoesNotExistException import RoleDoesNotExistException
from src.domain_model.role.Role import Role
from src.domain_model.role.RoleRepository import RoleRepository
from src.domain_model.token.TokenData import TokenData
from src.port_adapter.repository.DbSession import DbSession
from src.port_adapter.repository.db_model.Role import Role as DbRole
from src.resource.logging.decorator import debugLogger
from src.resource.logging.logger import logger


class RoleRepositoryImpl(RoleRepository):
    def __init__(self):
        try:
            self._db = create_engine(
                f"mysql+mysqlconnector://{os.getenv('CAFM_PROJECT_DB_USER', 'root')}:{os.getenv('CAFM_PROJECT_DB_PASSWORD', '1234')}@{os.getenv('CAFM_PROJECT_DB_HOST', '127.0.0.1')}/{os.getenv('CAFM_PROJECT_DB_NAME', 'cafm-role')}")
        except Exception as e:
            logger.warn(
                f'[{RoleRepositoryImpl.__init__.__qualname__}] Could not connect to the db, message: {e}')
            raise Exception(f'Could not connect to the db, message: {e}')

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
                raise RoleDoesNotExistException(f'id = {obj.id()}')
            repoObj = self._roleFromDbObject(dbObject)
            if repoObj != obj:
                dbObject.name = obj.name()
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
                raise RoleDoesNotExistException(f'name = {name}')
            return self._roleFromDbObject(dbObject=dbObject)
        finally:
            dbSession.close()

    @debugLogger
    def roleById(self, id: str) -> Role:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbRole).filter_by(id=id).first()
            if dbObject is None:
                raise RoleDoesNotExistException(f'id = {id}')
            return self._roleFromDbObject(dbObject=dbObject)
        finally:
            dbSession.close()

    @debugLogger
    def _roleFromDbObject(self, dbObject: DbRole):
        return Role(id=dbObject.id, name=dbObject.name, title=dbObject.title)

    @debugLogger
    def roles(self, resultFrom: int = 0, resultSize: int = 100,
              order: List[dict] = None, tokenData: TokenData = None) -> dict:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbRoles = dbSession.query(DbRole).all()
            if dbRoles is None:
                return {"items": [], "itemCount": 0}
            items = dbRoles
            itemCount = len(items)
            items = items[resultFrom:resultFrom + resultSize]
            return {"items": [self._roleFromDbObject(x) for x in items],
                    "itemCount": itemCount}
        finally:
            dbSession.close()