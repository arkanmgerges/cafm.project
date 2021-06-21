from src.domain_model.resource.exception.TagDoesNotExistException import TagDoesNotExistException
from typing import List

from sqlalchemy.sql.expression import text

from src.application.lifecycle.ApplicationServiceLifeCycle import ApplicationServiceLifeCycle
from src.domain_model.tag.Tag import Tag
from src.domain_model.tag.TagRepository import TagRepository
from src.domain_model.token.TokenData import TokenData
from src.port_adapter.repository.db_model.Tag import Tag as DbTag
from src.resource.logging.decorator import debugLogger


class TagRepositoryImpl(TagRepository):
    @debugLogger
    def tagByName(self, name: str) -> Tag:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        dbObject = dbSession.query(DbTag).filter_by(name=name).first()
        if dbObject is None:
            raise TagDoesNotExistException(f"name = {name}")
        return self._roleFromDbObject(dbObject=dbObject)

    @debugLogger
    def _roleFromDbObject(self, dbObject: DbTag):
        return Tag(
            id=dbObject.id,
            name=dbObject.name,
        )
