"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import os
from typing import List

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import text

from src.domain_model.project.Project import Project
from src.domain_model.project.ProjectRepository import ProjectRepository
from src.domain_model.resource.exception.ObjectIdenticalException import ObjectIdenticalException
from src.domain_model.resource.exception.ProjectDoesNotExistException import ProjectDoesNotExistException
from src.domain_model.token.TokenData import TokenData
from src.port_adapter.repository.db_model.Project import Project as DbProject
from src.resource.logging.decorator import debugLogger
from src.resource.logging.logger import logger


class ProjectRepositoryImpl(ProjectRepository):
    def __init__(self):
        try:
            self._db = create_engine(
                f"mysql+mysqlconnector://{os.getenv('CAFM_PROJECT_DB_USER', 'root')}:{os.getenv('CAFM_PROJECT_DB_PASSWORD', '1234')}@{os.getenv('CAFM_PROJECT_DB_HOST', '127.0.0.1')}:{os.getenv('CAFM_PROJECT_DB_PORT', '3306')}/{os.getenv('CAFM_PROJECT_DB_NAME', 'cafm-project')}")
            SessionFactory = sessionmaker(bind=self._db)
            self._dbSession: Session = SessionFactory()
        except Exception as e:
            logger.warn(f'[{ProjectRepositoryImpl.__init__.__qualname__}] Could not connect to the db, message: {e}')
            raise Exception(f'Could not connect to the db, message: {e}')

    @debugLogger
    def createProject(self, obj: Project, tokenData: TokenData):
        dbObject = DbProject(id=obj.id(), name=obj.name(), cityId=obj.cityId(),
                             countryId=obj.countryId(), addressLine=obj.addressLine(),
                             beneficiaryId=obj.beneficiaryId(), state=obj.state().value)
        result = self._dbSession.query(DbProject).filter_by(id=obj.id()).first()
        if result is None:
            self._dbSession.add(dbObject)
            self._dbSession.commit()

    @debugLogger
    def deleteProject(self, obj: Project, tokenData: TokenData) -> None:
        dbObject = self._dbSession.query(DbProject).filter_by(id=obj.id()).first()
        if dbObject is not None:
            self._dbSession.delete(dbObject)
            self._dbSession.commit()

    @debugLogger
    def updateProject(self, obj: Project, tokenData: TokenData) -> None:
        dbObject = self._dbSession.query(DbProject).filter_by(id=obj.id()).first()
        if dbObject is None:
            raise ProjectDoesNotExistException(f'id = {obj.id()}')
        if dbObject == obj:
            logger.debug(
                f'[{ProjectRepositoryImpl.updateProject.__qualname__}] Object identical exception for old project: {dbObject}\nproject: {obj}')
            raise ObjectIdenticalException(f'project id: {obj.id()}')
        dbObject.name = obj.name()
        dbObject.cityId = obj.cityId()
        dbObject.countryId = obj.countryId()
        dbObject.addressLine = obj.addressLine()
        dbObject.beneficiaryId = obj.beneficiaryId()
        dbObject.state = obj.state().value
        self._dbSession.add(dbObject)
        self._dbSession.commit()

    @debugLogger
    def projectByName(self, name: str) -> Project:
        dbObject = self._dbSession.query(DbProject).filter_by(name=name).first()
        if dbObject is None:
            raise ProjectDoesNotExistException(f'name = {name}')
        return Project(id=dbObject.id, name=dbObject.name, cityId=dbObject.cityId, countryId=dbObject.countryId,
                       addressLine=dbObject.addressLine, beneficiaryId=dbObject.beneficiaryId,
                       state=Project.stateStringToProjectState(dbObject.state))

    @debugLogger
    def projectById(self, id: str) -> Project:
        dbObject = self._dbSession.query(DbProject).filter_by(id=id).first()
        if dbObject is None:
            raise ProjectDoesNotExistException(f'id = {id}')
        return Project(id=dbObject.id, name=dbObject.name, cityId=dbObject.cityId, countryId=dbObject.countryId,
                       addressLine=dbObject.addressLine, beneficiaryId=dbObject.beneficiaryId,
                       state=Project.stateStringToProjectState(dbObject.state))

    @debugLogger
    def projects(self, tokenData: TokenData, resultFrom: int = 0, resultSize: int = 100,
                 order: List[dict] = None) -> dict:
        sortData = ''
        if order is not None:
            for item in order:
                sortData = f'{sortData}, {item["orderBy"]} {item["direction"]}'
            sortData = sortData[2:]
        items = self._dbSession.query(DbProject).order_by(text(sortData)).limit(resultSize).offset(resultFrom).all()
        itemsCount = self._dbSession.query(DbProject).count()
        if items is None:
            return {"items": [], "itemCount": 0}
        return {"items": [Project.createFrom(id=x.id, name=x.name, cityId=x.cityId, countryId=x.countryId,
                                             addressLine=x.addressLine, beneficiaryId=x.beneficiaryId,
                                             state=Project.stateStringToProjectState(x.state)) for x in items],
                "itemCount": itemsCount}

    @debugLogger
    def changeState(self, project: Project, tokenData: TokenData) -> None:
        dbObject = self._dbSession.query(DbProject).filter_by(id=id).first()
        if dbObject is None:
            raise ProjectDoesNotExistException(f'id = {id}')
        dbObject.state = project.state().value
        self._dbSession.add(dbObject)
        self._dbSession.commit()
