#!/usr/bin/python3
"""Defines the DBStorage engine."""
from os import getenv
from models.base_model import Base, BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker


class DBStorage:
    """Represents a database storage engine.

    Attributes:
        __db_engine (sqlalchemy.Engine): The working SQLAlchemy engine.
        __db_session (sqlalchemy.Session): The working SQLAlchemy session.
    """

    __db_engine = None
    __db_session = None

    def __init__(self):
        """Initialize a new DBStorage instance."""
        self.__db_engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                        format(getenv("HBNB_MYSQL_USER"),
                                               getenv("HBNB_MYSQL_PWD"),
                                               getenv("HBNB_MYSQL_HOST"),
                                               getenv("HBNB_MYSQL_DB")),
                                        pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__db_engine)

    def all(self, cls=None):
        """Query on the current database session all objects of the given class.
        If cls is None, queries all types of objects.

        Return:
            Dict of queried classes in the format <class name>.<obj id> = obj.
        """
        if cls is None:
            objects = self.__db_session.query(State).all()
            objects.extend(self.__db_session.query(City).all())
            objects.extend(self.__db_session.query(User).all())
            objects.extend(self.__db_session.query(Place).all())
            objects.extend(self.__db_session.query(Review).all())
            objects.extend(self.__db_session.query(Amenity).all())
        else:
            if type(cls) == str:
                cls = eval(cls)
            objects = self.__db_session.query(cls)
        return {"{}.{}".format(type(obj).__name__, obj.id): obj for obj in objects}

    def new(self, obj):
        """Add obj to the current database session."""
        self.__db_session.add(obj)

    def save(self):
        """Commit all changes to the current database session."""
        self.__db_session.commit()

    def delete(self, obj=None):
        """Delete obj from the current database session."""
        if obj is not None:
            self.__db_session.delete(obj)

    def reload(self):
        """Create all tables in the database and initialize a new session."""
        Base.metadata.create_all(self.__db_engine)
        session_factory = sessionmaker(bind=self.__db_engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__db_session = Session()

    def close(self):
        """Close the working SQLAlchemy session."""
        self.__db_session.close()
