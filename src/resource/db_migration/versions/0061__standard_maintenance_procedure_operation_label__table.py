from sqlalchemy import *
from migrate import *

meta = MetaData()

tbl = Table(
    "standard_maintenance_procedure_operation_label",
    meta,
    Column("id", String(40), primary_key=True),
    Column("index", Integer, primary_key=True, autoincrement=True),
    Column("label", String(255)),
    Column("generate_alert", Integer),
    # There is a limit on the foreign key name, 64 chars
    Column(
        "standard_maintenance_procedure_operation_id",
        String(40),
        ForeignKey(
            "standard_maintenance_procedure_operation.id",
            name="fk__std_main_proc_op_label__std_main_proc_op__id",
            onupdate="CASCADE",
        ),
        nullable=True,
    ),
    Column("modified_at", DateTime),
    Column("created_at", DateTime),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    meta.bind = migrate_engine
    Table("standard_maintenance_procedure_operation", meta, autoload=True)

    Index(
        "ix__std_main_proc_op_label__std_main_proc_op_id",
        tbl.c.standard_maintenance_procedure_operation_id,
    )
    tbl.create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    meta.bind = migrate_engine
    tbl.drop()
