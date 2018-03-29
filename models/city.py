#!/usr/bin/python3
'''
    Define the class City.
'''
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey, Integer, DateTime
from os import environ

class City(BaseModel):
    '''
        Define the class City that inherits from BaseModel.
    '''
    __tablename__ = "cities"

    if (environ.get('HBNB_TYPE_STORAGE') == 'db'):
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

    places = relationship("Place", backref="cities", cascade="delete")

    state_id = ""
    name = ""
