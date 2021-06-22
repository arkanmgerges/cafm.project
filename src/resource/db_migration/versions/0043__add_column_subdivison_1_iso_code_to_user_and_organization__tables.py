from sqlalchemy import *
from migrate import *


def upgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)
    user = Table("user", meta, autoload=True)
    uCountryStateIsoCode = Column("subdivision_1_iso_code", String(15), nullable=True)
    uCountryStateIsoCode.create(user)

    organization = Table("organization", meta, autoload=True)
    oCountryStateIsoCode = Column("subdivision_1_iso_code", String(15), nullable=True)
    oCountryStateIsoCode.create(organization)


def downgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)

    user = Table("user", meta, autoload=True)
    user.c.subdivision_1_iso_code.drop()

    organization = Table("organization", meta, autoload=True)
    organization.c.subdivision_1_iso_code.drop()
