#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

class DBStorage:
    """This class manages storage of hbnb models in a MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Creates the engine and session for database storage"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(os.getenv('HBNB_MYSQL_USER'),
                                             os.getenv('HBNB_MYSQL_PWD'),
                                             os.getenv('HBNB_MYSQL_HOST'),
                                             os.getenv('HBNB_MYSQL_DB'),
                                             pool_pre_ping=True))

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)

    def all(self, cls=None):
        """Query and return all objects based on class name"""
        objects = {}
        if cls:
            objects = self.__session.query(cls).all()
        else:
            for c in [User, State, City, Amenity, Place, Review]:
                objects.update({obj.__class__.__name__ + '.' + obj.id: obj for obj in self.__session.query(c).all()})
        return objects

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and initialize the session"""
        from models.base_model import Base
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))
