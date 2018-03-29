#!/usr/bin/python3
'''
    Implementation of the User class which inherits from BaseModel
'''
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey, Integer, DateTime
from os import environ

class User(BaseModel):
    '''
        Definition of the User class
    '''
    __tablename__ = "users"

    if (environ.get('HBNB_TYPE_STORAGE' == 'db'):
        email = Column(String(128), nullabe=False)
        password = Column(String(128), nullabe=False)
        first_name = Column(String(128), nullabe=False)
        last_name = Column(String(128), nullabe=False)
        places = relationship("Place", backref="user", cascade="delete")
        reviews = relationship("Review", backref="user", cascade="delete")

    email = ""
    password = ""
    first_name = ""
    last_name = ""
