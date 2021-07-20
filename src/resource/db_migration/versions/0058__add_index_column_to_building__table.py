from sqlalchemy import *
from migrate import *


def upgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)
    building = Table("building", meta, autoload=True)
    index = Column("index", Integer)
    index.create(building)
    UniqueConstraint("index", name="ix__building__index", table=building).create()
    with migrate_engine.connect() as conn:
        conn.execute("ALTER TABLE building CHANGE `index` `index` INT(10) AUTO_INCREMENT")


def downgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)
    building = Table("building", meta, autoload=True)
    building.c.index.drop()