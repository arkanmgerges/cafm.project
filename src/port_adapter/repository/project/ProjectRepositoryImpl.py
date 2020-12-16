"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import os


from src.domain_model.project.Project import Project
from src.domain_model.resource.exception.ProjectDoesNotExistException import ProjectDoesNotExistException
from src.port_adapter.repository.db_model.Project import Project as DbProject
from src.domain_model.project.ProjectRepository import ProjectRepository
from src.domain_model.token.TokenData import TokenData
from src.resource.logging.decorator import debugLogger
from src.resource.logging.logger import logger
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session

class ProjectRepositoryImpl(ProjectRepository):
    def __init__(self):
        try:
            self._db = create_engine(
                f"mysql+mysqlconnector://{os.getenv('CAFM_PROJECT_DB_USER', 'root')}:{os.getenv('CAFM_PROJECT_DB_PASSWORD', '1234')}@{os.getenv('CAFM_PROJECT_DB_HOST', '127.0.0.1')}/{os.getenv('CAFM_PROJECT_DB_NAME', 'cafm-project')}")
            SessionFactory = sessionmaker(bind=self._db)
            self._dbSession:Session = SessionFactory()
        except Exception as e:
            logger.warn(f'[{ProjectRepositoryImpl.__init__.__qualname__}] Could not connect to the db, message: {e}')
            raise Exception(f'Could not connect to the db, message: {e}')

    @debugLogger
    def createProject(self, project: Project, tokenData: TokenData):
        obj = DbProject(id=project.id(), name=project.name(), cityId=project.cityId(),
                        countryId=project.countryId(), addressLine=project.addressLine(),
                        beneficiaryId=project.beneficiaryId())
        res = self._dbSession.query(DbProject).filter_by(id=project.id()).first()
        if res is None:
            self._dbSession.add(obj)
            self._dbSession.commit()

    @debugLogger
    def deleteProject(self, project: Project, tokenData: TokenData) -> None:
        pass

    @debugLogger
    def updateProject(self, project: Project, tokenData: TokenData) -> None:
        pass

    @debugLogger
    def projectByName(self, name: str) -> Project:
        result = self._dbSession.query(DbProject).filter_by(name=name).first()
        if result is None:
            raise ProjectDoesNotExistException(f'id = {id}')
        return Project(id=result.id, name=result.name, cityId=result.cityId, countryId=result.countryId,
                       addressLine=result.addressLine, beneficiaryId=result.beneficiaryId)

    @debugLogger
    def projectById(self, id: str) -> Project:
        result = self._dbSession.query(DbProject).filter_by(id=id).first()
        if result is None:
            raise ProjectDoesNotExistException(f'id = {id}')
        return Project(id=result.id, name=result.name, cityId=result.cityId, countryId=result.countryId,
                       addressLine=result.addressLine, beneficiaryId=result.beneficiaryId)