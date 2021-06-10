from sqlalchemy import *
from migrate import *

meta = MetaData()

def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    meta.bind = migrate_engine
    try:
        with migrate_engine.connect() as conn:
            conn.execute(
                "ALTER TABLE daily_check_procedure DROP CONSTRAINT fk__daily_check_procedure__equipment_category_group__id"
            )
    except:
        pass


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    # Upgrade operations go here. Don't create your own engine; bind
    meta.bind = migrate_engine
    # with migrate_engine.connect() as conn:
    #     conn.execute(
    #         """
    #         ALTER TABLE daily_check_procedure
    #         ADD CONSTRAINT fk__daily_check_procedure__equipment_category_group__id
    #         FOREIGN KEY (equipment_category_group_id) REFERENCES equipment_category_group (id)
    #         """
    #     )
