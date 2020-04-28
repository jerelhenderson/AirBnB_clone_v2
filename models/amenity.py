#!/usr/bin/python3
'''
    Implementation of the Amenity class
'''
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import environ


class Amenity(BaseModel):
    '''
        Implementation for the Amenities.
    '''
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
