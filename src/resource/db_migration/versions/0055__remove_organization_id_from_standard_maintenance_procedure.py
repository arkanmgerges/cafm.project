from sqlalchemy import *
from migrate import *

meta = MetaData()

tbl = Table("standard_maintenance_procedure", meta)

col0 = Column("organization_id", String(40), nullable=True)


def upgrade(migrate_engine):
    meta.bind = migrate_engine
    with migrate_engine.connect() as conn:
        conn.execute("ALTER TABLE standard_maintenance_procedure DROP COLUMN organization_id")

def downgrade(migrate_engine):
    meta.bind = migrate_engine
    Table("standard_maintenance_procedure", meta, autoload=True)
    col0.create(tbl)
