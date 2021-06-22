from sqlalchemy import *

meta = MetaData()

tbl = Table("project", meta)

name = Column("developer_name", String(40), default="")
city = Column(
    "developer_city_id",
    Integer,
    ForeignKey(
        "city.geoname_id",
        name="fk__project__developer_city__id",
        onupdate="CASCADE",
    ),
    nullable=True,
)
country = Column(
    "developer_country_id",
    Integer,
    ForeignKey(
        "country.geoname_id",
        name="fk__project__developer_country__id",
        onupdate="CASCADE",
    ),
    nullable=True,
)
address_line_one = Column("developer_address_line_one", String(256), default="")
address_line_two = Column("developer_address_line_two", String(256), default="")
contact = Column("developer_contact_person", String(100), default="")
email = Column("developer_email", String(50), default="")
phone = Column("developer_phone_number", String(25), default="")
warranty = Column("developer_warranty", String(255), default="")


def upgrade(migrate_engine):
    meta.bind = migrate_engine
    Table("city", meta, autoload=True)
    Table("country", meta, autoload=True)
    name.create(tbl)
    city.create(tbl)
    country.create(tbl)
    address_line_one.create(tbl)
    address_line_two.create(tbl)
    contact.create(tbl)
    email.create(tbl)
    phone.create(tbl)
    warranty.create(tbl)


def downgrade(migrate_engine):
    meta.bind = migrate_engine
    with migrate_engine.connect() as conn:
        conn.execute(
            "ALTER TABLE project DROP CONSTRAINT fk__project__developer_city__id"
        )
        conn.execute(
            "ALTER TABLE project DROP CONSTRAINT fk__project__developer_country__id"
        )
        conn.execute("ALTER TABLE project DROP COLUMN developer_name")
        conn.execute("ALTER TABLE project DROP COLUMN developer_city_id")
        conn.execute("ALTER TABLE project DROP COLUMN developer_country_id")
        conn.execute("ALTER TABLE project DROP COLUMN developer_address_line_one")
        conn.execute("ALTER TABLE project DROP COLUMN developer_address_line_two")
        conn.execute("ALTER TABLE project DROP COLUMN developer_contact_person")
        conn.execute("ALTER TABLE project DROP COLUMN developer_email")
        conn.execute("ALTER TABLE project DROP COLUMN developer_phone_number")
        conn.execute("ALTER TABLE project DROP COLUMN developer_warranty")
