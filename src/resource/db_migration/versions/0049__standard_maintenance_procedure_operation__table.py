from sqlalchemy import *
from migrate import *

meta = MetaData()

tbl = Table(
    "standard_maintenance_procedure_operation",
    meta,
    Column("id", String(40), primary_key=True),
    Column("name", String(255)),
    # There is a limit on the foreign key name, 64 chars
    Column(
        "standard_maintenance_procedure_id",
        String(40),
        ForeignKey(
            "standard_maintenance_procedure.id",
            name="fk__std_maintenance_proc_op__std_maintenance_proc__id",
            onupdate="CASCADE",
        ),
        nullable=True,
    ),
    Column("description", String(255)),
    Column("type", String(40)),
    Column("modified_at", DateTime),
    Column("created_at", DateTime),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    meta.bind = migrate_engine
    Table("standard_maintenance_procedure", meta, autoload=True)
    Index(
        "ix__std_maintenance_proc_op__std_maintenance_proc_id", tbl.c.standard_maintenance_procedure_id
    )
    tbl.create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    meta.bind = migrate_engine
    tbl.drop()
