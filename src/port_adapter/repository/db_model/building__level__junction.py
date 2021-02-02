"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from sqlalchemy import Column, Integer, ForeignKey, Table, String

import src.port_adapter.AppDi as AppDi

Base = AppDi.instance.get(AppDi.DbBase)

associationTable = Table('building__level__junction', Base.metadata,
                         Column('building_id', String(40), ForeignKey('building.id')),
                         Column('building_level_id', String(40), ForeignKey('building_level.id'))
                         )
