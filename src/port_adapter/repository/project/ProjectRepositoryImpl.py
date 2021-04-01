"""
The file is generated by a scaffold script and modified manually
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

import os
from datetime import datetime
from typing import List

from sqlalchemy import create_engine
from sqlalchemy.sql.expression import text

from src.domain_model.project.Project import Project
from src.domain_model.project.ProjectRepository import ProjectRepository
from src.domain_model.resource.exception.ObjectIdenticalException import ObjectIdenticalException
from src.domain_model.resource.exception.ProjectDoesNotExistException import ProjectDoesNotExistException
from src.domain_model.token.TokenData import TokenData
from src.port_adapter.repository.DbSession import DbSession
from src.port_adapter.repository.db_model.Project import Project as DbProject
from src.resource.common.DateTimeHelper import DateTimeHelper
from src.resource.logging.decorator import debugLogger
from src.resource.logging.logger import logger


class ProjectRepositoryImpl(ProjectRepository):
    def __init__(self):
        try:
            self._db = create_engine(
                f"mysql+mysqlconnector://{os.getenv('CAFM_PROJECT_DB_USER', 'root')}:{os.getenv('CAFM_PROJECT_DB_PASSWORD', '1234')}@{os.getenv('CAFM_PROJECT_DB_HOST', '127.0.0.1')}:{os.getenv('CAFM_PROJECT_DB_PORT', '3306')}/{os.getenv('CAFM_PROJECT_DB_NAME', 'cafm-project')}")
        except Exception as e:
            logger.warn(f'[{ProjectRepositoryImpl.__init__.__qualname__}] Could not connect to the db, message: {e}')
            raise Exception(f'Could not connect to the db, message: {e}')

    @debugLogger
    def save(self, obj: Project, tokenData: TokenData = None):
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbProject).filter_by(id=obj.id()).first()
            if dbObject is not None:
                self.updateProject(obj=obj, tokenData=tokenData)
            else:
                self.createProject(obj=obj, tokenData=tokenData)
        finally:
            dbSession.close()

    @debugLogger
    def createProject(self, obj: Project, tokenData: TokenData = None):
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = DbProject(id=obj.id(), name=obj.name(), cityId=obj.cityId(), countryId=obj.countryId(),
                                 startDate=obj.startDate(), beneficiaryId=obj.beneficiaryId(),
                                 addressLine=obj.addressLine(), state=obj.state().value)
            result = dbSession.query(DbProject).filter_by(id=obj.id()).first()
            if result is None:
                dbSession.add(dbObject)
                dbSession.commit()
        finally:
            dbSession.close()

    @debugLogger
    def deleteProject(self, obj: Project, tokenData: TokenData = None) -> None:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbProject).filter_by(id=obj.id()).first()
            if dbObject is not None:
                dbSession.delete(dbObject)
                dbSession.commit()
        finally:
            dbSession.close()

    @debugLogger
    def updateProject(self, obj: Project, tokenData: TokenData = None) -> None:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbProject).filter_by(id=obj.id()).first()
            if dbObject is None:
                raise ProjectDoesNotExistException(f'id = {obj.id()}')
            savedObj: Project = self.projectById(obj.id())
            if savedObj != obj:
                dbObject.name = obj.name() if obj.name() is not None else dbObject.name
                dbObject.cityId = obj.cityId() if obj.cityId() is not None else dbObject.cityId
                dbObject.countryId = obj.countryId() if obj.countryId() is not None else dbObject.countryId
                dbObject.startDate = datetime.utcfromtimestamp(obj.startDate()) if obj.startDate() is not None and obj.startDate() > 0 else dbObject.startDate
                dbObject.beneficiaryId = obj.beneficiaryId() if obj.beneficiaryId() is not None else dbObject.beneficiaryId
                dbObject.addressLine = obj.addressLine() if obj.addressLine() is not None else dbObject.addressLine
                dbObject.state = obj.state().value if obj.state() is not None else dbObject.state
                dbSession.add(dbObject)
                dbSession.commit()
        finally:
            dbSession.close()

    @debugLogger
    def projectById(self, id: str) -> Project:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbProject).filter_by(id=id).first()
            if dbObject is None:
                raise ProjectDoesNotExistException(f'id = {id}')
            return Project(id=dbObject.id, name=dbObject.name, cityId=dbObject.cityId, countryId=dbObject.countryId,
                           addressLine=dbObject.addressLine, beneficiaryId=dbObject.beneficiaryId,
                           startDate=DateTimeHelper.datetimeToInt(dbObject.startDate),
                           state=Project.stateStringToProjectState(dbObject.state))
        finally:
            dbSession.close()

    @debugLogger
    def projects(self, resultFrom: int = 0, resultSize: int = 100, order: List[dict] = None,
                 tokenData: TokenData = None) -> dict:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            sortData = ''
            if order is not None:
                for item in order:
                    sortData = f'{sortData}, {item["orderBy"]} {item["direction"]}'
                sortData = sortData[2:]
            items = dbSession.query(DbProject).order_by(text(sortData)).limit(resultSize).offset(resultFrom).all()
            itemsCount = dbSession.query(DbProject).count()
            if items is None:
                return {"items": [], "itemCount": 0}
            return {"items": [Project.createFrom(id=x.id, name=x.name, cityId=x.cityId, countryId=x.countryId,
                                                 addressLine=x.addressLine, beneficiaryId=x.beneficiaryId,
                                                 startDate=DateTimeHelper.datetimeToInt(x.startDate),
                                                 state=Project.stateStringToProjectState(x.state)) for x in items],
                    "itemCount": itemsCount}
        finally:
            dbSession.close()

    @debugLogger
    def changeState(self, project: Project, tokenData: TokenData) -> None:

        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbProject).filter_by(id=project.id()).first()
            if dbObject is None:
                raise ProjectDoesNotExistException(f'id = {project.id()}')
            dbObject.state = project.state().value
            from src.domain_model.project.ProjectState import ProjectState
            if project.state() is ProjectState.ACTIVE and \
                    project.stateStringToProjectState(dbObject.state) != ProjectState.ACTIVE:
                dbObject.startDate = datetime.utcfromtimestamp(project.startDate())
            dbSession.add(dbObject)
            dbSession.commit()
        finally:
            dbSession.close()
