"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.sql.sqltypes import DateTime

import src.port_adapter.AppDi as AppDi

Base = AppDi.instance.get(AppDi.DbBase)
class User(Base):
    __tablename__ = 'user'
    id = Column('id', String(40), primary_key=True)
    name = Column('name', String(50))
    firstName = Column('first_name', String(25))
    lastName = Column('last_name', String(25))
    addressOne = Column('address_one', String(255))
    addressTwo = Column('address_two', String(255))
    postalCode = Column('postal_code', String(30))
    avatarImage = Column('avatar_image', String(255))
    createdAt = Column('created_at', DateTime, nullable=True, default=datetime.utcnow())
    modifiedAt = Column('modified_at', DateTime, nullable=True, onupdate=datetime.utcnow())

    def __repr__(self):
        return f"[Repo DB Model] User(id='{self.id}', name='{self.name}', \
                firstName='{self.firstName}', lastName='{self.lastName}', addressOne='{self.addressOne}', \
                addressTwo='{self.addressTwo}', postalCode='{self.postalCode}', avatarImage='{self.avatarImage}')"
