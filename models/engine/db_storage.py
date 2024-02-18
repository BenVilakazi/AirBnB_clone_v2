#!/usr/bin/python3
'''database storage engine'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.amenity import Amenity
from models.base_model import Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State,
           "User": User}


class DBStorage:
    """Defines class for database storage"""
from os import getenv

if getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.place import place_amenity

classes = {"User": User, "State": State, "City": City,
           "Amenity": Amenity, "Place": Place, "Review": Review}


class DBStorage:
    '''database storage engine for mysql storage'''
    __engine = None
    __session = None

    def __init__(self):
        """Instantiation of DBStorage instance"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(getenv('HBNB_MYSQL_USER'),
                                             getenv('HBNB_MYSQL_PWD'),
                                             getenv('HBNB_MYSQL_HOST'),
                                             getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session all
        objects depending of the class name"""
        obj_lists = []
        if cls is None:
            all_classes = [Amenity, City, Place, Review, State, User]
            for obj in all_classes:
                obj_list.extend()

        else:
            if type(cls) == str:
                cls = classes[cls]
            elif cls not in classes.values():
                return
            obj_list = self.__session.query(cls).all()
        obj_dict = {"{}.{}".format(v.__class__.__name, v.id):
                    v for v in obj_list}

        return obj_dict

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """closes the working SQLAlchemy session"""
        self.__session.close()
