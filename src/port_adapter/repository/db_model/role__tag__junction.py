"""
@author: Mohammad M. mmdii<mmdii@develoop.run>
"""

from sqlalchemy import Column, Integer, ForeignKey, Table

import src.port_adapter.AppDi as AppDi

Base = AppDi.instance.get(AppDi.DbBase)
ROLE__TAG__JUNCTION = "role__tag__junction"
associationTable = Table(
    "role__tag__junction",
    Base.metadata,
    Column(
        "role_id",
        Integer,
        ForeignKey("role.id", ondelete="CASCADE", onupdate="CASCADE"),
    ),
    Column(
        "tag_id",
        Integer,
        ForeignKey("tag.id", ondelete="CASCADE", onupdate="CASCADE"),
    ),
)
