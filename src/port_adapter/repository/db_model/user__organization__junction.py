"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from sqlalchemy import Column, Integer, ForeignKey, Table

import src.port_adapter.AppDi as AppDi

Base = AppDi.instance.get(AppDi.DbBase)

associationTable = Table('user__organization__junction', Base.metadata,
                         Column('user_id', Integer, ForeignKey('user.id')),
                         Column('organization_id', Integer, ForeignKey('organization.id'))
                         )
