"""
@author: Mohammad S. moso<moso@develoop.run>
"""

from sqlalchemy import Column, Integer, ForeignKey, Table

import src.port_adapter.AppDi as AppDi

Base = AppDi.instance.get(AppDi.DbBase)
EQUIPMENT_PROJECT_CATEGORY__EQUIPMENT_CATEGORY_GROUP__JUNCTION = (
    "equipment_project_category__equipment_category_group__junction"
)
associationTable = Table(
    EQUIPMENT_PROJECT_CATEGORY__EQUIPMENT_CATEGORY_GROUP__JUNCTION,
    Base.metadata,
    Column(
        "equipment_project_category_id",
        Integer,
        ForeignKey(
            "equipment_project_category.id", ondelete="CASCADE", onupdate="CASCADE"
        ),
    ),
    Column(
        "equipment_category_group_id",
        Integer,
        ForeignKey(
            "equipment_category_group.id", ondelete="CASCADE", onupdate="CASCADE"
        ),
    ),
)
