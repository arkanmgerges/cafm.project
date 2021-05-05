"""
@author: Mohammad S. moso<moso@develoop.run>
"""
from typing import List

from src.domain_model.organization.OrganizationRepository import OrganizationRepository
from src.domain_model.resource.exception.DomainModelException import DomainModelException
from src.domain_model.resource.exception.ProcessBulkDomainException import ProcessBulkDomainException
from src.domain_model.resource.exception.SubcontractorCategoryDoesNotExistException import \
    SubcontractorCategoryDoesNotExistException
from src.domain_model.resource.exception.UpdateSubcontractorFailedException import (
    UpdateSubcontractorFailedException,
)
from src.domain_model.subcontractor.Subcontractor import Subcontractor
from src.domain_model.subcontractor.category.SubcontractorCategory import (
    SubcontractorCategory,
)
from src.domain_model.subcontractor.category.SubcontractorCategoryRepository import (
    SubcontractorCategoryRepository,
)
from src.domain_model.subcontractor.SubcontractorRepository import (
    SubcontractorRepository,
)
from src.domain_model.subcontractor.SubcontractorService import SubcontractorService
from src.domain_model.token.TokenService import TokenService
from src.domain_model.util.DomainModelAttributeValidator import DomainModelAttributeValidator
from src.resource.logging.decorator import debugLogger


class SubcontractorApplicationService:
    def __init__(
        self,
        repo: SubcontractorRepository,
        orgRepo: OrganizationRepository,
        subcontractorCategoryRepo: SubcontractorCategoryRepository,
        domainService: SubcontractorService,
    ):
        self._repo = repo
        self._orgRepo = orgRepo
        self._subcontractorCategoryRepo = subcontractorCategoryRepo
        self._subcontractorService = domainService

    @debugLogger
    def newId(self):
        return Subcontractor.createFrom().id()

    @debugLogger
    def createSubcontractor(
        self,
        id: str = None,
        companyName: str = None,
        websiteUrl: str = None,
        contactPerson: str = None,
        email: str = None,
        phoneNumber: str = None,
        addressOne: str = None,
        addressTwo: str = None,
        subcontractorCategoryId: str = None,
        objectOnly: bool = False,
        token: str = "",
    ) -> Subcontractor:
        obj: Subcontractor = self.constructObject(
            id=id,
            companyName=companyName,
            websiteUrl=websiteUrl,
            contactPerson=contactPerson,
            email=email,
            phoneNumber=phoneNumber,
            subcontractorCategoryId=subcontractorCategoryId,
            addressOne=addressOne,
            addressTwo=addressTwo,
        )
        tokenData = TokenService.tokenDataFromToken(token=token)

        if subcontractorCategoryId is not None:
            subcontractorCategory = (
                self._subcontractorCategoryRepo.subcontractorCategoryById(
                    id=subcontractorCategoryId
                )
            )
            if subcontractorCategory is None:
                raise SubcontractorCategoryDoesNotExistException(
                    f"id = {subcontractorCategoryId}"
                )

        return self._subcontractorService.createSubcontractor(
            obj=obj, objectOnly=objectOnly, tokenData=tokenData
        )

    @debugLogger
    def updateSubcontractor(
        self,
        id: str = None,
        companyName: str = None,
        websiteUrl: str = None,
        contactPerson: str = None,
        email: str = None,
        phoneNumber: str = None,
        addressOne: str = None,
        addressTwo: str = None,
        subcontractorCategoryId: str = None,
        token: str = "",
    ):
        tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            oldObject: Subcontractor = self._repo.subcontractorById(id=id)
            obj: Subcontractor = self.constructObject(
                id=id,
                companyName=companyName,
                websiteUrl=websiteUrl,
                contactPerson=contactPerson,
                email=email,
                phoneNumber=phoneNumber,
                addressOne=addressOne,
                addressTwo=addressTwo,
                subcontractorCategoryId=subcontractorCategoryId,
                _sourceObject=oldObject,
            )
            self._subcontractorService.updateSubcontractor(
                oldObject=oldObject, newObject=obj, tokenData=tokenData
            )
        except Exception as e:
            raise UpdateSubcontractorFailedException(message=str(e))

    @debugLogger
    def deleteSubcontractor(self, id: str, token: str = ""):
        tokenData = TokenService.tokenDataFromToken(token=token)
        obj = self._repo.subcontractorById(id=id)
        self._subcontractorService.deleteSubcontractor(obj=obj, tokenData=tokenData)

    @debugLogger
    def assignSubcontractor(self, id: str, organizationId: str, token: str = ""):
        tokenData = TokenService.tokenDataFromToken(token=token)
        subcontractor = self._repo.subcontractorById(id=id)
        organization = self._orgRepo.organizationById(id=organizationId)
        self._subcontractorService.assignSubcontractor(
            subcontractor=subcontractor, organization=organization, tokenData=tokenData
        )

    @debugLogger
    def revokeSubcontractor(self, id: str, organizationId: str, token: str = ""):
        tokenData = TokenService.tokenDataFromToken(token=token)
        subcontractor = self._repo.subcontractorById(id=id)
        organization = self._orgRepo.organizationById(id=organizationId)
        self._subcontractorService.revokeSubcontractor(
            subcontractor=subcontractor, organization=organization, tokenData=tokenData
        )

    @debugLogger
    def bulkCreate(self, objListParams: List[dict], token: str = ""):
        objList = []
        exceptions = []
        for objListParamsItem in objListParams:
            try:
                DomainModelAttributeValidator.validate(domainModelObject=self.constructObject(skipValidation=True),
                                                       attributeDictionary=objListParamsItem)
                objList.append(self.constructObject(id=objListParamsItem["subcontractor_id"],
                                                    companyName=objListParamsItem["company_name"],
                                                    websiteUrl=objListParamsItem["website_url"],
                                                    contactPerson=objListParamsItem["contact_person"],
                                                    email=objListParamsItem["email"],
                                                    phoneNumber=objListParamsItem["phone_number"],
                                                    subcontractorCategoryId=objListParamsItem[
                                                        "subcontractor_category_id"],
                                                    addressOne=objListParamsItem["address_one"],
                                                    addressTwo=objListParamsItem["address_two"]))
            except DomainModelException as e:
                exceptions.append({"reason": {"message": e.message, "code": e.code}})
        tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            self._subcontractorService.bulkCreate(objList=objList)
            if len(exceptions) > 0:
                raise ProcessBulkDomainException(messages=exceptions)
        except DomainModelException as e:
            exceptions.append({"reason": {"message": e.message, "code": e.code}})
            raise ProcessBulkDomainException(messages=exceptions)

    @debugLogger
    def bulkDelete(self, objListParams: List[dict], token: str = ""):
        objList = []
        exceptions = []
        for objListParamsItem in objListParams:
            try:
                DomainModelAttributeValidator.validate(domainModelObject=self.constructObject(skipValidation=True),
                                                       attributeDictionary=objListParamsItem)
                objList.append(self.constructObject(id=objListParamsItem["subcontractor_id"], skipValidation=True))
            except DomainModelException as e:
                exceptions.append({"reason": {"message": e.message, "code": e.code}})
        tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            self._subcontractorService.bulkDelete(objList=objList)
            if len(exceptions) > 0:
                raise ProcessBulkDomainException(messages=exceptions)
        except DomainModelException as e:
            exceptions.append({"reason": {"message": e.message, "code": e.code}})
            raise ProcessBulkDomainException(messages=exceptions)

    @debugLogger
    def bulkUpdate(self, objListParams: List[dict], token: str = ""):
        objList = []
        exceptions = []
        for objListParamsItem in objListParams:
            try:
                DomainModelAttributeValidator.validate(domainModelObject=self.constructObject(skipValidation=True),
                                                       attributeDictionary=objListParamsItem)
                oldObject: Subcontractor = self._repo.subcontractorById(id=objListParamsItem["subcontractor_id"])
                newObject = self.constructObject(id=objListParamsItem["subcontractor_id"],
                                                 companyName=objListParamsItem[
                                                     "company_name"] if "company_name" in objListParamsItem else None,
                                                 websiteUrl=objListParamsItem[
                                                     "website_url"] if "website_url" in objListParamsItem else None,
                                                 contactPerson=objListParamsItem[
                                                     "contact_person"] if "contact_person" in objListParamsItem else None,
                                                 email=objListParamsItem[
                                                     "email"] if "email" in objListParamsItem else None,
                                                 phoneNumber=objListParamsItem[
                                                     "phone_number"] if "phone_number" in objListParamsItem else None,
                                                 addressOne=objListParamsItem[
                                                     "address_one"] if "address_one" in objListParamsItem else None,
                                                 addressTwo=objListParamsItem[
                                                     "address_two"] if "address_two" in objListParamsItem else None,
                                                 subcontractorCategoryId=objListParamsItem[
                                                     "subcontractor_category_id"] if "subcontractor_category_id" in objListParamsItem else None,
                                                 _sourceObject=oldObject)
                objList.append((newObject, oldObject), )
            except DomainModelException as e:
                exceptions.append({"reason": {"message": e.message, "code": e.code}})
        tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            self._subcontractorService.bulkUpdate(objList=objList)
            if len(exceptions) > 0:
                raise ProcessBulkDomainException(messages=exceptions)
        except DomainModelException as e:
            exceptions.append({"reason": {"message": e.message, "code": e.code}})
            raise ProcessBulkDomainException(messages=exceptions)

    @debugLogger
    def subcontractorById(self, id: str, token: str = "") -> Subcontractor:
        obj = self._repo.subcontractorById(id=id)
        tokenData = TokenService.tokenDataFromToken(token=token)
        return obj

    @debugLogger
    def subcontractors(
        self,
        resultFrom: int = 0,
        resultSize: int = 100,
        token: str = "",
        order: List[dict] = None,
    ) -> dict:
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._subcontractorService.subcontractors(
            tokenData=tokenData,
            resultFrom=resultFrom,
            resultSize=resultSize,
            order=order,
        )

    @debugLogger
    def subcontractorsByOrganizationId(
        self,
        organizationId: str,
        resultFrom: int = 0,
        resultSize: int = 100,
        token: str = "",
        order: List[dict] = None,
    ) -> dict:
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._subcontractorService.subcontractorsByOrganizationId(
            organizationId=organizationId,
            tokenData=tokenData,
            resultFrom=resultFrom,
            resultSize=resultSize,
            order=order,
        )

    @debugLogger
    def subcontractorsBySubcontractorCategoryId(
        self,
        subcontractorCategoryId: str,
        resultFrom: int = 0,
        resultSize: int = 100,
        token: str = "",
        order: List[dict] = None,
    ) -> dict:
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._subcontractorService.subcontractorsBySubcontractorCategoryId(
            subcontractorCategoryId=subcontractorCategoryId,
            tokenData=tokenData,
            resultFrom=resultFrom,
            resultSize=resultSize,
            order=order,
        )

    @debugLogger
    def constructObject(
        self,
        id: str = None,
        companyName: str = None,
        websiteUrl: str = None,
        contactPerson: str = None,
        email: str = None,
        phoneNumber: str = None,
        addressOne: str = None,
        addressTwo: str = None,
        subcontractorCategoryId: str = None,
        _sourceObject: Subcontractor = None,
    ) -> Subcontractor:
        if _sourceObject is not None:
            return Subcontractor.createFrom(
                id=id,
                companyName=companyName
                if companyName is not None
                else _sourceObject.companyName(),
                websiteUrl=websiteUrl
                if websiteUrl is not None
                else _sourceObject.websiteUrl(),
                contactPerson=contactPerson
                if contactPerson is not None
                else _sourceObject.contactPerson(),
                email=email if email is not None else _sourceObject.email(),
                phoneNumber=phoneNumber
                if phoneNumber is not None
                else _sourceObject.phoneNumber(),
                subcontractorCategoryId=subcontractorCategoryId
                if subcontractorCategoryId is not None
                else _sourceObject.subcontractorCategoryId(),
                addressOne=addressOne
                if addressOne is not None
                else _sourceObject.addressOne(),
                addressTwo=addressTwo
                if addressTwo is not None
                else _sourceObject.addressTwo(),
            )
        else:
            return Subcontractor.createFrom(
                id=id,
                companyName=companyName,
                websiteUrl=websiteUrl,
                contactPerson=contactPerson,
                email=email,
                phoneNumber=phoneNumber,
                subcontractorCategoryId=subcontractorCategoryId,
                addressOne=addressOne,
                addressTwo=addressTwo,
            )
