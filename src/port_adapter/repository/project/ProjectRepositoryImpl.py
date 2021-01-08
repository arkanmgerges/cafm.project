"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import os
from typing import List

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

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
    def createProject(self, project: Project, tokenData: TokenData):
        dbObject = DbProject(id=project.id(), name=project.name(), cityId=project.cityId(),
                             countryId=project.countryId(), addressLine=project.addressLine(),
                             beneficiaryId=project.beneficiaryId(), state=project.state().value)
        result = self._dbSession.query(DbProject).filter_by(id=project.id()).first()
        if result is None:
            self._dbSession.add(dbObject)
            self._dbSession.commit()

    @debugLogger
    def deleteProject(self, project: Project, tokenData: TokenData) -> None:
        dbObject = self._dbSession.query(DbProject).filter_by(id=project.id()).first()
        if dbObject is not None:
            self._dbSession.delete(dbObject)
            self._dbSession.commit()

    @debugLogger
    def updateProject(self, project: Project, tokenData: TokenData) -> None:
        oldObject = self._dbSession.query(DbProject).filter_by(id=project.id()).first()
        if oldObject is None:
            raise ProjectDoesNotExistException(f'id = {project.id()}')
        if oldObject == project:
            logger.debug(
                f'[{ProjectRepositoryImpl.updateProject.__qualname__}] Object identical exception for old project: {oldObject}\nproject: {project}')
            raise ObjectIdenticalException(f'project id: {project.id()}')
        oldObject.name = project.name()
        oldObject.cityId = project.cityId()
        oldObject.countryId = project.countryId()
        oldObject.addressLine = project.addressLine()
        oldObject.beneficiaryId = project.beneficiaryId()
        oldObject.state = project.state().value
        self._dbSession.add(oldObject)
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
        dbProjects = self._dbSession.query(DbProject).all()
        if dbProjects is None:
            return {"items": [], "itemCount": 0}
        items = dbProjects
        itemCount = len(items)
        items = items[resultFrom:resultFrom + resultSize]
        return {"items": [Project.createFrom(id=x.id, name=x.name, cityId=x.cityId, countryId=x.countryId,
                                             addressLine=x.addressLine, beneficiaryId=x.beneficiaryId,
                                             state=Project.stateStringToProjectState(x.state)) for x in items],
                "itemCount": itemCount}

    @debugLogger
    def changeState(self, project: Project, tokenData: TokenData) -> None:
        dbObject = self._dbSession.query(DbProject).filter_by(id=id).first()
        if dbObject is None:
            raise ProjectDoesNotExistException(f'id = {id}')
        dbObject.state = project.state().value
        self._dbSession.add(dbObject)
        self._dbSession.commit()
