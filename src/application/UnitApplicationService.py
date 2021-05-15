"""
The file is generated by scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from typing import List

from src.application.BaseApplicationService import BaseApplicationService
from src.application.model.BaseApplicationServiceBulkData import BaseApplicationServiceBulkData
from src.application.model.BaseApplicationServiceModelData import BaseApplicationServiceModelData
from src.domain_model.project.unit.Unit import Unit
from src.domain_model.project.unit.UnitRepository import UnitRepository
from src.domain_model.project.unit.UnitService import UnitService
from src.domain_model.resource.exception.UpdateUnitFailedException import (
    UpdateUnitFailedException,
)
from src.domain_model.token.TokenService import TokenService
from src.resource.logging.decorator import debugLogger


class UnitApplicationService(BaseApplicationService):
    def __init__(self, repo: UnitRepository, unitService: UnitService):
        self._repo = repo
        self._unitService = unitService

    @debugLogger
    def newId(self):
        return Unit.createFrom(skipValidation=True).id()

    @debugLogger
    def createUnit(self, token: str = None, objectOnly: bool = False, **kwargs):
        obj: Unit = self._constructObject(**kwargs)
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._unitService.createUnit(obj=obj, objectOnly=objectOnly, tokenData=tokenData)

    @debugLogger
    def updateUnit(
        self,
        token: str = None,
        **kwargs,
    ):
        tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            oldObject: Unit = self._repo.unitById(id=kwargs["id"])
            super().callFunction(
                modelData=BaseApplicationServiceModelData(
                    function=self._unitService.updateUnit,
                    kwargs={
                        "oldObject": oldObject,
                        "newObject": self._constructObject(_sourceObject=oldObject, **kwargs),
                        "tokenData": tokenData,
                    },
                )
            )

        except Exception as e:
            raise UpdateUnitFailedException(message=str(e))

    @debugLogger
    def deleteUnit(self, id: str, token: str = None):
        super().callFunction(
            modelData=BaseApplicationServiceModelData(
                function=self._unitService.deleteUnit,
                kwargs={"obj": self._repo.unitById(id=id), "tokenData": TokenService.tokenDataFromToken(token=token)},
            )
        )

    @debugLogger
    def bulkCreate(self, objListParams: List[dict], token: str = ""):
        super()._bulkCreate(
            baseBulkData=BaseApplicationServiceBulkData(
                objListParams=objListParams,
                token=token,
                sourceId="unit_id",
                domainService=self._unitService,
            )
        )

    @debugLogger
    def bulkDelete(self, objListParams: List[dict], token: str = ""):
        super()._bulkDelete(
            baseBulkData=BaseApplicationServiceBulkData(
                objListParams=objListParams,
                token=token,
                sourceId="unit_id",
                domainService=self._unitService,
            )
        )

    @debugLogger
    def bulkUpdate(self, objListParams: List[dict], token: str = ""):
        super()._bulkUpdate(
            baseBulkData=BaseApplicationServiceBulkData(
                objListParams=objListParams,
                token=token,
                sourceId="unit_id",
                domainService=self._unitService,
                repositoryCallbackFunction=self._repo.unitById,
            )
        )

    @debugLogger
    def unitById(self, id: str, token: str = None) -> Unit:
        TokenService.tokenDataFromToken(token=token)
        return super().callGetterFunction(
            modelData=BaseApplicationServiceModelData(getterFunction=self._repo.unitById, kwargs={"id": id})
        )

    @debugLogger
    def units(
        self,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
        token: str = None,
    ) -> dict:
        tokenData = TokenService.tokenDataFromToken(token=token)
        return super().callGetterFunction(
            modelData=BaseApplicationServiceModelData(
                getterFunction=self._unitService.units,
                kwargs={"resultFrom": resultFrom, "resultSize": resultSize, "order": order, "tokenData": tokenData},
            )
        )

    @debugLogger
    def _constructObject(self, *args, **kwargs) -> Unit:
        kwargs[BaseApplicationService.DOMAIN_MODEL_CLASS] = Unit
        return super()._constructObject(*args, **kwargs)
