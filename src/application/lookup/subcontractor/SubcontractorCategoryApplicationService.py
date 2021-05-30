"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from src.application.BaseApplicationService import BaseApplicationService
from src.application.lookup.subcontractor.SubcontractorCategoryRepository import \
    SubcontractorCategoryRepository as EsSubcontractorCategoryRepository
from src.domain_model.resource.exception.DomainModelException import DomainModelException
from src.domain_model.resource.exception.ProcessBulkDomainException import ProcessBulkDomainException
from src.domain_model.subcontractor.category.SubcontractorCategory import SubcontractorCategory
from src.domain_model.token.TokenService import TokenService
from src.domain_model.util.DomainModelAttributeValidator import DomainModelAttributeValidator
from src.resource.common.Util import Util
from src.resource.logging.decorator import debugLogger


class SubcontractorCategoryApplicationService(BaseApplicationService):
    def __init__(self, repo: EsSubcontractorCategoryRepository):
        self._repo = repo

    @debugLogger
    def updateSubcontractorCategory(self, *args, **kwargs):
        _tokenData = TokenService.tokenDataFromToken(token=kwargs["token"])
        obj: SubcontractorCategory = self._constructObject(*args, skipValidation=True, **kwargs)
        self._repo.save(obj=obj)

    @debugLogger
    def bulkCreateSubcontractorCategory(self, objListParams: List[dict], token: str = ""):
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
                            objListParamsItem, keyReplacements=[{"source": "subcontractor_category_id", "target": "id"}]
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
    def _constructObject(self, *args, **kwargs) -> SubcontractorCategory:
        kwargs[BaseApplicationService.DOMAIN_MODEL_CLASS] = SubcontractorCategory
        return super()._constructObject(*args, **kwargs)
