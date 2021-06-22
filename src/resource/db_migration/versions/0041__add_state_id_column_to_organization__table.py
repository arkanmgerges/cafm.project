from sqlalchemy import *
from migrate import *


def upgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)
    organization = Table("organization", meta, autoload=True)
    stateId = Column("state_id", String(15), nullable=True)
    stateId.create(organization)


def downgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)
    organization = Table("organization", meta, autoload=True)
    organization.c.state_id.drop()
