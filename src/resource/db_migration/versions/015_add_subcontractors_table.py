from sqlalchemy import *

meta = MetaData()

tbl = Table(
    'subcontractor', meta,
    Column('id', String(40), primary_key=True),
    Column('company_name', String(50)),
    Column('website', String(50)),
    Column('contact_person', String(25)),
    Column('email', String(50)),
    Column('phone_number', String(30)),
    Column('address_one', String(255)),
    Column('address_two', String(255)),
    Column('modified_at', DateTime),
    Column('created_at', DateTime),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    meta.bind = migrate_engine
    tbl.create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    meta.bind = migrate_engine
    tbl.drop()
