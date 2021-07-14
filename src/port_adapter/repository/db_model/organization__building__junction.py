"""
@author: Mohammad S. moso<moso@develoop.run>
"""

from sqlalchemy import Column, Integer, ForeignKey, Table

import src.port_adapter.AppDi as AppDi

Base = AppDi.instance.get(AppDi.DbBase)
ORGANIZATION__BUILDING__JUNCTION = "organization__building__junction"
associationTable = Table(
    "organization__building__junction",
    Base.metadata,
    Column(
        "organization_id",
        Integer,
        ForeignKey("organization.id", ondelete="CASCADE", onupdate="CASCADE"),
    ),
    Column(
        "project_id",
        Integer,
        ForeignKey("project.id", ondelete="CASCADE", onupdate="CASCADE"),
    ),
    Column(
        "building_id",
        Integer,
        ForeignKey("building.id", ondelete="CASCADE", onupdate="CASCADE"),
    ),
    Column(
        "building_level_id",
        Integer,
        ForeignKey("building_level.id", ondelete="CASCADE", onupdate="CASCADE"),
    ),
    Column(
        "building_level_room_id",
        Integer,
        ForeignKey("building_level_room.id", ondelete="CASCADE", onupdate="CASCADE"),
    )
)
