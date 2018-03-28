#!/usr/bin/python3
'''
    Implementation of the State class
'''

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City
from os import environ
import models


class State(BaseModel):
    '''
        Implementation for the State.
    '''
    if environ.get("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="delete")
    else:
        name = ""

        @property
        def cities(self):
            c_dict = models.storage.all(City)
            stateq = self.id
            cityl = []
            for key, value in c_dict.items():
                if value.state_id == self.id:
                    cityl.append(value)
            return cityl
