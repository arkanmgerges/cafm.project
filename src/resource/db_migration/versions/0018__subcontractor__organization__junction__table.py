from sqlalchemy import *
from migrate import *

meta = MetaData()

tbl = Table(
    "subcontractor__organization__junction",
    meta,
    Column("id", Integer, primary_key=True),
    # There is a limit on the foreign key name, 64 chars
    Column(
        "subcontractor_id",
        String(40),
        ForeignKey(
            "subcontractor.id",
            name="fk__subcontractor__organization__junction__subcontractor__id",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
    ),
    Column(
        "organization_id",
        String(40),
        ForeignKey(
            "organization.id",
            name="fk__subcontractor__organization__junction__organization__id",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
    ),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    meta.bind = migrate_engine
    _t = Table("subcontractor", meta, autoload=True)
    _t = Table("organization", meta, autoload=True)
    Index(
        "ix__subcontractor__organization__junction__subcontractor_id",
        tbl.c.subcontractor_id,
    )
    Index(
        "ix__subcontractor__organization__junction__organization_id",
        tbl.c.organization_id,
    )
    tbl.create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    meta.bind = migrate_engine
    tbl.drop()
