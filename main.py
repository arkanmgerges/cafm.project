import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative.api import declarative_base
from sqlalchemy.orm.session import Session
from sqlalchemy.sql.schema import Table, Column, ForeignKey
from sqlalchemy import MetaData
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy.orm import relationship

print(sqlalchemy.__version__)
engine = create_engine('mysql+mysqldb://root:1234@127.0.0.1')
engine.execute(f"CREATE DATABASE IF NOT EXISTS `cafm-project`")
engine = create_engine('mysql+mysqldb://root:1234@127.0.0.1/cafm-project')

metadata = MetaData()
Table(
    "address",
    metadata,
    Column('id', Integer, primary_key=True),
    Column('email_address', String(50), nullable=False)
)

# metadata.create_all(engine)
metadata.drop_all(engine)

Base = declarative_base()

class User(Base):
     __tablename__ = 'user_account'

     id = Column(Integer, primary_key=True)
     name = Column(String(30))
     fullname = Column(String(30))

     addresses = relationship("Address", back_populates="user")

     def __repr__(self):
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"

class Address(Base):
     __tablename__ = 'address'

     id = Column(Integer, primary_key=True)
     email_address = Column(String(30), nullable=False)
     user_id = Column(Integer, ForeignKey('user_account.id'))

     user = relationship("User", back_populates="addresses")

     def __repr__(self):
         return f"Address(id={self.id!r}, email_address={self.email_address!r})"

Base.metadata.create_all(engine)


sandy = User(name="sandy", fullname="Sandy Cheeks")
session = Session(engine)
session.add(sandy)
session.commit()
# session.flush()

