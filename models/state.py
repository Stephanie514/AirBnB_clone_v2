#!/usr/bin/python3
"""Defines the State class."""
import models
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.city import City
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """This represents state for a MySQL database.
    Inherits from SQLAlchemy Base. Links to MySQL table states.
    Attributes:
        __tablename__ (str): name of MySQL table to store States.
        name (sqlalchemy String): name of state.
        thecities (sqlalchemy relationship): State-City relationship.
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    thecities = relationship("City",  backref="state", cascade="delete")
    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def thecities(self):
            """Get a list of all related City objects."""
            LIST_city = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    LIST_city.append(city)
            return LIST_city
