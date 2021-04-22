"""
@author: Mohammad S. moso<moso@develoop.run>
"""

from sqlalchemy import Column, Integer, ForeignKey, Table

import src.port_adapter.AppDi as AppDi

Base = AppDi.instance.get(AppDi.DbBase)
ROLE__ORGANIZATION__JUNCTION = 'role__organization__junction'
associationTable = Table('role__organization__junction', Base.metadata,
                         Column('role_id', Integer, ForeignKey('role.id', ondelete='CASCADE', onupdate='CASCADE')),
                         Column('organization_id', Integer,
                                ForeignKey('organization.id', ondelete='CASCADE', onupdate='CASCADE')))
