"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from sqlalchemy import Column, Integer, ForeignKey, Table

import src.port_adapter.AppDi as AppDi

Base = AppDi.instance.get(AppDi.DbBase)
USER__ROLE__JUNCTION = "user__role__junction"
associationTable = Table(
    USER__ROLE__JUNCTION,
    Base.metadata,
    Column(
        "user_id",
        Integer,
        ForeignKey("user.id", ondelete="CASCADE", onupdate="CASCADE"),
    ),
    Column(
        "role_id",
        Integer,
        ForeignKey("role.id", ondelete="CASCADE", onupdate="CASCADE"),
    ),
)
