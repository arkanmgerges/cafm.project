"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from src.application.lookup.subcontractor.SubcontractorLookupRepository import SubcontractorLookupRepository
from src.application.user_lookup.UserLookup import UserLookup
from src.domain_model.resource.exception.DomainModelException import DomainModelException
from src.domain_model.resource.exception.ProcessBulkDomainException import ProcessBulkDomainException
from src.domain_model.subcontractor.Subcontractor import Subcontractor
from src.domain_model.token.TokenService import TokenService
from src.domain_model.util.DomainModelAttributeValidator import DomainModelAttributeValidator
from src.resource.logging.decorator import debugLogger


class SubcontractorLookupApplicationService:
    def __init__(self, repo: SubcontractorLookupRepository):
        self._repo = repo

    @debugLogger
    def createSubcontractor(self,
        id: str = None,
        companyName: str = None,
        websiteUrl: str = None,
        contactPerson: str = None,
        email: str = None,
        phoneNumber: str = None,
        addressOne: str = None,
        addressTwo: str = None,
        subcontractorCategoryId: str = None,
        token: str = "",):
        _tokenData = TokenService.tokenDataFromToken(token=token)
        obj: Subcontractor = self._constructObject(
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
        self._repo.save(obj=obj)

    @debugLogger
    def bulkCreateSubcontractor(self, objListParams: List[dict], token: str = ""):
        objList = []
        exceptions = []
        for objListParamsItem in objListParams:
            try:
                DomainModelAttributeValidator.validate(domainModelObject=self._constructObject(skipValidation=True),
                                                       attributeDictionary=objListParamsItem)
                objList.append(self._constructObject(id=objListParamsItem["subcontractor_id"],
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
            #todo add bulk create to repo
            # self._subcontractorService.bulkCreate(objList=objList)
            if len(exceptions) > 0:
                raise ProcessBulkDomainException(messages=exceptions)
        except DomainModelException as e:
            exceptions.append({"reason": {"message": e.message, "code": e.code}})
            raise ProcessBulkDomainException(messages=exceptions)

    @debugLogger
    def _constructObject(
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
        skipValidation: bool = False,
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
                skipValidation=skipValidation,
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
                skipValidation=skipValidation,
            )