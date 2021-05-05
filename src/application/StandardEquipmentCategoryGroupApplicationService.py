"""
The file is generated by scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from typing import List

from src.domain_model.project.standard_equipment.standard_category.standard_group.StandardEquipmentCategoryGroup import (
    StandardEquipmentCategoryGroup,
)
from src.domain_model.project.standard_equipment.standard_category.standard_group.StandardEquipmentCategoryGroupRepository import (
    StandardEquipmentCategoryGroupRepository,
)
from src.domain_model.project.standard_equipment.standard_category.standard_group.StandardEquipmentCategoryGroupService import (
    StandardEquipmentCategoryGroupService,
)
from src.domain_model.resource.exception.DomainModelException import DomainModelException
from src.domain_model.resource.exception.ProcessBulkDomainException import ProcessBulkDomainException
from src.domain_model.resource.exception.UpdateStandardEquipmentCategoryGroupFailedException import (
    UpdateStandardEquipmentCategoryGroupFailedException,
)
from src.domain_model.token.TokenService import TokenService
from src.domain_model.util.DomainModelAttributeValidator import DomainModelAttributeValidator
from src.resource.logging.decorator import debugLogger
from src.domain_model.project.standard_equipment.standard_category.StandardEquipmentCategoryRepository import (
    StandardEquipmentCategoryRepository,
)


class StandardEquipmentCategoryGroupApplicationService:
    def __init__(
        self,
        repo: StandardEquipmentCategoryGroupRepository,
        standardEquipmentCategoryGroupService: StandardEquipmentCategoryGroupService,
        standardEquipmentCategoryRepo: StandardEquipmentCategoryRepository,
    ):
        self._repo = repo
        self._standardEquipmentCategoryGroupService = (
            standardEquipmentCategoryGroupService
        )
        self._standardEquipmentCategoryRepo = standardEquipmentCategoryRepo

    @debugLogger
    def newId(self):
        return StandardEquipmentCategoryGroup.createFrom(skipValidation=True).id()

    @debugLogger
    def createStandardEquipmentCategoryGroup(
        self,
        id: str = None,
        name: str = None,
        standardEquipmentCategoryId: str = None,
        objectOnly: bool = False,
        token: str = "",
    ):
        obj: StandardEquipmentCategoryGroup = self.constructObject(
            id=id,
            name=name,
            standardEquipmentCategoryId=standardEquipmentCategoryId
        )
        tokenData = TokenService.tokenDataFromToken(token=token)
        self._standardEquipmentCategoryRepo.standardEquipmentCategoryById(
            id=standardEquipmentCategoryId
        )
        return self._standardEquipmentCategoryGroupService.createStandardEquipmentCategoryGroup(
            obj=obj, objectOnly=objectOnly, tokenData=tokenData
        )

    @debugLogger
    def updateStandardEquipmentCategoryGroup(
        self,
        id: str,
        name: str = None,
        standardEquipmentCategoryId: str = None,
        token: str = None,
    ):
        tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            oldObject: StandardEquipmentCategoryGroup = (
                self._repo.standardEquipmentCategoryGroupById(id=id)
            )
            obj: StandardEquipmentCategoryGroup = self.constructObject(
                id=id,
                name=name,
                standardEquipmentCategoryId=standardEquipmentCategoryId,
                _sourceObject=oldObject,
            )
            self._standardEquipmentCategoryGroupService.updateStandardEquipmentCategoryGroup(
                oldObject=oldObject, newObject=obj, tokenData=tokenData
            )
        except Exception as e:
            raise UpdateStandardEquipmentCategoryGroupFailedException(message=str(e))

    @debugLogger
    def deleteStandardEquipmentCategoryGroup(self, id: str, token: str = None):
        tokenData = TokenService.tokenDataFromToken(token=token)
        obj = self._repo.standardEquipmentCategoryGroupById(id=id)
        self._standardEquipmentCategoryGroupService.deleteStandardEquipmentCategoryGroup(
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
                objList.append(self.constructObject(id=objListParamsItem["standard_equipment_category_group_id"],
                                                    name=objListParamsItem["name"],
                                                    standardEquipmentCategoryId=objListParamsItem[
                                                        "standard_equipment_category_id"]))
            except DomainModelException as e:
                exceptions.append({"reason": {"message": e.message, "code": e.code}})
        tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            self._standardEquipmentCategoryGroupService.bulkCreate(objList=objList)
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
                objList.append(self.constructObject(id=objListParamsItem["standard_equipment_category_group_id"],
                                                    skipValidation=True))
            except DomainModelException as e:
                exceptions.append({"reason": {"message": e.message, "code": e.code}})
        tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            self._standardEquipmentCategoryGroupService.bulkDelete(objList=objList)
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
                oldObject: StandardEquipmentCategoryGroup = self._repo.standardEquipmentCategoryGroupById(
                    id=objListParamsItem["standard_equipment_category_group_id"])
                newObject = self.constructObject(id=objListParamsItem["standard_equipment_category_group_id"],
                                                 name=objListParamsItem[
                                                     "name"] if "name" in objListParamsItem else None,
                                                 standardEquipmentCategoryId=objListParamsItem[
                                                     "standard_equipment_category_id"] if "standard_equipment_category_id" in objListParamsItem else None,
                                                 _sourceObject=oldObject)
                objList.append((newObject, oldObject), )
            except DomainModelException as e:
                exceptions.append({"reason": {"message": e.message, "code": e.code}})
        tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            self._standardEquipmentCategoryGroupService.bulkUpdate(objList=objList)
            if len(exceptions) > 0:
                raise ProcessBulkDomainException(messages=exceptions)
        except DomainModelException as e:
            exceptions.append({"reason": {"message": e.message, "code": e.code}})
            raise ProcessBulkDomainException(messages=exceptions)

    @debugLogger
    def standardEquipmentCategoryGroupById(
        self, id: str, token: str = None
    ) -> StandardEquipmentCategoryGroup:
        standardEquipmentCategoryGroup = self._repo.standardEquipmentCategoryGroupById(
            id=id
        )
        TokenService.tokenDataFromToken(token=token)
        return standardEquipmentCategoryGroup

    @debugLogger
    def standardEquipmentCategoryGroups(
        self,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
        token: str = None,
    ) -> dict:
        tokenData = TokenService.tokenDataFromToken(token=token)
        return (
            self._standardEquipmentCategoryGroupService.standardEquipmentCategoryGroups(
                tokenData=tokenData,
                resultFrom=resultFrom,
                resultSize=resultSize,
                order=order,
            )
        )

    @debugLogger
    def constructObject(
        self,
        id: str = None,
        name: str = None,
        standardEquipmentCategoryId: str = None,
        _sourceObject: StandardEquipmentCategoryGroup = None,
        skipValidation: bool = False,
    ) -> StandardEquipmentCategoryGroup:
        if _sourceObject is not None:
            return StandardEquipmentCategoryGroup.createFrom(
                id=id,
                name=name if name is not None else _sourceObject.name(),
                standardEquipmentCategoryId=standardEquipmentCategoryId
                if standardEquipmentCategoryId is not None
                else _sourceObject.standardEquipmentCategoryId(),
                skipValidation=skipValidation,
            )
        else:
            return StandardEquipmentCategoryGroup.createFrom(
                id=id,
                name=name,
                standardEquipmentCategoryId=standardEquipmentCategoryId,
                skipValidation=skipValidation,
            )
