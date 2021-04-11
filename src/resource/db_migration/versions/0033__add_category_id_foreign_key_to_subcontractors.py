from sqlalchemy import *
from migrate import *

meta = MetaData()

tbl = Table('subcontractor', meta)

col = Column('subcontractor_category_id', String(40),
             ForeignKey('subcontractor_category.id',
                        name='fk__subcontractor__subcontractor_category__id',
                        ondelete='CASCADE',
                        onupdate='CASCADE'),
             nullable=True
)


def upgrade(migrate_engine):
    meta.bind = migrate_engine
    Table('subcontractor_category', meta, autoload=True)
    col.create(tbl)


def downgrade(migrate_engine):
    meta.bind = migrate_engine
    with migrate_engine.connect() as conn:
        conn.execute('ALTER TABLE subcontractor DROP CONSTRAINT fk__subcontractor__subcontractor_category__id')
        conn.execute('ALTER TABLE subcontractor DROP COLUMN subcontractor_category_id')
