from sqlalchemy import *
from migrate import *


def upgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)

    organization = Table("organization", meta, autoload=True)
    organization.c.state_id.drop()

    user = Table("user", meta, autoload=True)
    user.c.state_id.drop()


def downgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)

    user = Table("user", meta, autoload=True)
    stateId = Column("state_id", String(15), nullable=True)
    stateId.create(user)

    organization = Table("organization", meta, autoload=True)
    stateId = Column("state_id", String(15), nullable=True)
    stateId.create(organization)
