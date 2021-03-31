from sqlalchemy import *
from migrate import *
from migrate.changeset.constraint import ForeignKeyConstraint


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    meta = MetaData(bind=migrate_engine)
    tbl = Table('building__level__junction', meta, autoload=True)
    building_tbl = Table('building', meta, autoload=True)
    building_level_tbl = Table('building_level', meta, autoload=True)
    ForeignKeyConstraint(columns=[tbl.c.building_id], refcolumns=[building_tbl.c.id],
                         name='building__level__junction_ibfk_1', ondelete='CASCADE', onupdate='CASCADE').create()
    ForeignKeyConstraint(columns=[tbl.c.building_level_id], refcolumns=[building_level_tbl.c.id],
                         name='building__level__junction_ibfk_2', ondelete='CASCADE', onupdate='CASCADE').create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    meta = MetaData(bind=migrate_engine)
    tbl = Table('building__level__junction', meta, autoload=True)
    building_tbl = Table('building', meta, autoload=True)
    building_level_tbl = Table('building_level', meta, autoload=True)
    ForeignKeyConstraint(columns=[tbl.c.building_id], refcolumns=[building_tbl.c.id],
                         name='building__level__junction_ibfk_1').drop()
    ForeignKeyConstraint(columns=[tbl.c.building_level_id], refcolumns=[building_level_tbl.c.id],
                         name='building__level__junction_ibfk_2').drop()
