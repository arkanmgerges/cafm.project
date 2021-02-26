from sqlalchemy import *
from migrate import *

meta = MetaData()

tbl = Table(
    'maintenance_procedure_operation', meta,
    Column('id', String(40), primary_key=True),
    Column('name', String(40)),
    Column('maintenance_procedure_id', String(40), ForeignKey('maintenance_procedure.id', ondelete='CASCADE'), nullable=False),
    Column('description', String(255)),
    Column('type', String(40)),
    Column('modified_at', DateTime),
    Column('created_at', DateTime),
)

def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    meta.bind = migrate_engine
    Table('maintenance_procedure', meta, autoload=True)
    tbl.create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    meta.bind = migrate_engine
    tbl.drop()
