from sqlalchemy import *
from migrate import *

meta = MetaData()

tbl = Table("subcontractor", meta)

col0 = Column("description", String(255), nullable=True)
col1 = Column(
    "country_id",
    Integer,
    ForeignKey(
        "country.geoname_id",
        name="fk__subcontractor__country_id",
        ondelete="CASCADE",
        onupdate="CASCADE",
    ),
    nullable=True,
)
col2 = Column(
    "city_id",
    Integer,
    ForeignKey(
        "city.geoname_id",
        name="fk__subcontractor__city_id",
        ondelete="CASCADE",
        onupdate="CASCADE",
    ),
    nullable=True,
)
col3 = Column("state_id", String(15), nullable=True)
col4 = Column("postal_code", String(30), nullable=True)


def upgrade(migrate_engine):
    meta.bind = migrate_engine
    Table("country", meta, autoload=True)
    Table("city", meta, autoload=True)
    col0.create(tbl)
    col1.create(tbl)
    col2.create(tbl)
    col3.create(tbl)
    col4.create(tbl)


def downgrade(migrate_engine):
    meta.bind = migrate_engine
    with migrate_engine.connect() as conn:
        conn.execute("ALTER TABLE subcontractor DROP COLUMN description")

        conn.execute(
            "ALTER TABLE subcontractor DROP CONSTRAINT fk__subcontractor__country_id"
        )
        conn.execute("ALTER TABLE subcontractor DROP COLUMN country_id")

        conn.execute(
            "ALTER TABLE subcontractor DROP CONSTRAINT fk__subcontractor__city_id"
        )
        conn.execute("ALTER TABLE subcontractor DROP COLUMN city_id")

        conn.execute("ALTER TABLE subcontractor DROP COLUMN state_id")

        conn.execute("ALTER TABLE subcontractor DROP COLUMN postal_code")

