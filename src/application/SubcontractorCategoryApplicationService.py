"""
The file is generated by scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from typing import List

from src.domain_model.resource.exception.DomainModelException import DomainModelException
from src.domain_model.resource.exception.ProcessBulkDomainException import ProcessBulkDomainException
from src.domain_model.subcontractor.category.SubcontractorCategory import (
    SubcontractorCategory,
)
from src.domain_model.subcontractor.category.SubcontractorCategoryRepository import (
    SubcontractorCategoryRepository,
)
from src.domain_model.subcontractor.category.SubcontractorCategoryService import (
    SubcontractorCategoryService,
)
from src.domain_model.resource.exception.UpdateSubcontractorCategoryFailedException import (
    UpdateSubcontractorCategoryFailedException,
)
from src.domain_model.token.TokenService import TokenService
from src.domain_model.util.DomainModelAttributeValidator import DomainModelAttributeValidator
from src.resource.logging.decorator import debugLogger


class SubcontractorCategoryApplicationService:
    def __init__(
        self,
        repo: SubcontractorCategoryRepository,
        subcontractorCategoryService: SubcontractorCategoryService,
    ):
        self._repo = repo
        self._subcontractorCategoryService = subcontractorCategoryService

    @debugLogger
    def newId(self):
        return SubcontractorCategory.createFrom(skipValidation=True).id()

    @debugLogger
    def createSubcontractorCategory(
        self,
        id: str = None,
        name: str = None,
        objectOnly: bool = False,
        token: str = "",
    ):
        obj: SubcontractorCategory = self.constructObject(id=id, name=name)
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._subcontractorCategoryService.createSubcontractorCategory(
            obj=obj, objectOnly=objectOnly, tokenData=tokenData
        )

    @debugLogger
    def updateSubcontractorCategory(self, id: str, name: str = None, token: str = None):
        tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            oldObject: SubcontractorCategory = self._repo.subcontractorCategoryById(
                id=id
            )
            obj: SubcontractorCategory = self.constructObject(
                id=id, name=name, _sourceObject=oldObject
            )
            self._subcontractorCategoryService.updateSubcontractorCategory(
                oldObject=oldObject, newObject=obj, tokenData=tokenData
            )
        except Exception as e:
            raise UpdateSubcontractorCategoryFailedException(message=str(e))

    @debugLogger
    def deleteSubcontractorCategory(self, id: str, token: str = None):
        tokenData = TokenService.tokenDataFromToken(token=token)
        obj = self._repo.subcontractorCategoryById(id=id)
        self._subcontractorCategoryService.deleteSubcontractorCategory(
            obj=obj, tokenData=tokenData
        )

    @debugLogger
    def bulkCreate(self, objListParams: List[dict], token: str = ""):
        objList = []
        exceptions = []
        for objListParamsItem in objListParams:
            try:
                DomainModelAttributeValidator.validate(domainModelObject=self.constructObject(skipValidation=True),
                                                       attributeDictionary=objListParamsItem)
                objList.append(self.constructObject(id=objListParamsItem["subcontractor_category_id"],
                                                    name=objListParamsItem["name"]))
            except DomainModelException as e:
                exceptions.append({"reason": {"message": e.message, "code": e.code}})
        tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            self._subcontractorCategoryService.bulkCreate(objList=objList)
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
                objList.append(
                    self.constructObject(id=objListParamsItem["subcontractor_category_id"], skipValidation=True))
            except DomainModelException as e:
                exceptions.append({"reason": {"message": e.message, "code": e.code}})
        tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            self._subcontractorCategoryService.bulkDelete(objList=objList)
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
                oldObject: SubcontractorCategory = self._repo.subcontractorCategoryById(
                    id=objListParamsItem["subcontractor_category_id"])
                newObject = self.constructObject(id=objListParamsItem["subcontractor_category_id"],
                                                 name=objListParamsItem[
                                                     "name"] if "name" in objListParamsItem else None,
                                                 _sourceObject=oldObject)
                objList.append((newObject, oldObject), )
            except DomainModelException as e:
                exceptions.append({"reason": {"message": e.message, "code": e.code}})
        tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            self._subcontractorCategoryService.bulkUpdate(objList=objList)
            if len(exceptions) > 0:
                raise ProcessBulkDomainException(messages=exceptions)
        except DomainModelException as e:
            exceptions.append({"reason": {"message": e.message, "code": e.code}})
            raise ProcessBulkDomainException(messages=exceptions)

    @debugLogger
    def subcontractorCategoryById(
        self, id: str, token: str = None
    ) -> SubcontractorCategory:
        subcontractorCategory = self._repo.subcontractorCategoryById(id=id)
        TokenService.tokenDataFromToken(token=token)
        return subcontractorCategory

    @debugLogger
    def subcontractorCategories(
        self,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
        token: str = None,
    ) -> dict:
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._subcontractorCategoryService.subcontractorCategories(
            tokenData=tokenData,
            resultFrom=resultFrom,
            resultSize=resultSize,
            order=order,
        )

    @debugLogger
    def constructObject(
        self, id: str = None, name: str = None, _sourceObject: SubcontractorCategory = None,
            skipValidation: bool = False,
    ) -> SubcontractorCategory:
        if _sourceObject is not None:
            return SubcontractorCategory.createFrom(
                id=id, name=name if name is not None else _sourceObject.name(), skipValidation=skipValidation,
            )
        else:
            return SubcontractorCategory.createFrom(id=id, name=name, skipValidation=skipValidation,)
