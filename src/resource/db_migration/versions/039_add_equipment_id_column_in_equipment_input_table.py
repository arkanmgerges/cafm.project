from sqlalchemy import *
from migrate import *


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    meta = MetaData(bind=migrate_engine)
    tbl = Table('equipment_input', meta, autoload=True)
    equipmentTable = Table('equipment', meta, autoload=True)
    col = Column('equipment_id', String(40), ForeignKey(equipmentTable.c.id, name='equipment_input_equipment_id_fkey', ondelete='CASCADE'), nullable=False)
    col.create(tbl)



def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    meta = MetaData(bind=migrate_engine)
    tbl = Table('equipment_input', meta, autoload=True)
    equipmentTable = Table('equipment', meta, autoload=True)
    fkc = ForeignKeyConstraint(columns=[tbl.c.equipment_id], refcolumns=[equipmentTable.c.id], name='equipment_input_equipment_id_fkey')
    fkc.drop()
    tbl.c.equipment_id.drop()
