from sqlalchemy import *
from migrate import *


def upgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)
    project = Table("project", meta, autoload=True)
    pCountryStateIsoCode = Column("subdivision_1_iso_code", String(15), nullable=True)
    pCountryStateIsoCode.create(project)

    dpCountryStateIsoCode = Column("developer_subdivision_1_iso_code", String(15), nullable=True)
    dpCountryStateIsoCode.create(project)

    pCountryStateName = Column("subdivision_1_name", String(100), nullable=True)
    pCountryStateName.create(project)

    dpCountryStateName = Column("developer_subdivision_1_name", String(100), nullable=True)
    dpCountryStateName.create(project)

    subcontractor = Table("subcontractor", meta, autoload=True)
    sCountryStateIsoCode = Column("subdivision_1_iso_code", String(15), nullable=True)
    sCountryStateIsoCode.create(subcontractor)

    subcontractor = Table("subcontractor", meta, autoload=True)
    sCountryStateName = Column("subdivision_1_name", String(100), nullable=True)
    sCountryStateName.create(subcontractor)

def downgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)

    project = Table("project", meta, autoload=True)
    project.c.subdivision_1_iso_code.drop()
    project.c.developer_subdivision_1_iso_code.drop()
    project.c.subdivision_1_name.drop()
    project.c.developer_subdivision_1_name.drop()

    subcontractor = Table("subcontractor", meta, autoload=True)
    subcontractor.c.subdivision_1_iso_code.drop()
    subcontractor.c.subdivision_1_name.drop()
