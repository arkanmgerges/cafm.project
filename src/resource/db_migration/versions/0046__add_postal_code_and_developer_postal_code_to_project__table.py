from sqlalchemy import *

meta = MetaData()


def upgrade(migrate_engine):
    meta.bind = migrate_engine
    tbl = Table("project", meta, autoload=True)
    col = Column("postal_code", String(20), default="")
    col.create(tbl)
    col = Column("developer_postal_code", String(20), default="")
    col.create(tbl)


def downgrade(migrate_engine):
    meta.bind = migrate_engine
    with migrate_engine.connect() as conn:
        conn.execute("ALTER TABLE project DROP COLUMN postal_code")
        conn.execute("ALTER TABLE project DROP COLUMN developer_postal_code")
