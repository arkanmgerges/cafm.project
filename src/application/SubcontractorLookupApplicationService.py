"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from src.application.BaseApplicationService import BaseApplicationService
from src.application.lookup.subcontractor.SubcontractorLookupRepository import SubcontractorLookupRepository
from src.domain_model.resource.exception.DomainModelException import DomainModelException
from src.domain_model.resource.exception.ProcessBulkDomainException import ProcessBulkDomainException
from src.domain_model.subcontractor.Subcontractor import Subcontractor
from src.domain_model.token.TokenService import TokenService
from src.domain_model.util.DomainModelAttributeValidator import DomainModelAttributeValidator
from src.resource.common.Util import Util
from src.resource.logging.decorator import debugLogger


class SubcontractorLookupApplicationService(BaseApplicationService):
    def __init__(self, repo: SubcontractorLookupRepository):
        self._repo = repo

    @debugLogger
    def createSubcontractor(self, *args, **kwargs):
        _tokenData = TokenService.tokenDataFromToken(token=kwargs["token"])
        obj: Subcontractor = self._constructObject(*args, **kwargs)
        self._repo.save(obj=obj)

    @debugLogger
    def bulkCreateSubcontractor(self, objListParams: List[dict], token: str = ""):
        objList = []
        exceptions = []
        for objListParamsItem in objListParams:
            try:
                DomainModelAttributeValidator.validate(
                    domainModelObject=self._constructObject(skipValidation=True), attributeDictionary=objListParamsItem
                )
                objList.append(
                    self._constructObject(
                        **Util.snakeCaseToLowerCameCaseDict(
                            objListParamsItem, keyReplacements=[{"source": "subcontractor_id", "target": "id"}]
                        )
                    )
                )
            except DomainModelException as e:
                exceptions.append({"reason": {"message": e.message, "code": e.code}})
        _tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            # todo add bulk create to repo
            # self._subcontractorService.bulkCreate(objList=objList)
            if len(exceptions) > 0:
                raise ProcessBulkDomainException(messages=exceptions)
        except DomainModelException as e:
            exceptions.append({"reason": {"message": e.message, "code": e.code}})
            raise ProcessBulkDomainException(messages=exceptions)

    @debugLogger
    def _constructObject(self, *args, **kwargs) -> Subcontractor:
        kwargs[BaseApplicationService.APPLICATION_SERVICE_CLASS] = Subcontractor
        return super()._constructObject(*args, **kwargs)
