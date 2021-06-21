from sqlalchemy import Column, String, ForeignKey, Table

import src.port_adapter.AppDi as AppDi

Base = AppDi.instance.get(AppDi.DbBase)
PROJECT__ORGANIZATION__JUNCTION = "project__organization__junction"
associationTable = Table(
    PROJECT__ORGANIZATION__JUNCTION,
    Base.metadata,
    Column(
        "project_id",
        String(40),
        ForeignKey("project.id", ondelete="CASCADE", onupdate="CASCADE"),
    ),
    Column(
        "organization_id",
        String(40),
        ForeignKey("organization.id", ondelete="CASCADE", onupdate="CASCADE"),
    ),
)
