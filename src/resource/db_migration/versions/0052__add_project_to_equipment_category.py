from sqlalchemy import *
from migrate import *

meta = MetaData()

tbl = Table("equipment_category", meta)

col0 = Column("project_id", String(40), nullable=True)


def upgrade(migrate_engine):
    meta.bind = migrate_engine
    Table("equipment_category", meta, autoload=True)
    col0.create(tbl)

def downgrade(migrate_engine):
    meta.bind = migrate_engine
    with migrate_engine.connect() as conn:
        conn.execute("ALTER TABLE equipment_category DROP COLUMN project_id")
