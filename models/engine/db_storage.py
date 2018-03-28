#!/usr/bin/python3
"""
database storage
"""
import models
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from sqlalchemy import create_engine, Column, String
from os import environ
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session


class DBStorage:
    """
    objects to a database
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        makes class
        """
        usr = environ.get("HBNB_MYSQL_USER")
        passwd = environ["HBNB_MYSQL_PWD"]
        host = environ["HBNB_MYSQL_HOST"]
        db = environ["HBNB_MYSQL_DB"]

        self.__engine = create_engine('mysql.mysqldb://{}:{}@{}/{}'.
                                      format(usr, passwd, host, db),
                                      pool_pre_ping=True)

        if environ.get("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        will return objects
        """
        allobj = {}
        if not cls:
            for key, value in models.classes.items():
                result = self.__session.query(value)
                for i in result:
                    k = str(i.__class__.__name__) + "." + str(i.id)
                    allobj[k] = i

        else:
            if type(cls) == str:
                cls = models.classes[cls]

            result = self.__session.query(cls)
            for i in result:
                k = str(i.__class__.__name__) + "." + str(i.id)
                allobj[k] = i

        return allobj

    def new(self, obj):
        """
        add object to session
        """
        self.__session.add(obj)

    def delete(self, obj=None):
        """
        delete database session if obj is not none
        """
        if obj:
            self.__session.delete(obj)
            self.__session.commit()

    def reload(self):
        """
        create all tables
        """
        Base.etadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
