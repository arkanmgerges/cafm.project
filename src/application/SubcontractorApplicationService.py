"""
The file is generated by scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from typing import List

from src.application.BaseApplicationService import BaseApplicationService
from src.application.lifecycle.decorator.readOnly import readOnly
from src.application.lifecycle.decorator.transactional import transactional
from src.application.model.BaseApplicationServiceBulkData import (
    BaseApplicationServiceBulkData,
)
from src.application.model.BaseApplicationServiceModelData import (
    BaseApplicationServiceModelData,
)
from src.domain_model.organization.OrganizationRepository import OrganizationRepository
from src.domain_model.resource.exception.SubcontractorCategoryDoesNotExistException import (
    SubcontractorCategoryDoesNotExistException,
)
from src.domain_model.resource.exception.UpdateSubcontractorFailedException import (
    UpdateSubcontractorFailedException,
)
from src.domain_model.subcontractor.Subcontractor import Subcontractor
from src.domain_model.subcontractor.SubcontractorRepository import (
    SubcontractorRepository,
)
from src.domain_model.subcontractor.SubcontractorService import SubcontractorService
from src.domain_model.subcontractor.category.SubcontractorCategoryRepository import (
    SubcontractorCategoryRepository,
)
from src.domain_model.token.TokenService import TokenService
from src.resource.logging.decorator import debugLogger


class SubcontractorApplicationService(BaseApplicationService):
    def __init__(
        self,
        repo: SubcontractorRepository,
        orgRepo: OrganizationRepository,
        subcontractorService: SubcontractorService,
        subcontractorCategoryRepo: SubcontractorCategoryRepository,
    ):
        self._repo = repo
        self._orgRepo = orgRepo
        self._subcontractorService = subcontractorService
        self._subcontractorCategoryRepo = subcontractorCategoryRepo

    @debugLogger
    def newId(self):
        return Subcontractor.createFrom(skipValidation=True).id()

    @transactional
    @debugLogger
    def createSubcontractor(
        self, token: str = None, objectOnly: bool = False, **kwargs
    ):
        obj: Subcontractor = self._constructObject(**kwargs)
        tokenData = TokenService.tokenDataFromToken(token=token)

        if kwargs["subcontractorCategoryId"] is None:
            raise SubcontractorCategoryDoesNotExistException(
                f"subcontractor category id = {kwargs['subcontractorCategoryId']}"
            )

        if (
            kwargs["subcontractorCategoryId"] is not None
            and kwargs["subcontractorCategoryId"] != ""
        ):
            subcontractorCategory = (
                self._subcontractorCategoryRepo.subcontractorCategoryById(
                    id=kwargs["subcontractorCategoryId"]
                )
            )
            if subcontractorCategory is None:
                raise SubcontractorCategoryDoesNotExistException(
                    f"subcontractor category id = {kwargs['subcontractorCategoryId']}"
                )

        return self._subcontractorService.createSubcontractor(
            obj=obj, objectOnly=objectOnly, tokenData=tokenData
        )

    @transactional
    @debugLogger
    def assignSubcontractor(
        self, id: str, organizationId: str, token: str = "", **_kwargs
    ):
        tokenData = TokenService.tokenDataFromToken(token=token)
        subcontractor = self._repo.subcontractorById(id=id)
        organization = self._orgRepo.organizationById(id=organizationId)
        self._subcontractorService.assignSubcontractor(
            subcontractor=subcontractor, organization=organization, tokenData=tokenData
        )

    @transactional
    @debugLogger
    def revokeSubcontractor(
        self, id: str, organizationId: str, token: str = "", **_kwargs
    ):
        tokenData = TokenService.tokenDataFromToken(token=token)
        subcontractor = self._repo.subcontractorById(id=id)
        organization = self._orgRepo.organizationById(id=organizationId)
        self._subcontractorService.revokeSubcontractor(
            subcontractor=subcontractor, organization=organization, tokenData=tokenData
        )

    @readOnly
    @debugLogger
    def subcontractorsByOrganizationId(
        self,
        organizationId: str,
        resultFrom: int = 0,
        resultSize: int = 100,
        token: str = "",
        order: List[dict] = None,
        **_kwargs,
    ) -> dict:
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._subcontractorService.subcontractorsByOrganizationId(
            organizationId=organizationId,
            tokenData=tokenData,
            resultFrom=resultFrom,
            resultSize=resultSize,
            order=order,
        )

    @readOnly
    @debugLogger
    def subcontractorsBySubcontractorCategoryId(
        self,
        subcontractorCategoryId: str = None,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
        token: str = None,
        **_kwargs,
    ) -> dict:
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._subcontractorService.subcontractorsBySubcontractorCategoryId(
            tokenData=tokenData,
            subcontractorCategoryId=subcontractorCategoryId,
            resultFrom=resultFrom,
            resultSize=resultSize,
            order=order,
        )

    @transactional
    @debugLogger
    def updateSubcontractor(
        self,
        token: str = None,
        **kwargs,
    ):
        tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            oldObject: Subcontractor = self._repo.subcontractorById(id=kwargs["id"])
            super().callFunction(
                modelData=BaseApplicationServiceModelData(
                    function=self._subcontractorService.updateSubcontractor,
                    kwargs={
                        "oldObject": oldObject,
                        "newObject": self._constructObject(
                            _sourceObject=oldObject, **kwargs
                        ),
                        "tokenData": tokenData,
                    },
                )
            )

        except Exception as e:
            raise UpdateSubcontractorFailedException(message=str(e))

    @transactional
    @debugLogger
    def deleteSubcontractor(self, id: str, token: str = None, **_kwargs):
        super().callFunction(
            modelData=BaseApplicationServiceModelData(
                function=self._subcontractorService.deleteSubcontractor,
                kwargs={
                    "obj": self._repo.subcontractorById(id=id),
                    "tokenData": TokenService.tokenDataFromToken(token=token),
                },
            )
        )

    @transactional
    @debugLogger
    def bulkCreate(self, objListParams: List[dict], token: str = ""):
        super()._bulkCreate(
            baseBulkData=BaseApplicationServiceBulkData(
                objListParams=objListParams,
                token=token,
                sourceId="subcontractor_id",
                domainService=self._subcontractorService,
            )
        )

    @transactional
    @debugLogger
    def bulkDelete(self, objListParams: List[dict], token: str = ""):
        super()._bulkDelete(
            baseBulkData=BaseApplicationServiceBulkData(
                objListParams=objListParams,
                token=token,
                sourceId="subcontractor_id",
                domainService=self._subcontractorService,
            )
        )

    @transactional
    @debugLogger
    def bulkUpdate(self, objListParams: List[dict], token: str = ""):
        super()._bulkUpdate(
            baseBulkData=BaseApplicationServiceBulkData(
                objListParams=objListParams,
                token=token,
                sourceId="subcontractor_id",
                domainService=self._subcontractorService,
                repositoryCallbackFunction=self._repo.subcontractorById,
            )
        )

    @readOnly
    @debugLogger
    def subcontractorById(self, id: str, token: str = None, **_kwargs) -> Subcontractor:
        TokenService.tokenDataFromToken(token=token)
        return super().callGetterFunction(
            modelData=BaseApplicationServiceModelData(
                getterFunction=self._repo.subcontractorById, kwargs={"id": id}
            )
        )

    @readOnly
    @debugLogger
    def subcontractors(
        self,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
        token: str = None,
        **_kwargs,
    ) -> dict:
        tokenData = TokenService.tokenDataFromToken(token=token)
        return super().callGetterFunction(
            modelData=BaseApplicationServiceModelData(
                getterFunction=self._subcontractorService.subcontractors,
                kwargs={
                    "resultFrom": resultFrom,
                    "resultSize": resultSize,
                    "order": order,
                    "tokenData": tokenData,
                },
            )
        )

    @debugLogger
    def _constructObject(self, *args, **kwargs) -> Subcontractor:
        kwargs[BaseApplicationService.DOMAIN_MODEL_CLASS] = Subcontractor
        return super()._constructObject(*args, **kwargs)
