#!/usr/bin/python3
'''
    Implementation of the State class
'''

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from os import environ
import models


class State(BaseModel, Base):
    '''
        Implementation for the State.
    '''
    if environ.get("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="delete")
    else:
        @property
        def cities(self):
            cityl = []
            allc = models.storage.all(City)
            for key, value in allc.items():
                if value.state_id == self.id:
                    cityl.append(value)
            return cityl
