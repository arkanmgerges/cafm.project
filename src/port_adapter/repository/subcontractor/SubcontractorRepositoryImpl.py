"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

import os
from typing import List

from sqlalchemy import create_engine
from sqlalchemy.sql.expression import text

from src.domain_model.organization.Organization import Organization
from src.domain_model.subcontractor.Subcontractor import Subcontractor
from src.domain_model.subcontractor.SubcontractorRepository import (
    SubcontractorRepository,
)
from src.domain_model.resource.exception.SubcontractorDoesNotExistException import (
    SubcontractorDoesNotExistException,
)
from src.domain_model.token.TokenData import TokenData
from src.port_adapter.repository.DbSession import DbSession
from src.port_adapter.repository.db_model.Organization import (
    Organization as DbOrganization,
)
from src.port_adapter.repository.db_model.Subcontractor import (
    Subcontractor as DbSubcontractor,
)
from src.port_adapter.repository.db_model.SubcontractorCategory import (
    SubcontractorCategory as DbSubcontractorCategory,
)
from src.port_adapter.repository.db_model.subcontractor__organization__junction import (
    SUBCONTRACTOR__ORGANIZATION__JUNCTION,
)
from src.resource.logging.decorator import debugLogger
from src.resource.logging.logger import logger


class SubcontractorRepositoryImpl(SubcontractorRepository):
    def __init__(self):
        try:
            self._db = create_engine(
                f"mysql+mysqlconnector://{os.getenv('CAFM_PROJECT_DB_USER', 'root')}:{os.getenv('CAFM_PROJECT_DB_PASSWORD', '1234')}@{os.getenv('CAFM_PROJECT_DB_HOST', '127.0.0.1')}:{os.getenv('CAFM_PROJECT_DB_PORT', '3306')}/{os.getenv('CAFM_PROJECT_DB_NAME', 'cafm-project')}"
            )
        except Exception as e:
            logger.warn(
                f"[{SubcontractorRepositoryImpl.__init__.__qualname__}] Could not connect to the db, message: {e}"
            )
            raise Exception(f"Could not connect to the db, message: {e}")

    @debugLogger
    def save(self, obj: Subcontractor, tokenData: TokenData = None):
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbSubcontractor).filter_by(id=obj.id()).first()
            if dbObject is not None:
                self.updateSubcontractor(
                    obj=obj, dbObject=dbObject, tokenData=tokenData
                )
            else:
                self.createSubcontractor(obj=obj, tokenData=tokenData)
        finally:
            dbSession.close()

    @debugLogger
    def createSubcontractor(self, obj: Subcontractor, tokenData: TokenData = None):
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = self._createDbObjectByObj(obj=obj)
            result = dbSession.query(DbSubcontractor).filter_by(id=obj.id()).first()
            if result is None:
                dbSession.add(dbObject)
                dbSession.commit()
        finally:
            dbSession.close()

    @debugLogger
    def deleteSubcontractor(
        self, obj: Subcontractor, tokenData: TokenData = None
    ) -> None:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbSubcontractor).filter_by(id=obj.id()).first()
            if dbObject is not None:
                dbSession.delete(dbObject)
                dbSession.commit()
        finally:
            dbSession.close()

    @debugLogger
    def updateSubcontractor(
        self,
        obj: Subcontractor,
        dbObject: DbSubcontractor = None,
        tokenData: TokenData = None,
    ) -> None:
        from sqlalchemy import inspect

        dbSession = inspect(dbObject).session
        if dbObject is None:
            raise SubcontractorDoesNotExistException(f"id = {obj.id()}")
        dbSession.add(self._updateDbObjectByObj(dbObject=dbObject, obj=obj))
        dbSession.commit()

    @debugLogger
    def bulkSave(self, objList: List[Subcontractor], tokenData: TokenData = None):
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            for obj in objList:
                dbObject = (
                    dbSession.query(DbSubcontractor).filter_by(id=obj.id()).first()
                )
                if dbObject is not None:
                    dbObject = self._updateDbObjectByObj(dbObject=dbObject, obj=obj)
                else:
                    dbObject = self._createDbObjectByObj(obj=obj)
                dbSession.add(dbObject)
            dbSession.commit()
        finally:
            dbSession.close()

    @debugLogger
    def bulkDelete(
        self, objList: List[Subcontractor], tokenData: TokenData = None
    ) -> None:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            for obj in objList:
                dbObject = (
                    dbSession.query(DbSubcontractor).filter_by(id=obj.id()).first()
                )
                if dbObject is not None:
                    dbSession.delete(dbObject)
            dbSession.commit()
        finally:
            dbSession.close()

    @debugLogger
    def assignSubcontractorToOrganization(
        self,
        subcontractor: Subcontractor,
        organization: Organization,
        tokenData: TokenData,
    ):
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbSubcontractorObject = (
                dbSession.query(DbSubcontractor)
                .filter_by(id=subcontractor.id())
                .first()
            )
            if dbSubcontractorObject is not None:
                dbOrganizationObject = (
                    dbSession.query(DbOrganization)
                    .filter_by(id=organization.id())
                    .first()
                )
                if dbOrganizationObject is not None:
                    dbSubcontractorObject.organizations.append(dbOrganizationObject)
                    dbSession.commit()
        finally:
            dbSession.close()

    @debugLogger
    def revokeRoleToUserAssignment(
        self,
        subcontractor: Subcontractor,
        organization: Organization,
        tokenData: TokenData,
    ):

        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbSubcontractorObject = (
                dbSession.query(DbSubcontractor)
                .filter_by(id=subcontractor.id())
                .first()
            )
            if dbSubcontractorObject is not None:
                dbOrganizationObject = (
                    dbSession.query(DbOrganization)
                    .filter_by(id=organization.id())
                    .first()
                )
                if dbOrganizationObject is not None:
                    for obj in dbSubcontractorObject.organizations:
                        if obj.id == organization.id():
                            dbSubcontractorObject.organizations.remove(obj)
                    dbSession.commit()
        finally:
            dbSession.close()

    @debugLogger
    def subcontractorById(self, id: str) -> Subcontractor:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbSubcontractor).filter_by(id=id).first()
            if dbObject is None:
                raise SubcontractorDoesNotExistException(f"id = {id}")
            return self._subcontractorFromDbObject(dbObject=dbObject)
        finally:
            dbSession.close()

    @debugLogger
    def subcontractorByName(self, companyName: str) -> Subcontractor:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = (
                dbSession.query(DbSubcontractor)
                .filter_by(companyName=companyName)
                .first()
            )
            if dbObject is None:
                raise SubcontractorDoesNotExistException(f"companyName = {companyName}")
            return self._subcontractorFromDbObject(dbObject=dbObject)
        finally:
            dbSession.close()

    @debugLogger
    def subcontractors(
        self,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
        tokenData: TokenData = None,
    ) -> dict:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            sortData = ""
            if order is not None:
                for item in order:
                    sortData = f'{sortData}, {item["orderBy"]} {item["direction"]}'
                sortData = sortData[2:]
            items = (
                dbSession.query(DbSubcontractor)
                .order_by(text(sortData))
                .limit(resultSize)
                .offset(resultFrom)
                .all()
            )
            itemsCount = dbSession.query(DbSubcontractor).count()
            if items is None:
                return {"items": [], "totalItemCount": 0}
            x = [self._subcontractorFromDbObject(x) for x in items]
            logger.info(f"___________________________________________________\n {x}")
            return {
                "items": x,
                "totalItemCount": itemsCount,
            }

        finally:
            dbSession.close()

    @debugLogger
    def subcontractorsBySubcontractorCategoryId(
        self,
        subcontractorCategoryId: str = None,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
        tokenData: TokenData = None,
    ) -> dict:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            sortData = ""
            if order is not None:
                for item in order:
                    sortData = f'{sortData}, {item["orderBy"]} {item["direction"]}'
                sortData = sortData[2:]
            items = (
                dbSession.query(DbSubcontractor)
                .join(DbSubcontractorCategory)
                .filter(DbSubcontractorCategory.id == subcontractorCategoryId)
                .order_by(text(sortData))
                .limit(resultSize)
                .offset(resultFrom)
                .all()
            )
            itemsCount = (
                dbSession.query(DbSubcontractor)
                .join(DbSubcontractorCategory)
                .filter(DbSubcontractorCategory.id == subcontractorCategoryId)
                .count()
            )
            if items is None:
                return {"items": [], "totalItemCount": 0}
            return {
                "items": [self._subcontractorFromDbObject(x) for x in items],
                "totalItemCount": itemsCount,
            }
        finally:
            dbSession.close()

    @debugLogger
    def subcontractorsByOrganizationId(
        self,
        organizationId: str,
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
                            subcontractor_id as id,
                            website as websiteUrl,
                            company_name as companyName, 
                            contact_person as contactPerson,
                            email,
                            phone_number as phoneNumber,
                            subcontractor.address_one as addressOne, 
                            subcontractor.address_two as addressTwo,
                            subcontractor_category_id as subcontractorCategoryId,
                            subcontractor.description,
                            subcontractor.country_id as countryId,
                            subcontractor.city_id as cityId,
                            subcontractor.state_id as stateId,
                            subcontractor.postal_code as postalCode 
                        FROM subcontractor
                        LEFT OUTER JOIN
                            {SUBCONTRACTOR__ORGANIZATION__JUNCTION} subcon__org__junction ON subcontractor.id = subcon__org__junction.subcontractor_id
                        LEFT OUTER JOIN
                            organization ON organization.id = subcon__org__junction.organization_id
                        WHERE subcon__org__junction.organization_id = '{organizationId}'

                        {sortData}       
                        LIMIT {resultSize} OFFSET {resultFrom}                            
            """
                )
            )

            dbObjectsCount = self._db.execute(
                text(
                    f"""SELECT count(1) FROM subcontractor
                        LEFT OUTER JOIN
                            {SUBCONTRACTOR__ORGANIZATION__JUNCTION} subcon__org__junction ON subcontractor.id = subcon__org__junction.subcontractor_id
                        LEFT OUTER JOIN
                            organization ON organization.id = subcon__org__junction.organization_id         
                        WHERE subcon__org__junction.organization_id = '{organizationId}'                        
            """
                )
            ).scalar()

            if dbItemsResult is None:
                return {"items": [], "totalItemCount": 0}
            return {
                "items": [self._subcontractorFromDbObject(x) for x in dbItemsResult],
                "totalItemCount": dbObjectsCount,
            }
        finally:
            dbSession.close()

    @debugLogger
    def _subcontractorFromDbObject(self, dbObject: DbSubcontractor):
        return Subcontractor(
            id=dbObject.id,
            companyName=dbObject.companyName,
            websiteUrl=dbObject.websiteUrl,
            contactPerson=dbObject.contactPerson,
            email=dbObject.email,
            phoneNumber=dbObject.phoneNumber,
            addressOne=dbObject.addressOne,
            addressTwo=dbObject.addressTwo,
            subcontractorCategoryId=dbObject.subcontractorCategoryId,
            description=dbObject.description,
            cityId=dbObject.cityId,
            countryId=dbObject.countryId,
            stateId=dbObject.stateId,
            postalCode=dbObject.postalCode,
        )

    def _updateDbObjectByObj(self, dbObject: DbSubcontractor, obj: Subcontractor):
        dbObject.companyName = (
            obj.companyName() if obj.companyName() is not None else dbObject.companyName
        )
        dbObject.websiteUrl = (
            obj.websiteUrl() if obj.websiteUrl() is not None else dbObject.websiteUrl
        )
        dbObject.contactPerson = (
            obj.contactPerson()
            if obj.contactPerson() is not None
            else dbObject.contactPerson
        )
        dbObject.email = obj.email() if obj.email() is not None else dbObject.email
        dbObject.phoneNumber = (
            obj.phoneNumber() if obj.phoneNumber() is not None else dbObject.phoneNumber
        )
        dbObject.addressOne = (
            obj.addressOne() if obj.addressOne() is not None else dbObject.addressOne
        )
        dbObject.addressTwo = (
            obj.addressTwo() if obj.addressTwo() is not None else dbObject.addressTwo
        )
        dbObject.subcontractorCategoryId = (
            obj.subcontractorCategoryId()
            if obj.subcontractorCategoryId() is not None
            else dbObject.subcontractorCategoryId
        )
        dbObject.description = (
            obj.description() if obj.description() is not None else dbObject.description
        )
        dbObject.cityId = obj.cityId() if obj.cityId() is not None else dbObject.cityId
        dbObject.countryId = (
            obj.countryId() if obj.countryId() is not None else dbObject.countryId
        )
        dbObject.stateId = (
            obj.stateId() if obj.stateId() is not None else dbObject.stateId
        )
        dbObject.postalCode = (
            obj.postalCode() if obj.postalCode() is not None else dbObject.postalCode
        )

    def _createDbObjectByObj(self, obj: Subcontractor):
        return DbSubcontractor(
            id=obj.id(),
            companyName=obj.companyName(),
            websiteUrl=obj.websiteUrl(),
            contactPerson=obj.contactPerson(),
            email=obj.email(),
            phoneNumber=obj.phoneNumber(),
            addressOne=obj.addressOne(),
            addressTwo=obj.addressTwo(),
            subcontractorCategoryId=obj.subcontractorCategoryId(),
            description=obj.description(),
            cityId=obj.cityId(),
            countryId=obj.countryId(),
            stateId=obj.stateId(),
            postalCode=obj.postalCode(),
        )
