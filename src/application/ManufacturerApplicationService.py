"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from src.domain_model.manufacturer.Manufacturer import Manufacturer
from src.domain_model.manufacturer.ManufacturerRepository import ManufacturerRepository
from src.domain_model.manufacturer.ManufacturerService import ManufacturerService
from src.domain_model.resource.exception.UpdateManufacturerFailedException import UpdateManufacturerFailedException
from src.domain_model.token.TokenService import TokenService
from src.resource.logging.decorator import debugLogger


class ManufacturerApplicationService:
    def __init__(self, repo: ManufacturerRepository, manufacturerService: ManufacturerService):
        self._repo = repo
        self._manufacturerService = manufacturerService

    @debugLogger
    def createManufacturer(self, id: str = None, name: str = '', objectOnly: bool = False, token: str = ''):
        obj: Manufacturer = self.constructObject(id=id, name=name)
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._manufacturerService.createManufacturer(obj=obj,
                                                            objectOnly=objectOnly, tokenData=tokenData)

    @debugLogger
    def updateManufacturer(self, id: str, name: str, token: str = ''):
        obj: Manufacturer = self.constructObject(id=id, name=name)
        tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            oldObject: Manufacturer = self._repo.manufacturerById(id=id)
            self._manufacturerService.updateManufacturer(oldObject=oldObject,
                                                         newObject=obj, tokenData=tokenData)
        except Exception as e:
            raise UpdateManufacturerFailedException(message=str(e))

    @debugLogger
    def deleteManufacturer(self, id: str, token: str = ''):
        tokenData = TokenService.tokenDataFromToken(token=token)
        obj = self._repo.manufacturerById(id=id)
        self._manufacturerService.deleteManufacturer(obj=obj, tokenData=tokenData)

    @debugLogger
    def manufacturerByName(self, name: str, token: str = '') -> Manufacturer:
        manufacturer = self._repo.manufacturerByName(name=name)
        tokenData = TokenService.tokenDataFromToken(token=token)
        return manufacturer

    @debugLogger
    def manufacturerById(self, id: str, token: str = '') -> Manufacturer:
        manufacturer = self._repo.manufacturerById(id=id)
        tokenData = TokenService.tokenDataFromToken(token=token)
        return manufacturer

    @debugLogger
    def manufacturers(self, resultFrom: int = 0, resultSize: int = 100, token: str = '',
                      order: List[dict] = None) -> dict:
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._manufacturerService.manufacturers(tokenData=tokenData,
                                                       resultFrom=resultFrom,
                                                       resultSize=resultSize,
                                                       order=order)

    @debugLogger
    def constructObject(self, id: str, name: str) -> Manufacturer:
        return Manufacturer.createFrom(id=id, name=name)