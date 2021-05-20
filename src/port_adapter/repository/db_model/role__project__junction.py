"""
@author: Mohammad M. mmdii<mmdii@develoop.run>
"""

from sqlalchemy import Column, Integer, ForeignKey, Table

import src.port_adapter.AppDi as AppDi

Base = AppDi.instance.get(AppDi.DbBase)
ROLE__PROJECT__JUNCTION = "role__project__junction"
associationTable = Table(
    "role__project__junction",
    Base.metadata,
    Column(
        "role_id",
        Integer,
        ForeignKey("role.id", ondelete="CASCADE", onupdate="CASCADE"),
    ),
    Column(
        "project_id",
        Integer,
        ForeignKey("project.id", ondelete="CASCADE", onupdate="CASCADE"),
    ),
)
