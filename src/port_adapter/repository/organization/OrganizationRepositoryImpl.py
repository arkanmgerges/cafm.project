"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from src.domain_model.project.building.level.room.BuildingLevelRoom import BuildingLevelRoom
from src.domain_model.project.building.level.BuildingLevel import BuildingLevel
from src.domain_model.project.building.Building import Building
from typing import List

from sqlalchemy.sql.expression import text

from src.application.lifecycle.ApplicationServiceLifeCycle import ApplicationServiceLifeCycle
from src.domain_model.organization.Organization import Organization
from src.domain_model.organization.OrganizationRepository import OrganizationRepository
from src.domain_model.resource.exception.OrganizationDoesNotExistException import (
    OrganizationDoesNotExistException,
)
from src.domain_model.token.TokenData import TokenData
from src.port_adapter.repository.db_model.City import City as DbCity
from src.port_adapter.repository.db_model.Organization import (
    Organization as DbOrganization,
)
from src.port_adapter.repository.db_model.organization__building__junction import ORGANIZATION__BUILDING__JUNCTION

from src.resource.logging.decorator import debugLogger


class OrganizationRepositoryImpl(OrganizationRepository):
    @debugLogger
    def bulkSave(self, objList: List[Organization], tokenData: TokenData = None):
        dbSession = ApplicationServiceLifeCycle.dbContext()
        for obj in objList:
            cityInfo = dbSession.query(DbCity).filter_by(
                geoNameId=obj.cityId()).first()

            obj.update(data={
                'country_state_name': cityInfo.subdivisionOneIsoName if cityInfo is not None else None,
                'country_state_iso_code': cityInfo.subdivisionOneIsoCode if cityInfo is not None else None,
            })

            dbObject = (
                dbSession.query(DbOrganization).filter_by(id=obj.id()).first()
            )
            if dbObject is not None:
                dbObject = self._updateDbObjectByObj(
                    dbObject=dbObject, obj=obj)
            else:
                dbObject = self._createDbObjectByObj(obj=obj)
            dbSession.add(dbObject)

    @debugLogger
    def bulkDelete(
        self, objList: List[Organization], tokenData: TokenData = None
    ) -> None:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        for obj in objList:
            dbObject = (
                dbSession.query(DbOrganization).filter_by(id=obj.id()).first()
            )
            if dbObject is not None:
                dbSession.delete(dbObject)

    @debugLogger
    def save(self, obj: Organization, tokenData: TokenData = None):
        dbSession = ApplicationServiceLifeCycle.dbContext()
        cityInfo = dbSession.query(DbCity).filter_by(
            geoNameId=obj.cityId()).first()

        obj.update(data={
            'country_state_name': cityInfo.subdivisionOneIsoName if cityInfo is not None else None,
            'country_state_iso_code': cityInfo.subdivisionOneIsoCode if cityInfo is not None else None,
        })

        dbObject = dbSession.query(
            DbOrganization).filter_by(id=obj.id()).first()
        if dbObject is not None:
            self.updateOrganization(
                obj=obj, dbObject=dbObject, tokenData=tokenData)
        else:
            self.createOrganization(obj=obj, tokenData=tokenData)

    @debugLogger
    def createOrganization(self, obj: Organization, tokenData: TokenData = None):
        dbSession = ApplicationServiceLifeCycle.dbContext()
        dbObject = self._createDbObjectByObj(obj=obj)
        dbSession.add(dbObject)

    @debugLogger
    def deleteOrganization(
        self, obj: Organization, tokenData: TokenData = None
    ) -> None:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        dbObject = dbSession.query(
            DbOrganization).filter_by(id=obj.id()).first()
        if dbObject is not None:
            dbSession.delete(dbObject)

    @debugLogger
    def updateOrganization(
        self, obj: Organization, dbObject: DbOrganization, tokenData: TokenData = None
    ) -> None:
        from sqlalchemy import inspect

        dbSession = inspect(dbObject).session
        if dbObject is None:
            raise OrganizationDoesNotExistException(f"id = {obj.id()}")
        dbSession.add(self._updateDbObjectByObj(dbObject=dbObject, obj=obj))
        dbSession.commit()

    @debugLogger
    def organizationByName(self, name: str) -> Organization:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        dbObject = dbSession.query(DbOrganization).filter_by(name=name).first()
        if dbObject is None:
            raise OrganizationDoesNotExistException(f"name = {name}")
        return self._organizationFromDbObject(dbObject=dbObject)

    @debugLogger
    def organizationById(self, id: str) -> Organization:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        dbObject = dbSession.query(DbOrganization).filter_by(id=id).first()
        if dbObject is None:
            raise OrganizationDoesNotExistException(f"id = {id}")
        return self._organizationFromDbObject(dbObject=dbObject)

    @debugLogger
    def organizationsFilteredByOrganizationList(self, tokenData: TokenData, resultFrom: int = 0, resultSize: int = 10,
                                                order: List[dict] = None,
                                                organizationList: List[Organization] = None) -> dict:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        sortData = ""
        if order is not None:
            for item in order:
                sortData = f'{sortData}, {item["orderBy"]} {item["direction"]}'
            sortData = sortData[2:]
        items = dbSession.query(DbOrganization).filter(DbOrganization.id.in_([x.id() for x in organizationList])).order_by(
            text(sortData)).limit(resultSize).offset(resultFrom).all()
        itemsCount = dbSession.query(DbOrganization).filter(
            DbOrganization.id.in_([x.id() for x in organizationList])).count()
        if items is None:
            return {"items": [], "totalItemCount": 0}
        return {
            "items": [self._organizationFromDbObject(x) for x in items],
            "totalItemCount": itemsCount,
        }

    @debugLogger
    def _organizationFromDbObject(self, dbObject: DbOrganization):
        return Organization(
            id=dbObject.id,
            name=dbObject.name,
            websiteUrl=dbObject.websiteUrl,
            organizationType=dbObject.organizationType,
            addressOne=dbObject.addressOne,
            addressTwo=dbObject.addressTwo,
            postalCode=dbObject.postalCode,
            countryId=dbObject.countryId,
            cityId=dbObject.cityId,
            countryStateName=dbObject.countryStateName,
            countryStateIsoCode=dbObject.countryStateIsoCode,
            managerFirstName=dbObject.managerFirstName,
            managerLastName=dbObject.managerLastName,
            managerEmail=dbObject.managerEmail,
            managerPhoneNumber=dbObject.managerPhoneNumber,
            managerAvatar=dbObject.managerAvatar,
        )

    @debugLogger
    def organizations(
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
            dbSession.query(DbOrganization)
            .order_by(text(sortData))
            .limit(resultSize)
            .offset(resultFrom)
            .all()
        )
        itemsCount = dbSession.query(DbOrganization).count()
        if items is None:
            return {"items": [], "totalItemCount": 0}
        return {
            "items": [self._organizationFromDbObject(x) for x in items],
            "totalItemCount": itemsCount,
        }

    @debugLogger
    def organizationsByType(
        self,
        tokenData: TokenData,
        type: str = None,
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
            dbSession.query(DbOrganization)
            .filter_by(organizationType=type)
            .order_by(text(sortData))
            .limit(resultSize)
            .offset(resultFrom)
            .all()
        )
        itemsCount = dbSession.query(DbOrganization).filter_by(
            organizationType=type).count()
        if items is None:
            return {"items": [], "totalItemCount": 0}
        return {
            "items": [self._organizationFromDbObject(x) for x in items],
            "totalItemCount": itemsCount,
        }

    def _updateDbObjectByObj(self, dbObject: DbOrganization, obj: Organization):
        dbObject.name = dbObject.name if obj.name() is None else obj.name()
        dbObject.websiteUrl = (
            dbObject.websiteUrl if obj.websiteUrl() is None else obj.websiteUrl()
        )
        dbObject.organizationType = (
            dbObject.organizationType
            if obj.organizationType() is None
            else obj.organizationType()
        )
        dbObject.addressOne = (
            dbObject.addressOne if obj.addressOne() is None else obj.addressOne()
        )
        dbObject.addressTwo = (
            dbObject.addressTwo if obj.addressTwo() is None else obj.addressTwo()
        )
        dbObject.postalCode = (
            dbObject.postalCode if obj.postalCode() is None else obj.postalCode()
        )
        dbObject.countryId = (
            dbObject.countryId if obj.countryId() is None else obj.countryId()
        )
        dbObject.cityId = dbObject.cityId if obj.cityId() is None else obj.cityId()
        dbObject.countryStateName = (
            dbObject.countryStateName
            if obj.countryStateName() is None
            else obj.countryStateName()
        )
        dbObject.countryStateIsoCode = (
            dbObject.countryStateIsoCode
            if obj.countryStateIsoCode() is None
            else obj.countryStateIsoCode()
        )
        dbObject.managerFirstName = (
            dbObject.managerFirstName
            if obj.managerFirstName() is None
            else obj.managerFirstName()
        )
        dbObject.managerLastName = (
            dbObject.managerLastName
            if obj.managerLastName() is None
            else obj.managerLastName()
        )
        dbObject.managerEmail = (
            dbObject.managerEmail if obj.managerEmail() is None else obj.managerEmail()
        )
        dbObject.managerPhoneNumber = (
            dbObject.managerPhoneNumber
            if obj.managerPhoneNumber() is None
            else obj.managerPhoneNumber()
        )
        dbObject.managerAvatar = (
            dbObject.managerAvatar
            if obj.managerAvatar() is None
            else obj.managerAvatar()
        )
        return dbObject

    def _createDbObjectByObj(self, obj: Organization):
        return DbOrganization(
            id=obj.id(),
            name=obj.name(),
            websiteUrl=obj.websiteUrl(),
            organizationType=obj.organizationType(),
            addressOne=obj.addressOne(),
            addressTwo=obj.addressTwo(),
            postalCode=obj.postalCode(),
            countryId=obj.countryId(),
            cityId=obj.cityId(),
            countryStateName=obj.countryStateName(),
            countryStateIsoCode=obj.countryStateIsoCode(),
            managerFirstName=obj.managerFirstName(),
            managerLastName=obj.managerLastName(),
            managerEmail=obj.managerEmail(),
            managerPhoneNumber=obj.managerPhoneNumber(),
            managerAvatar=obj.managerAvatar(),
        )

    @debugLogger
    def linkOrganizationToBuilding(self,
                                 organization: Organization,
                                 building: Building,
                                 buildingLevel: BuildingLevel,
                                 buildingLevelRoom: BuildingLevelRoom,
                                 tokenData: TokenData = None):
        dbSession = ApplicationServiceLifeCycle.dbContext()

        sql = f"""FROM {ORGANIZATION__BUILDING__JUNCTION} organization__building__junc
                            WHERE
                                organization__building__junc.organization_id = "{organization.id()}" AND
                                organization__building__junc.project_id = "{building.projectId()}" AND
                                organization__building__junc.building_id = "{building.id()}" AND
                                organization__building__junc.building_level_id = "{buildingLevel.id()}" AND
                                organization__building__junc.building_level_room_id = "{buildingLevelRoom.id()}"
                        """
        dbObjectsCount = dbSession.execute(
            text(f"SELECT count(1) {sql}")
        ).scalar()

        if dbObjectsCount == 0:
            dbSession.execute(
                text(f"""
                    INSERT INTO {ORGANIZATION__BUILDING__JUNCTION} (`organization_id`, `project_id`, `building_id`, `building_level_id`, `building_level_room_id`)
                    VALUES ("{organization.id()}", "{building.projectId()}", "{building.id()}", "{buildingLevel.id()}", "{buildingLevelRoom.id()}")
                """)
            )

    @debugLogger
    def unlinkOrganizationToBuilding(self,
                                   organization: Organization,
                                   building: Building,
                                   buildingLevel: BuildingLevel,
                                   buildingLevelRoom: BuildingLevelRoom,
                                   tokenData: TokenData = None):
        dbSession = ApplicationServiceLifeCycle.dbContext()
        dbSession.execute(
            text(f"""
                DELETE FROM {ORGANIZATION__BUILDING__JUNCTION} organization__building__junc
                WHERE
                    organization__building__junc.organization_id = "{organization.id()}" AND
                    organization__building__junc.project_id = "{building.projectId()}" AND
                    organization__building__junc.building_id = "{building.id()}" AND
                    organization__building__junc.building_level_id = "{buildingLevel.id()}" AND
                    organization__building__junc.building_level_room_id = "{buildingLevelRoom.id()}"
            """)
        )
