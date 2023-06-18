#!/usr/bin/python3
"""
    Python file that contains the class definition of a city and an
    instance Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """
        City class that inherits from declarative_base
        Attributes:
            id (int): unique identifier of state(auto incremented)
            name (String): name of state
            state_id (int): id of state city is in (foreign key)
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
