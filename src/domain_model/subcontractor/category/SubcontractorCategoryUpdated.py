"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from uuid import uuid4
from src.domain_model.event.DomainEvent import DomainEvent
from src.domain_model.event.EventConstant import CommonEventConstant
from src.domain_model.subcontractor.category.SubcontractorCategory import (
    SubcontractorCategory,
)


class SubcontractorCategoryUpdated(DomainEvent):
    def __init__(self, oldObj: SubcontractorCategory, newObj: SubcontractorCategory):
        super().__init__(
            id=str(uuid4()),
            name=CommonEventConstant.SUBCONTRACTOR_CATEGORY_UPDATED.value,
        )
        self._data = {"old": oldObj.toMap(), "new": newObj.toMap()}
