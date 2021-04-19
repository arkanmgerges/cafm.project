from sqlalchemy import *
from migrate import *

meta = MetaData()

tbl = Table('standard_maintenance_procedure', meta)

col = Column('standard_equipment_category_group_id', String(40),
             ForeignKey('standard_equipment_category_group.id',
                        name='fk__maintenance_procedure__st_eq_cat_gr__id',
                        ondelete='CASCADE',
                        onupdate='CASCADE'),
             nullable=True
)


def upgrade(migrate_engine):
    meta.bind = migrate_engine
    Table('standard_equipment_category_group', meta, autoload=True)
    col.create(tbl)


def downgrade(migrate_engine):
    meta.bind = migrate_engine
    with migrate_engine.connect() as conn:
        conn.execute('ALTER TABLE maintenance_procedure DROP CONSTRAINT fk__maintenance_procedure__st_eq_cat_gr__id')
        conn.execute('ALTER TABLE maintenance_procedure DROP COLUMN standard_equipment_category_group_id')
