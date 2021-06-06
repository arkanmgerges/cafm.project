"""
The file is generated by scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from typing import List


from src.application.BaseApplicationService import BaseApplicationService
from src.application.lookup.daily_check_procedure.EquipmentCategoryGroupRepository import (
    EquipmentCategoryGroupRepository,
)
from src.domain_model.resource.exception.DomainModelException import (
    DomainModelException,
)
from src.domain_model.resource.exception.ProcessBulkDomainException import (
    ProcessBulkDomainException,
)
from src.domain_model.project.equipment.category.group.EquipmentCategoryGroup import EquipmentCategoryGroup
from src.domain_model.token.TokenService import TokenService
from src.domain_model.util.DomainModelAttributeValidator import (
    DomainModelAttributeValidator,
)
from src.resource.common.Util import Util
from src.resource.logging.decorator import debugLogger

class EquipmentCategoryGroupApplicationService(BaseApplicationService):
    def __init__(self, repo: EquipmentCategoryGroupRepository):
        self._repo = repo

    @debugLogger
    def createEquipmentCategoryGroup(self, *args, **kwargs):
        _tokenData = TokenService.tokenDataFromToken(token=kwargs["token"])
        obj: EquipmentCategoryGroup = self._constructObject(*args, **kwargs)
        self._repo.save(obj=obj)

    @debugLogger
    def updateEquipmentCategoryGroup(self, *args, **kwargs):
        _tokenData = TokenService.tokenDataFromToken(token=kwargs["token"])
        kwargs["skipValidation"] = True
        obj: EquipmentCategoryGroup = self._constructObject(*args, **kwargs)
        self._repo.save(obj=obj)

    @debugLogger
    def deleteEquipmentCategoryGroup(self, *args, **kwargs):
        _tokenData = TokenService.tokenDataFromToken(token=kwargs["token"])
        kwargs["skipValidation"] = True
        obj: EquipmentCategoryGroup = self._constructObject(*args, **kwargs)
        self._repo.delete(obj=obj)

    @debugLogger
    def bulkCreateEquipmentCategoryGroup(self, objListParams: List[dict], token: str = ""):
        objList = []
        exceptions = []
        for objListParamsItem in objListParams:
            try:
                DomainModelAttributeValidator.validate(
                    domainModelObject=self._constructObject(skipValidation=True),
                    attributeDictionary=objListParamsItem,
                )
                objList.append(
                    self._constructObject(
                        **Util.snakeCaseToLowerCameCaseDict(
                            objListParamsItem,
                            keyReplacements=[
                                {"source": "_id", "target": "id"}
                            ],
                        )
                    )
                )
            except DomainModelException as e:
                exceptions.append({"reason": {"message": e.message, "code": e.code}})
        _tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            # todo add bulk create to repo
            # self._Service.bulkCreate(objList=objList)
            if len(exceptions) > 0:
                raise ProcessBulkDomainException(messages=exceptions)
        except DomainModelException as e:
            exceptions.append({"reason": {"message": e.message, "code": e.code}})
            raise ProcessBulkDomainException(messages=exceptions)

    @debugLogger
    def _constructObject(self, *args, **kwargs) -> EquipmentCategoryGroup:
        kwargs[BaseApplicationService.DOMAIN_MODEL_CLASS] = EquipmentCategoryGroup
        return super()._constructObject(*args, **kwargs)
