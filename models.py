""" models.py: provides models for views.py"""

__author__ = "Phil Jay Kwon"

from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    )
from sqlalchemy.ext.declarative import DeferredReflection
from sqlalchemy.ext.declarative import declarative_base


from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class Institutions(DeferredReflection, Base):
    __tablename__ = 'institutions'

class Addresses(DeferredReflection, Base):
    __tablename__ = 'addresses'

class Keys(DeferredReflection, Base):
    __tablename__ = 'inst_keys'

class Credentials(DeferredReflection, Base):
    __tablename__ = 'user_credentials'

class Accounts(DeferredReflection, Base):
    __tablename__ = 'accounts'

class Transactions(DeferredReflection, Base):
    __tablename__ = 'transactions'
