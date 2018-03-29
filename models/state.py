#!/usr/bin/python3
'''
    Implementation of the State class
'''

from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey, Integer, DateTime
from os import environ

class State(BaseModel, Base):
    '''
        Implementation for the State.
    '''
    __tablename__ = "states"

    if (environ.get('HBNB_TYPE_STORAGE') == 'db'):
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="delete")

        @property
        def cities(self):
        '''
        getter for cities using FileStorage
        '''
        city_dict = models.storage.all(City)

        state_cities = []
        for key, value in city_dict:
            if value.state_id == self.id:
                state_cities.append(value)
            return state_cities

    name = ""
