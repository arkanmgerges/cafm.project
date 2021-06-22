"""
The file is generated by scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from typing import List

from src.domain_model.tag.Tag import Tag
from src.domain_model.tag.TagRepository import TagRepository
from src.domain_model.tag.TagService import TagService
from src.domain_model.resource.exception.UpdateTagFailedException import UpdateTagFailedException
from src.domain_model.token.TokenService import TokenService
from src.application.BaseApplicationService import BaseApplicationService
from src.application.lifecycle.decorator.readOnly import readOnly
from src.application.lifecycle.decorator.transactional import transactional
from src.application.model.BaseApplicationServiceBulkData import BaseApplicationServiceBulkData
from src.application.model.BaseApplicationServiceModelData import BaseApplicationServiceModelData
from src.resource.logging.decorator import debugLogger

class TagApplicationService(BaseApplicationService):
    def __init__(self, repo: TagRepository, tagService: TagService,):
        self._repo = repo
        self._tagService = tagService

    @debugLogger
    def newId(self, **_kwargs):
        return Tag.createFrom(skipValidation=True).id()

    @transactional
    @debugLogger
    def createTag(self, token: str = None, objectOnly: bool = False, **kwargs):
        obj: Tag = self._constructObject(**kwargs)
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._tagService.createTag(obj=obj, objectOnly=objectOnly, tokenData=tokenData)

    @transactional
    @debugLogger
    def updateTag(
        self,
        token: str = None,
        **kwargs,
    ):
        tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            oldObject: Tag = self._repo.tagById(id=kwargs["id"])
            super().callFunction(
                modelData=BaseApplicationServiceModelData(
                    function=self._tagService.updateTag,
                    kwargs={
                        "oldObject": oldObject,
                        "newObject": self._constructObject(_sourceObject=oldObject, **kwargs),
                        "tokenData": tokenData,
                    },
                )
            )

        except Exception as e:
            raise UpdateTagFailedException(message=str(e))

    @transactional
    @debugLogger
    def deleteTag(self, id: str, token: str = None, **_kwargs):
        super().callFunction(
            modelData=BaseApplicationServiceModelData(
                function=self._tagService.deleteTag,
                kwargs={
                    "obj": self._repo.tagById(id=id),
                    "tokenData": TokenService.tokenDataFromToken(token=token),
                },
            )
        )

    @transactional
    @debugLogger
    def bulkCreate(self, objListParams: List[dict], token: str = "", **_kwargs):
        super()._bulkCreate(
            baseBulkData=BaseApplicationServiceBulkData(
                objListParams=objListParams,
                token=token,
                sourceId="tag_id",
                domainService=self._tagService,
            )
        )

    @transactional
    @debugLogger
    def bulkDelete(self, objListParams: List[dict], token: str = "", **_kwargs):
        super()._bulkDelete(
            baseBulkData=BaseApplicationServiceBulkData(
                objListParams=objListParams,
                token=token,
                sourceId="tag_id",
                domainService=self._tagService,
            )
        )

    @transactional
    @debugLogger
    def bulkUpdate(self, objListParams: List[dict], token: str = "", **_kwargs):
        super()._bulkUpdate(
            baseBulkData=BaseApplicationServiceBulkData(
                objListParams=objListParams,
                token=token,
                sourceId="tag_id",
                domainService=self._tagService,
                repositoryCallbackFunction=self._repo.tagById,
            )
        )

    @readOnly
    @debugLogger
    def tagById(self, id: str, token: str = None, **_kwargs) -> Tag:
        TokenService.tokenDataFromToken(token=token)
        return super().callGetterFunction(
            modelData=BaseApplicationServiceModelData(getterFunction=self._repo.tagById, kwargs={"id": id})
        )

    @readOnly
    @debugLogger
    def tags(
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
                getterFunction=self._tagService.tags,
                kwargs={"resultFrom": resultFrom, "resultSize": resultSize, "order": order, "tokenData": tokenData},
            )
        )

    @debugLogger
    def _constructObject(self, *args, **kwargs) -> Tag:
        kwargs[BaseApplicationService.DOMAIN_MODEL_CLASS] = Tag
        return super()._constructObject(*args, **kwargs)
