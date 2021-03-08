from sqlalchemy import *

meta = MetaData()

tbl = Table(
    'equipment_project_category__category_group__junction', meta,
    Column('id', Integer, primary_key=True),
    Column('equipment_project_category_id', String(50), ForeignKey('equipment_project_category.id'), index=True),
    Column('equipment_category_group_id', String(50), ForeignKey('equipment_category_group.id'), index=True)
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    meta.bind = migrate_engine
    _t = Table('equipment_project_category', meta, autoload=True)
    _t = Table('equipment_category_group', meta, autoload=True)
    tbl.create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    meta.bind = migrate_engine
    tbl.drop()
