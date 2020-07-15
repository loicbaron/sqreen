#!/usr/bin/env python3
from marshmallow import ValidationError
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from project.config.environment import environment

config = {
    'SQL_DATABASE_URI': 'sqlite://{}?check_same_thread=False'.format(environment["db"]),
    'SQL_ISOLATION_LEVEL': 'SERIALIZABLE',
    'SQL_ECHO': True,
    'SQL_ECHO_POOL': False,
    'SQL_CONVERT_UNICODE': True,
    'SQL_POOL_SIZE': None,
    'SQL_POOL_TIMEOUT': None,
    #'SQL_POOL_RECYCLE': 3600,
    #'SQL_MAX_OVERFLOW': 10,
    'SQL_AUTOCOMMIT': False,
    'SQL_AUTOFLUSH': True,
    'SQL_EXPIRE_ON_COMMIT': True
}

engine = create_engine(config['SQL_DATABASE_URI'], convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import project.models
    Base.metadata.create_all(bind=engine)

def must_not_be_blank(data):
    if not data:
        raise ValidationError('Data not provided.')