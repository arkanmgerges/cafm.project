meta = MetaData()

tbl = Table(
    'user', meta,
    Column('id', String(40), primary_key=True),
    Column('email', String(50)),
    Column('first_name', String(25)),
    Column('last_name', String(25)),
    Column('address_one', String(255)),
    Column('address_two', String(255)),
    Column('postal_code', String(30)),
    Column('phone_number', String(30)),
    Column('avatar_image', String(255)),
    Column('country_id', Integer, ForeignKey('country.geoname_id'), nullable=False),
    Column('city_id', Integer, ForeignKey('city.geoname_id'), nullable=False),
    Column('subdivision_1_name', String(100)),
    Column('start_date', DateTime, nullable=True),
    Column('modified_at', DateTime),
    Column('created_at', DateTime)
)

def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    meta.bind = migrate_engine
    _t = Table('country', meta, autoload=True)
    _t = Table('city', meta, autoload=True)
    tbl.create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    meta.bind = migrate_engine
    tbl.drop()
