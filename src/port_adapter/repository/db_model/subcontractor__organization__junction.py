"""
@author: Mohammad S. moso<moso@develoop.run>
"""

from sqlalchemy import Column, Integer, ForeignKey, Table

import src.port_adapter.AppDi as AppDi

Base = AppDi.instance.get(AppDi.DbBase)
SUBCONTRACTOR__ORGANIZATION__JUNCTION = "subcontractor__organization__junction"
associationTable = Table(
    "subcontractor__organization__junction",
    Base.metadata,
    Column(
        "subcontractor_id",
        Integer,
        ForeignKey("subcontractor.id", ondelete="CASCADE", onupdate="CASCADE"),
    ),
    Column(
        "organization_id",
        Integer,
        ForeignKey("organization.id", ondelete="CASCADE", onupdate="CASCADE"),
    ),
)
