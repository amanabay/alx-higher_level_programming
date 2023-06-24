#!/usr/bin/python3
"""
    Python file that contains the class definition of a State and an
    instance Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """
        State class that inherits from declarative_base
        Attributes:
            id (int): unique identifier of state(auto incremented)
            name (String): name of state
            cities(relationship): represent a relationship with the class City
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state',
                          cascade='all, delete-orphan')
