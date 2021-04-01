from sqlalchemy import *
from migrate import *

meta = MetaData()

tbl = Table(
    'user__role__junction', meta,
    Column('id', Integer, primary_key=True),
    Column('user_id', String(50), ForeignKey('user.id', name='fk__user__role__junction__user__id', ondelete='CASCADE', onupdate='CASCADE')),
    Column('role_id', String(50), ForeignKey('role.id', name='fk__user__role__junction__role__id', ondelete='CASCADE', onupdate='CASCADE'))
)

def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    meta.bind = migrate_engine
    _t = Table('user', meta, autoload=True)
    _t = Table('role', meta, autoload=True)
    Index('ix__user__role__junction__user_id', tbl.c.user_id)
    Index('ix__user__role__junction__role_id', tbl.c.role_id)
    tbl.create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    meta.bind = migrate_engine
    tbl.drop()
