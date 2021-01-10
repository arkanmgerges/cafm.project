from sqlalchemy import *
from migrate import *


meta = MetaData()

tbl = Table(
    'user_organization_juction', meta,
    Column('id', String(40), primary_key=True),
    Column('user_id', String(50), ForeignKey('user.id'), index=True),
    Column('organization_id', String(50), ForeignKey('organization.id'), index=True)
)

def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    meta.bind = migrate_engine
    _t = Table('user', meta, autoload=True)
    _t = Table('organization', meta, autoload=True)
    tbl.create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    meta.bind = migrate_engine
    tbl.drop()
