from sqlalchemy import *
from migrate import *

meta = MetaData()

# Note that here you use Table instance
# not the class derived from sqlalchemy.ext.declarative.declarative_base
tbl = Table(
    'subcontractor',
    meta,
)

col = Column('subcontractor_category_id', String(40),
             ForeignKey('subcontractor_category.id',
                        name='fk__subcontractor__subcontractor_category__id',
                        ondelete='CASCADE',
                        onupdate='CASCADE'),
             nullable=True
)


def upgrade(migrate_engine):
    meta.bind = migrate_engine
    col.create(tbl)


def downgrade(migrate_engine):
    meta.bind = migrate_engine
    tbl.append_column(col)
    tbl.c.subcontractor_category_id.drop()
