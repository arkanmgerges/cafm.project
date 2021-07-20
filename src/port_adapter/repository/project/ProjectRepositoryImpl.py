"""
The file is generated by a scaffold script and modified manually
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from src.resource.logging.logger import logger
from typing import List

from sqlalchemy.sql.expression import text

from src.application.lifecycle.ApplicationServiceLifeCycle import ApplicationServiceLifeCycle
from src.domain_model.project.Project import Project
from src.domain_model.project.ProjectRepository import ProjectRepository
from src.domain_model.resource.exception.ProjectDoesNotExistException import (
    ProjectDoesNotExistException,
)
from src.domain_model.token.TokenData import TokenData
from src.port_adapter.repository.common.DbUtil import DbUtil
from src.port_adapter.repository.db_model.Project import Project as DbProject
from src.port_adapter.repository.db_model.City import City as DbCity

from src.port_adapter.repository.db_model.project__organization__junction import (
    PROJECT__ORGANIZATION__JUNCTION,
)
from src.resource.common.DateTimeHelper import DateTimeHelper
from src.resource.logging.decorator import debugLogger


class ProjectRepositoryImpl(ProjectRepository):
    @debugLogger
    def save(self, obj: Project, tokenData: TokenData = None):
        dbSession = ApplicationServiceLifeCycle.dbContext()
        dbObject = dbSession.query(DbProject).filter_by(id=obj.id()).first()
        if dbObject is not None:
            self.updateProject(obj=obj, dbObject=dbObject, tokenData=tokenData)
        else:
            self.createProject(obj=obj, tokenData=tokenData)

    @debugLogger
    def createProject(self, obj: Project, tokenData: TokenData = None):
        dbSession = ApplicationServiceLifeCycle.dbContext()
        dbObject = self._createDbObjectByObj(obj=obj)
        result = dbSession.query(DbProject).filter_by(id=obj.id()).first()
        if result is None:
            dbSession.add(dbObject)

    @debugLogger
    def deleteProject(self, obj: Project, tokenData: TokenData = None) -> None:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        # Project has foreign key constraints, we need to disable them then enable them
        DbUtil.disableForeignKeyChecks(dbSession=dbSession)
        dbSession.execute(text(f"""
            DELETE FROM project WHERE id = "{obj.id()}"
            """))
        DbUtil.enableForeignKeyChecks(dbSession=dbSession)

    @debugLogger
    def updateProject(self, obj: Project, dbObject: DbProject = None, tokenData: TokenData = None) -> None:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        cityInfo = dbSession.query(DbCity).filter_by(
            geoNameId=obj.cityId()).first()
        devCityInfo = dbSession.query(DbCity).filter_by(
            geoNameId=obj.developerCityId()).first()

        obj.update(data={
            'country_state_name': cityInfo.subdivisionOneIsoName if cityInfo is not None else None,
            'country_state_iso_code': cityInfo.subdivisionOneIsoCode if cityInfo is not None else None,
            'developer_country_state_name': devCityInfo.subdivisionOneIsoName if devCityInfo is not None else None,
            'developer_country_state_iso_code': devCityInfo.subdivisionOneIsoCode if devCityInfo is not None else None,
        })

        if dbObject is None:
            raise ProjectDoesNotExistException(f"id = {obj.id()}")
        dbObject = self._updateDbObjectByObj(dbObject=dbObject, obj=obj)
        dbSession.add(dbObject)

    @debugLogger
    def bulkSave(self, objList: List[Project], tokenData: TokenData = None):
        dbSession = ApplicationServiceLifeCycle.dbContext()
        for obj in objList:
            cityInfo = dbSession.query(DbCity).filter_by(
                geoNameId=obj.cityId()).first()
            devCityInfo = dbSession.query(DbCity).filter_by(
                geoNameId=obj.developerCityId()).first()

            obj.update(data={
                'country_state_name': cityInfo.subdivisionOneIsoName if cityInfo is not None else None,
                'country_state_iso_code': cityInfo.subdivisionOneIsoCode if cityInfo is not None else None,
                'developer_country_state_name': devCityInfo.subdivisionOneIsoName if devCityInfo is not None else None,
                'developer_country_state_iso_code': devCityInfo.subdivisionOneIsoCode if devCityInfo is not None else None,
            })

            dbObject = dbSession.query(
               DbProject).filter_by(id=obj.id()).first()
            if dbObject is not None:
                dbObject = self._updateDbObjectByObj(
                    dbObject=dbObject, obj=obj)
            else:
                dbObject = self._createDbObjectByObj(obj=obj)
            dbSession.add(dbObject)

    @debugLogger
    def bulkDelete(self, objList: List[Project], tokenData: TokenData = None) -> None:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        for obj in objList:
            dbObject = dbSession.query(
                DbProject).filter_by(id=obj.id()).first()
            if dbObject is not None:
                dbSession.delete(dbObject)

    @debugLogger
    def projectById(self, id: str) -> Project:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        dbObject = dbSession.query(DbProject).filter_by(id=id).first()
        if dbObject is None:
            raise ProjectDoesNotExistException(f"id = {id}")
        return self._projectFromDbObject(dbObject)

    @debugLogger
    def projects(
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
        items = dbSession.query(DbProject).order_by(
            text(sortData)).limit(resultSize).offset(resultFrom).all()
        itemsCount = dbSession.query(DbProject).count()
        if items is None:
            return {"items": [], "totalItemCount": 0}
        return {
            "items": [self._projectFromDbObject(x) for x in items],
            "totalItemCount": itemsCount,
        }

    @debugLogger
    def projectsFilteredByProjectList(self, tokenData: TokenData, resultFrom: int = 0, resultSize: int = 10,
                                      order: List[dict] = None, projectList: List[Project] = None) -> dict:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        sortData = ""
        if order is not None:
            for item in order:
                sortData = f'{sortData}, {item["orderBy"]} {item["direction"]}'
            sortData = sortData[2:]
        items = dbSession.query(DbProject).filter(DbProject.id.in_([x.id() for x in projectList])).order_by(
            text(sortData)).limit(resultSize).offset(resultFrom).all()
        itemsCount = dbSession.query(DbProject).filter(DbProject.id.in_([x.id() for x in projectList])).count()
        if items is None:
            return {"items": [], "totalItemCount": 0}
        return {
            "items": [self._projectFromDbObject(x) for x in items],
            "totalItemCount": itemsCount,
        }

    @debugLogger
    def projectsByStateFilteredByProjectList(self, tokenData: TokenData, state: str = '',
                                             resultFrom: int = 0, resultSize: int = 10,
                                      order: List[dict] = None, projectList: List[Project] = None) -> dict:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        sortData = ""
        if order is not None:
            for item in order:
                sortData = f'{sortData}, {item["orderBy"]} {item["direction"]}'
            sortData = sortData[2:]
        items = dbSession.query(DbProject).filter(DbProject.id.in_([x.id() for x in projectList])).filter_by(state=state).order_by(
            text(sortData)).limit(resultSize).offset(resultFrom).all()
        itemsCount = dbSession.query(DbProject).filter(DbProject.id.in_([x.id() for x in projectList])).filter_by(state=state).count()
        if items is None:
            return {"items": [], "totalItemCount": 0}
        return {
            "items": [self._projectFromDbObject(x) for x in items],
            "totalItemCount": itemsCount,
        }

    @debugLogger
    def projectsByState(
        self,
        state: str = None,
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
            dbSession.query(DbProject)
            .filter_by(state=state)
            .order_by(text(sortData))
            .limit(resultSize)
            .offset(resultFrom)
            .all()
        )
        itemsCount = dbSession.query(DbProject).filter_by(state=state).count()
        if items is None:
            return {"items": [], "totalItemCount": 0}
        return {
            "items": [self._projectFromDbObject(x) for x in items],
            "totalItemCount": itemsCount,
        }

    @debugLogger
    def projectsByOrganizationId(
        self,
        organizationId: str,
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

        items = dbSession.execute(
            text(
                f"""SELECT
                        project_id as id,
                        project.name as name,
                        project.city_id as cityId,
                        project.country_id as countryId,
                        project.address_line as addressLine,
                        project.address_line_two as addressLineTwo,
                        project.beneficiary_id as beneficiaryId,
                        project.start_date as startDate,
                        project.postal_code as postalCode,
                        project.subdivision_1_iso_code as countryStateIsoCode,
                        project.subdivision_1_name as countryStateName,
                        project.state as state,
                        project.developer_name as developerName,
                        project.developer_city_id as developerCityId,
                        project.developer_country_id as developerCountryId,
                        project.developer_address_line_one as developerAddressLineOne,
                        project.developer_address_line_two as developerAddressLineTwo,
                        project.developer_contact_person as developerContactPerson,
                        project.developer_email as developerEmail,
                        project.developer_phone_number as developerPhone,
                        project.developer_warranty as developerWarranty,
                        project.developer_postal_code as developerPostalCode
                        project.developer_subdivision_1_iso_code as developerCountryStateIsoCode,
                        project.developer_subdivision_1_name as developerCountryStateName
                    FROM project
                    LEFT OUTER JOIN
                        {PROJECT__ORGANIZATION__JUNCTION} project__organization__junction ON project.id = project__organization__junction.project_id
                    LEFT OUTER JOIN
                        organization ON organization.id = project__organization__junction.organization_id
                    WHERE project__organization__junction.organization_id = '{organizationId}'

                    {sortData}
                    LIMIT {resultSize} OFFSET {resultFrom}
                """
            )
        )

        itemsCount = dbSession.execute(
            text(
                f"""SELECT count(1) FROM project
                    LEFT OUTER JOIN
                        {PROJECT__ORGANIZATION__JUNCTION} project__organization__junction ON project.id = project__organization__junction.project_id
                    LEFT OUTER JOIN
                        organization ON organization.id = project__organization__junction.organization_id
                    WHERE project__organization__junction.organization_id = '{organizationId}'
                """
            )
        ).scalar()

        if items is None:
            return {"items": [], "totalItemCount": 0}
        return {
            "items": [self._projectFromDbObject(x) for x in items],
            "totalItemCount": itemsCount,
        }

    @debugLogger
    def changeState(self, project: Project, tokenData: TokenData) -> None:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        dbObject = dbSession.query(DbProject).filter_by(
            id=project.id()).first()
        if dbObject is None:
            raise ProjectDoesNotExistException(f"id = {project.id()}")
        dbObject.state = project.state().value
        from src.domain_model.project.ProjectState import ProjectState

        if (
            project.state() is ProjectState.ACTIVE
            and project.stateStringToProjectState(dbObject.state) != ProjectState.ACTIVE
        ):
            dbObject.startDate = DateTimeHelper.intToDateTime(
                project.startDate())
        dbSession.add(dbObject)

    def _updateDbObjectByObj(self, dbObject: DbProject, obj: Project):
        dbObject.name = obj.name() if obj.name() is not None else dbObject.name
        dbObject.cityId = obj.cityId() if obj.cityId() is not None else dbObject.cityId
        dbObject.countryId = obj.countryId() if obj.countryId(
        ) is not None else dbObject.countryId
        dbObject.startDate = (
            DateTimeHelper.intToDateTime(obj.startDate())
            if obj.startDate() is not None and obj.startDate() > 0
            else dbObject.startDate
        )
        dbObject.beneficiaryId = obj.beneficiaryId(
        ) if obj.beneficiaryId() is not None else dbObject.beneficiaryId
        dbObject.postalCode = obj.postalCode() if obj.postalCode(
        ) is not None else dbObject.postalCode
        dbObject.addressLine = obj.addressLine(
        ) if obj.addressLine() is not None else dbObject.addressLine
        # dbObject.state = (
        #     obj.state().value if obj.state() is not None else dbObject.state
        # )
        # Note: state will remain the same as it is in the database. It can be updated only through changeState
        dbObject.addressLineTwo = obj.addressLineTwo(
        ) if obj.addressLineTwo() is not None else dbObject.addressLineTwo
        dbObject.developerName = obj.developerName(
        ) if obj.developerName() is not None else dbObject.developerName
        dbObject.developerCityId = (
            obj.developerCityId() if obj.developerCityId(
            ) is not None else dbObject.developerCityId
        )
        dbObject.developerCountryId = (
            obj.developerCountryId() if obj.developerCountryId(
            ) is not None else dbObject.developerCountryId
        )
        dbObject.developerAddressLineOne = (
            obj.developerAddressLineOne()
            if obj.developerAddressLineOne() is not None
            else dbObject.developerAddressLineOne
        )
        dbObject.developerAddressLineTwo = (
            obj.developerAddressLineTwo()
            if obj.developerAddressLineTwo() is not None
            else dbObject.developerAddressLineTwo
        )
        dbObject.developerContactPerson = (
            obj.developerContact() if obj.developerContact(
            ) is not None else dbObject.developerContactPerson
        )
        dbObject.developerEmail = obj.developerEmail(
        ) if obj.developerEmail() is not None else dbObject.developerEmail
        dbObject.developerPhone = (
            obj.developerPhoneNumber() if obj.developerPhoneNumber(
            ) is not None else dbObject.developerPhone
        )
        dbObject.developerWarranty = (
            obj.developerWarranty() if obj.developerWarranty(
            ) is not None else dbObject.developerWarranty
        )
        dbObject.developerPostalCode = (
            obj.developerPostalCode() if obj.developerPostalCode(
            ) is not None else dbObject.developerPostalCode
        )

        dbObject.countryStateName = obj.countryStateName(
        ) if obj.countryStateName() is not None else dbObject.countryStateName
        dbObject.countryStateIsoCode = obj.countryStateIsoCode(
        ) if obj.countryStateIsoCode() is not None else dbObject.countryStateIsoCode
        dbObject.developerCountryStateName = obj.developerCountryStateName(
        ) if obj.developerCountryStateName() is not None else dbObject.developerCountryStateName
        dbObject.developerCountryStateIsoCode = obj.developerCountryStateIsoCode(
        ) if obj.developerCountryStateIsoCode() is not None else dbObject.developerCountryStateIsoCode

        return dbObject

    def _createDbObjectByObj(self, obj: Project):
        return DbProject(
            id=obj.id(),
            name=obj.name(),
            cityId=obj.cityId(),
            countryId=obj.countryId(),
            startDate=DateTimeHelper.intToDateTime(obj.startDate())
            if obj.startDate() is not None and obj.startDate() > 0
            else None,
            beneficiaryId=obj.beneficiaryId(),
            postalCode=obj.postalCode(),
            countryStateName=obj.countryStateName(),
            countryStateIsoCode=obj.countryStateIsoCode(),
            addressLine=obj.addressLine(),
            state=obj.state().value,
            addressLineTwo=obj.addressLineTwo(),
            developerName=obj.developerName(),
            developerCityId=obj.developerCityId(),
            developerCountryId=obj.developerCountryId(),
            developerAddressLineOne=obj.developerAddressLineOne(),
            developerAddressLineTwo=obj.developerAddressLineTwo(),
            developerContactPerson=obj.developerContact(),
            developerEmail=obj.developerEmail(),
            developerPhone=obj.developerPhoneNumber(),
            developerWarranty=obj.developerWarranty(),
            developerPostalCode=obj.developerPostalCode(),
            developerCountryStateName=obj.developerCountryStateName(),
            developerCountryStateIsoCode=obj.developerCountryStateIsoCode(),
        )

    @debugLogger
    def _projectFromDbObject(self, dbObject: DbProject):
        return Project.createFrom(
            id=dbObject.id,
            name=dbObject.name,
            cityId=dbObject.cityId,
            countryId=dbObject.countryId,
            addressLine=dbObject.addressLine,
            addressLineTwo=dbObject.addressLineTwo,
            beneficiaryId=dbObject.beneficiaryId,
            postalCode=dbObject.postalCode,
            countryStateName=dbObject.countryStateName,
            countryStateIsoCode=dbObject.countryStateIsoCode,
            startDate=DateTimeHelper.datetimeToInt(dbObject.startDate),
            state=Project.stateStringToProjectState(dbObject.state),
            developerName=dbObject.developerName,
            developerCityId=dbObject.developerCityId,
            developerCountryId=dbObject.developerCountryId,
            developerAddressLineOne=dbObject.developerAddressLineOne,
            developerAddressLineTwo=dbObject.developerAddressLineTwo,
            developerContact=dbObject.developerContactPerson,
            developerEmail=dbObject.developerEmail,
            developerPhoneNumber=dbObject.developerPhone,
            developerWarranty=dbObject.developerWarranty,
            developerPostalCode=dbObject.developerPostalCode,
            developerCountryStateName=dbObject.developerCountryStateName,
            developerCountryStateIsoCode=dbObject.developerCountryStateIsoCode,
            modifiedAt=DateTimeHelper.datetimeToInt(dbObject.modifiedAt) if dbObject.modifiedAt is not None else 0,
            createdAt=DateTimeHelper.datetimeToInt(dbObject.createdAt) if dbObject.createdAt is not None else 0,
        )
