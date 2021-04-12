from sqlalchemy import *

meta = MetaData()


def upgrade(migrate_engine):
    meta.bind = migrate_engine
    tbl = Table('project', meta, autoload=True)
    col = Column('address_line_two', String(256), default="")
    col.create(tbl)


def downgrade(migrate_engine):
    meta.bind = migrate_engine
    with migrate_engine.connect() as conn:
        conn.execute('ALTER TABLE project DROP COLUMN address_line_two')
