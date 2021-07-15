from sqlalchemy import *
from migrate import *

meta = MetaData()

tbl = Table(
    "daily_check_procedure_operation_label",
    meta,
    Column("id", String(40), primary_key=True),
    Column("label", String(255)),
    Column("generate_alert", Integer),
    # There is a limit on the foreign key name, 64 chars
    Column(
        "daily_check_procedure_operation_id",
        String(40),
        ForeignKey(
            "daily_check_procedure_operation.id",
            name="fk__daily_check_proc_op_param__daily_check_proc_op__id",
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
    Table("daily_check_procedure_operation", meta, autoload=True)

    Index(
        "ix__daily_check_proc_op_param__daily_check_proc_op_id",
        tbl.c.daily_check_procedure_operation_id,
    )
    tbl.create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    meta.bind = migrate_engine
    tbl.drop()
