

from sqlalchemy import *
from migrate import *
from migrate.changeset.constraint import ForeignKeyConstraint


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    meta = MetaData(bind=migrate_engine)
    tbl = Table('equipment_category_group', meta, autoload=True)
    equipment_category_tbl = Table('equipment_category', meta, autoload=True)
    ForeignKeyConstraint(columns=[tbl.c.equipment_category_id], refcolumns=[equipment_category_tbl.c.id],
                         name='equipment_category_group_ibfk_1', ondelete='CASCADE', onupdate='CASCADE').create()



def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    meta = MetaData(bind=migrate_engine)
    tbl = Table('equipment_category_group', meta, autoload=True)
    equipment_category_tbl = Table('equipment_category', meta, autoload=True)
    ForeignKeyConstraint(columns=[tbl.c.equipment_category_id], refcolumns=[equipment_category_tbl.c.id],
                         name='equipment_category_group_ibfk_1').drop()
