from sqlalchemy import *
from migrate import *

meta = MetaData()

tbl = Table(
    'equipment', meta,
    Column('id', String(40), primary_key=True),
    Column('name', String(40)),
    Column('quantity', Integer),
    Column('project_id', String(40), ForeignKey('project.id', ondelete='CASCADE'), nullable=False),
    Column('equipment_project_category_id', String(40), ForeignKey('equipment_project_category.id', ondelete='CASCADE'), nullable=False),
    Column('equipment_category_id', String(40), ForeignKey('equipment_category.id', ondelete='CASCADE'), nullable=False),
    Column('equipment_category_group_id', String(40), ForeignKey('equipment_category_group.id', ondelete='CASCADE'), nullable=False),
    Column('building_id', String(40), ForeignKey('building.id', ondelete='CASCADE'), nullable=False),
    Column('building_level_id', String(40), ForeignKey('building_level.id', ondelete='CASCADE'), nullable=False),
    Column('building_level_room_id', String(40), ForeignKey('building_level_room.id', ondelete='CASCADE'), nullable=False),
    Column('manufacturer_id', String(40), ForeignKey('manufacturer.id', ondelete='CASCADE'), nullable=False),
    Column('equipment_model_id', String(40), ForeignKey('equipment_model.id', ondelete='CASCADE'), nullable=False),
    Column('modified_at', DateTime),
    Column('created_at', DateTime),
)

def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    meta.bind = migrate_engine
    Table('project', meta, autoload=True)
    Table('equipment_project_category', meta, autoload=True)
    Table('equipment_category', meta, autoload=True)
    Table('equipment_category_group', meta, autoload=True)
    Table('building', meta, autoload=True)
    Table('building_level', meta, autoload=True)
    Table('building_level_room', meta, autoload=True)
    Table('manufacturer', meta, autoload=True)
    Table('equipment_model', meta, autoload=True)
    tbl.create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    meta.bind = migrate_engine
    tbl.drop()
