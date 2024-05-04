#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
import models
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name =Column(String(128), nullable=False)
    cities = relationship('City', cascade='all, delete, delete-orphan',
                          backref='state')

    @property
    def cities(self):
        """return a list of City instances with state_id == State.id"""
        from models import storage
        list_cities = []
        for city in storage.all(City).values():
            if city.state_id == self.id:
                list_cities.append(city)
        return list_cities
