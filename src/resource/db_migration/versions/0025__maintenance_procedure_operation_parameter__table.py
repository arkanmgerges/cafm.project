from sqlalchemy import *
from migrate import *

meta = MetaData()

tbl = Table(
    "maintenance_procedure_operation_parameter",
    meta,
    Column("id", String(40), primary_key=True),
    Column("name", String(255)),
    # There is a limit on the foreign key name, 64 chars
    Column(
        "maintenance_procedure_operation_id",
        String(40),
        ForeignKey(
            "maintenance_procedure_operation.id",
            name="fk__maintenance_proc_op_param__maintenance_proc_op__id",
            onupdate="CASCADE",
        ),
        nullable=True,
    ),
    Column(
        "unit_id",
        String(40),
        ForeignKey(
            "unit.id",
            name="fk__maintenance_proc_op_param__unit__id",
            onupdate="CASCADE",
        ),
        nullable=True,
    ),
    Column("min_value", Float),
    Column("max_value", Float),
    Column("modified_at", DateTime),
    Column("created_at", DateTime),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    meta.bind = migrate_engine
    Table("unit", meta, autoload=True)
    Table("maintenance_procedure_operation", meta, autoload=True)

    Index(
        "ix__maintenance_proc_op_param__maintenance_proc_op_id",
        tbl.c.maintenance_procedure_operation_id,
    )
    Index("ix__maintenance_proc_op_param__unit_id", tbl.c.unit_id)
    tbl.create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    meta.bind = migrate_engine
    tbl.drop()
