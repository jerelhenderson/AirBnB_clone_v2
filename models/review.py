#!/usr/bin/python3
'''
    Implementation of the Review class
'''

from models.base_model import BaseModel


class Review(BaseModel):
    '''
        Implementation for the Review.
    '''
    __tablename__ = "reviews"

    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)

    if None:
        return
    else:
        place_id = ""
        user_id = ""
        text = ""
