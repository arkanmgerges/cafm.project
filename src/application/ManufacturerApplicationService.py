"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from src.application.BaseApplicationService import BaseApplicationService
from src.application.model.BaseApplicationServiceBulkData import BaseApplicationServiceBulkData
from src.application.model.BaseApplicationServiceModelData import BaseApplicationServiceModelData
from src.domain_model.manufacturer.Manufacturer import Manufacturer
from src.domain_model.manufacturer.ManufacturerRepository import ManufacturerRepository
from src.domain_model.manufacturer.ManufacturerService import ManufacturerService
from src.domain_model.resource.exception.UpdateManufacturerFailedException import (
    UpdateManufacturerFailedException,
)
from src.domain_model.token.TokenService import TokenService
from src.resource.logging.decorator import debugLogger


class ManufacturerApplicationService(BaseApplicationService):
    def __init__(self, repo: ManufacturerRepository, manufacturerService: ManufacturerService):
        self._repo = repo
        self._manufacturerService = manufacturerService

    @debugLogger
    def newId(self):
        return Manufacturer.createFrom(skipValidation=True).id()

    @debugLogger
    def createManufacturer(self, token: str = None, objectOnly: bool = False, **kwargs):
        obj: Manufacturer = self._constructObject(**kwargs)
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._manufacturerService.createManufacturer(obj=obj, objectOnly=objectOnly, tokenData=tokenData)

    @debugLogger
    def manufacturerByName(self, name: str = None, token: str = "") -> Manufacturer:
        _tokenData = TokenService.tokenDataFromToken(token=token)
        return super().callGetterFunction(
            modelData=BaseApplicationServiceModelData(
                getterFunction=self._repo.manufacturerByName, kwargs={"name": name}
            )
        )

    @debugLogger
    def updateManufacturer(
        self,
        token: str = None,
        **kwargs,
    ):
        tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            oldObject: Manufacturer = self._repo.manufacturerById(id=kwargs["id"])
            super().callFunction(
                modelData=BaseApplicationServiceModelData(
                    function=self._manufacturerService.updateManufacturer,
                    kwargs={
                        "oldObject": oldObject,
                        "newObject": self._constructObject(_sourceObject=oldObject, **kwargs),
                        "tokenData": tokenData,
                    },
                )
            )

        except Exception as e:
            raise UpdateManufacturerFailedException(message=str(e))

    @debugLogger
    def deleteManufacturer(self, id: str, token: str = None, **_kwargs):
        super().callFunction(
            modelData=BaseApplicationServiceModelData(
                function=self._manufacturerService.deleteManufacturer,
                kwargs={
                    "obj": self._repo.manufacturerById(id=id),
                    "tokenData": TokenService.tokenDataFromToken(token=token),
                },
            )
        )

    @debugLogger
    def bulkCreate(self, objListParams: List[dict], token: str = "", **_kwargs):
        super()._bulkCreate(
            baseBulkData=BaseApplicationServiceBulkData(
                objListParams=objListParams,
                token=token,
                sourceId="manufacturer_id",
                domainService=self._manufacturerService,
            )
        )

    @debugLogger
    def bulkDelete(self, objListParams: List[dict], token: str = "", **_kwargs):
        super()._bulkDelete(
            baseBulkData=BaseApplicationServiceBulkData(
                objListParams=objListParams,
                token=token,
                sourceId="manufacturer_id",
                domainService=self._manufacturerService,
            )
        )

    @debugLogger
    def bulkUpdate(self, objListParams: List[dict], token: str = "", **_kwargs):
        super()._bulkUpdate(
            baseBulkData=BaseApplicationServiceBulkData(
                objListParams=objListParams,
                token=token,
                sourceId="manufacturer_id",
                domainService=self._manufacturerService,
                repositoryCallbackFunction=self._repo.manufacturerById,
            )
        )

    @debugLogger
    def manufacturerById(self, id: str, token: str = None, **_kwargs) -> Manufacturer:
        TokenService.tokenDataFromToken(token=token)
        return super().callGetterFunction(
            modelData=BaseApplicationServiceModelData(getterFunction=self._repo.manufacturerById, kwargs={"id": id})
        )

    @debugLogger
    def manufacturers(
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
                getterFunction=self._manufacturerService.manufacturers,
                kwargs={"resultFrom": resultFrom, "resultSize": resultSize, "order": order, "tokenData": tokenData},
            )
        )

    @debugLogger
    def _constructObject(self, *args, **kwargs) -> Manufacturer:
        kwargs[BaseApplicationService.DOMAIN_MODEL_CLASS] = Manufacturer
        return super()._constructObject(*args, **kwargs)
