"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import os
from typing import List

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

from src.domain_model.role.Role import Role
from src.domain_model.role.RoleRepository import RoleRepository
from src.domain_model.resource.exception.ObjectIdenticalException import ObjectIdenticalException
from src.domain_model.resource.exception.RoleDoesNotExistException import RoleDoesNotExistException
from src.domain_model.token.TokenData import TokenData
from src.port_adapter.repository.db_model.Role import Role as DbRole
from src.resource.logging.decorator import debugLogger
from src.resource.logging.logger import logger


class RoleRepositoryImpl(RoleRepository):
    def __init__(self):
        try:
            self._db = create_engine(
                f"mysql+mysqlconnector://{os.getenv('CAFM_PROJECT_DB_USER', 'root')}:{os.getenv('CAFM_PROJECT_DB_PASSWORD', '1234')}@{os.getenv('CAFM_PROJECT_DB_HOST', '127.0.0.1')}/{os.getenv('CAFM_PROJECT_DB_NAME', 'cafm-role')}")
            SessionFactory = sessionmaker(bind=self._db)
            self._dbSession: Session = SessionFactory()
        except Exception as e:
            logger.warn(
                f'[{RoleRepositoryImpl.__init__.__qualname__}] Could not connect to the db, message: {e}')
            raise Exception(f'Could not connect to the db, message: {e}')

    @debugLogger
    def createRole(self, obj: Role, tokenData: TokenData):
        dbObject = DbRole(id=obj.id(), name=obj.name(), title=obj.title())
        result = self._dbSession.query(DbRole).filter_by(id=obj.id()).first()
        if result is None:
            self._dbSession.add(dbObject)
            self._dbSession.commit()

    @debugLogger
    def deleteRole(self, obj: Role, tokenData: TokenData) -> None:
        dbObject = self._dbSession.query(DbRole).filter_by(id=obj.id()).first()
        if dbObject is not None:
            self._dbSession.delete(dbObject)
            self._dbSession.commit()

    @debugLogger
    def updateRole(self, obj: Role, tokenData: TokenData) -> None:
        dbObject: DbRole = self._dbSession.query(DbRole).filter_by(id=obj.id()).first()
        if dbObject is None:
            raise RoleDoesNotExistException(f'id = {obj.id()}')
        repoObj = self._roleFromDbObject(dbObject)
        if repoObj == obj:
            logger.debug(
                f'[{RoleRepositoryImpl.updateRole.__qualname__}] Object identical exception for old role: {repoObj}\nrole: {obj}')
            raise ObjectIdenticalException(f'role id: {obj.id()}')
        dbObject.name = obj.name()
        self._dbSession.add(dbObject)
        self._dbSession.commit()

    @debugLogger
    def roleByName(self, name: str) -> Role:
        dbObject = self._dbSession.query(DbRole).filter_by(name=name).first()
        if dbObject is None:
            raise RoleDoesNotExistException(f'name = {name}')
        return self._roleFromDbObject(dbObject=dbObject)

    @debugLogger
    def roleById(self, id: str) -> Role:
        dbObject = self._dbSession.query(DbRole).filter_by(id=id).first()
        if dbObject is None:
            raise RoleDoesNotExistException(f'id = {id}')
        return self._roleFromDbObject(dbObject=dbObject)

    @debugLogger
    def _roleFromDbObject(self, dbObject: DbRole):
        return Role(id=dbObject.id, name=dbObject.name, title=dbObject.title)

    @debugLogger
    def roles(self, tokenData: TokenData, resultFrom: int = 0, resultSize: int = 100,
              order: List[dict] = None) -> dict:
        dbRoles = self._dbSession.query(DbRole).all()
        if dbRoles is None:
            return {"items": [], "itemCount": 0}
        items = dbRoles
        itemCount = len(items)
        items = items[resultFrom:resultFrom + resultSize]
        return {"items": [self._roleFromDbObject(x) for x in items],
                "itemCount": itemCount}
