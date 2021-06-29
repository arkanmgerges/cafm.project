from sqlalchemy import *
from migrate import *

meta = MetaData()

tbl = Table("standard_equipment_category", meta)

col0 = Column("organization_id", String(40), nullable=True)


def upgrade(migrate_engine):
    meta.bind = migrate_engine
    Table("standard_equipment_category", meta, autoload=True)
    col0.create(tbl)

def downgrade(migrate_engine):
    meta.bind = migrate_engine
    with migrate_engine.connect() as conn:
        conn.execute("ALTER TABLE standard_equipment_category DROP COLUMN organization_id")
