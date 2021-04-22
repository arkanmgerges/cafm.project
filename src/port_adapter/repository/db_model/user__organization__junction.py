"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from sqlalchemy import Column, Integer, ForeignKey, Table

import src.port_adapter.AppDi as AppDi

Base = AppDi.instance.get(AppDi.DbBase)
USER__ORGANIZATION__JUNCTION = "user__organization__junction"
associationTable = Table(
    "user__organization__junction",
    Base.metadata,
    Column(
        "user_id",
        Integer,
        ForeignKey("user.id", ondelete="CASCADE", onupdate="CASCADE"),
    ),
    Column(
        "organization_id",
        Integer,
        ForeignKey("organization.id", ondelete="CASCADE", onupdate="CASCADE"),
    ),
)
