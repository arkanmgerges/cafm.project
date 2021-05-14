"""
The file is generated by scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from typing import List

from src.application.BaseApplicationService import BaseApplicationService
from src.application.model.BaseApplicationServiceBulkData import BaseApplicationServiceBulkData
from src.application.model.BaseApplicationServiceModelData import BaseApplicationServiceModelData
from src.domain_model.resource.exception.UpdateSubcontractorCategoryFailedException import (
    UpdateSubcontractorCategoryFailedException,
)
from src.domain_model.subcontractor.category.SubcontractorCategory import (
    SubcontractorCategory,
)
from src.domain_model.subcontractor.category.SubcontractorCategoryRepository import (
    SubcontractorCategoryRepository,
)
from src.domain_model.subcontractor.category.SubcontractorCategoryService import (
    SubcontractorCategoryService,
)
from src.domain_model.token.TokenService import TokenService
from src.resource.logging.decorator import debugLogger


class SubcontractorCategoryApplicationService(BaseApplicationService):
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
    def createSubcontractorCategory(self, token: str = None, objectOnly: bool = False, **kwargs):
        obj: SubcontractorCategory = self._constructObject(**kwargs)
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._subcontractorCategoryService.createSubcontractorCategory(
            obj=obj, objectOnly=objectOnly, tokenData=tokenData
        )

    @debugLogger
    def updateSubcontractorCategory(
        self,
        token: str = None,
        **kwargs,
    ):
        tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            oldObject: SubcontractorCategory = self._repo.subcontractorCategoryById(id=kwargs["id"])
            super().callFunction(
                modelData=BaseApplicationServiceModelData(
                    function=self._subcontractorCategoryService.updateSubcontractorCategory,
                    kwargs={
                        "oldObject": oldObject,
                        "newObject": self._constructObject(_sourceObject=oldObject, **kwargs),
                        "tokenData": tokenData,
                    },
                )
            )

        except Exception as e:
            raise UpdateSubcontractorCategoryFailedException(message=str(e))

    @debugLogger
    def deleteSubcontractorCategory(self, id: str, token: str = None):
        super().callFunction(
            modelData=BaseApplicationServiceModelData(
                function=self._subcontractorCategoryService.deleteSubcontractorCategory,
                kwargs={
                    "obj": self._repo.subcontractorCategoryById(id=id),
                    "tokenData": TokenService.tokenDataFromToken(token=token),
                },
            )
        )

    @debugLogger
    def bulkCreate(self, objListParams: List[dict], token: str = ""):
        super()._bulkCreate(
            baseBulkData=BaseApplicationServiceBulkData(
                objListParams=objListParams,
                token=token,
                sourceId="subcontractor_category_id",
                domainService=self._subcontractorCategoryService,
            )
        )

    @debugLogger
    def bulkDelete(self, objListParams: List[dict], token: str = ""):
        super()._bulkDelete(
            baseBulkData=BaseApplicationServiceBulkData(
                objListParams=objListParams,
                token=token,
                sourceId="subcontractor_category_id",
                domainService=self._subcontractorCategoryService,
            )
        )

    @debugLogger
    def bulkUpdate(self, objListParams: List[dict], token: str = ""):
        super()._bulkUpdate(
            baseBulkData=BaseApplicationServiceBulkData(
                objListParams=objListParams,
                token=token,
                sourceId="subcontractor_category_id",
                domainService=self._subcontractorCategoryService,
                repositoryCallbackFunction=self._repo.subcontractorCategoryById,
            )
        )

    @debugLogger
    def subcontractorCategoryById(self, id: str, token: str = None) -> SubcontractorCategory:
        TokenService.tokenDataFromToken(token=token)
        return super().callGetterFunction(
            modelData=BaseApplicationServiceModelData(
                getterFunction=self._repo.subcontractorCategoryById, kwargs={"id": id}
            )
        )

    @debugLogger
    def subcontractorCategories(
        self,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
        token: str = None,
    ) -> dict:
        tokenData = TokenService.tokenDataFromToken(token=token)
        return super().callGetterFunction(
            modelData=BaseApplicationServiceModelData(
                getterFunction=self._subcontractorCategoryService.subcontractorCategories,
                kwargs={"resultFrom": resultFrom, "resultSize": resultSize, "order": order, "tokenData": tokenData},
            )
        )

    @debugLogger
    def _constructObject(self, *args, **kwargs) -> SubcontractorCategory:
        kwargs[BaseApplicationService.APPLICATION_SERVICE_CLASS] = SubcontractorCategory
        return super()._constructObject(*args, **kwargs)
