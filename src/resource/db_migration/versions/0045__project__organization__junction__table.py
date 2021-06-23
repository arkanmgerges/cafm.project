from sqlalchemy import *
from migrate import *

meta = MetaData()

tbl = Table(
    "project__organization__junction",
    meta,
    Column("id", Integer, primary_key=True),
    Column(
        "project_id",
        String(40),
        ForeignKey(
            "project.id",
            name="fk__project__organization__junction__project__id",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
    ),
    Column(
        "organization_id",
        String(40),
        ForeignKey(
            "organization.id",
            name="fk__project__organization__junction__organization__id",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
    ),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    meta.bind = migrate_engine
    _t = Table("project", meta, autoload=True)
    _t = Table("organization", meta, autoload=True)
    Index("ix__project__organization__junction__project_id", tbl.c.project_id)
    Index("ix__project__organization__junction__organization_id", tbl.c.organization_id)
    tbl.create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    meta.bind = migrate_engine
    tbl.drop()
