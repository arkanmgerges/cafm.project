from sqlalchemy import *

meta = MetaData()

tbl = Table(
    "user__organization__junction",
    meta,
    Column("id", Integer, primary_key=True),
    Column(
        "user_id",
        String(40),
        ForeignKey(
            "user.id",
            name="fk__user__organization__junction__user__id",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
    ),
    Column(
        "organization_id",
        String(40),
        ForeignKey(
            "organization.id",
            name="fk__user__organization__junction__organization__id",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
    ),
)

tbl2 = Table(
    "role__organization__junction",
    meta,
    Column("id", Integer, primary_key=True),
    Column(
        "role_id",
        String(40),
        ForeignKey(
            "role.id",
            name="fk__role__organization__junction__role__id",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
    ),
    Column(
        "organization_id",
        String(40),
        ForeignKey(
            "organization.id",
            name="fk__role__organization__junction__organization__id",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
    ),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    meta.bind = migrate_engine
    tbl.drop()
    _t = Table("role", meta, autoload=True)
    _t = Table("organization", meta, autoload=True)
    Index("ix__role__organization__junction__role_id", tbl2.columns.role_id)
    Index(
        "ix__role__organization__junction__organization_id",
        tbl2.columns.organization_id,
    )
    tbl2.create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    meta.bind = migrate_engine
    tbl2.drop()
    _t = Table("user", meta, autoload=True)
    _t = Table("organization", meta, autoload=True)
    Index("ix__user__organization__junction__user_id", tbl.columns.user_id)
    Index(
        "ix__user__organization__junction__organization_id", tbl.columns.organization_id
    )
    tbl.create()
