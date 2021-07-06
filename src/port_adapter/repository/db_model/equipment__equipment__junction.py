"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from sqlalchemy import Column, Integer, ForeignKey, Table

import src.port_adapter.AppDi as AppDi

Base = AppDi.instance.get(AppDi.DbBase)
EQUIPMENT__EQUIPMENT__JUNCTION = "equipment__equipment__junction"
associationTable = Table(
    EQUIPMENT__EQUIPMENT__JUNCTION,
    Base.metadata,
    Column(
        "src_equipment_id",
        Integer,
        ForeignKey("equipment.id", ondelete="CASCADE", onupdate="CASCADE"),
    ),
    Column(
        "dst_equipment_id",
        Integer,
        ForeignKey("equipment.id", ondelete="CASCADE", onupdate="CASCADE"),
    ),
)
