from sqlalchemy import *

meta = MetaData()

tbl = Table(
    'equipment_project_category__category_group__junction', meta,
    Column('id', Integer, primary_key=True),
    # There is a limit on the foreign key name, 64 chars
    Column('equipment_project_category_id', String(40), ForeignKey('equipment_project_category.id', name='fk__equip_proj_cat__cat_grp__junction__equip_proj_cat__id', ondelete='CASCADE', onupdate='CASCADE')),
    Column('equipment_category_group_id', String(40), ForeignKey('equipment_category_group.id', name='fk__equip_proj_cat__cat_grp__junction__equip_cat_grp__id', ondelete='CASCADE', onupdate='CASCADE'))
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    meta.bind = migrate_engine
    _t = Table('equipment_project_category', meta, autoload=True)
    _t = Table('equipment_category_group', meta, autoload=True)

    Index('ix__equip_proj_cat__cat_grp__junction__equip_proj_cat_id', tbl.c.equipment_project_category_id)
    Index('ix__equip_proj_cat__cat_grp__junction__equip_cat_grp_id', tbl.c.equipment_category_group_id)
    tbl.create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    meta.bind = migrate_engine
    tbl.drop()
