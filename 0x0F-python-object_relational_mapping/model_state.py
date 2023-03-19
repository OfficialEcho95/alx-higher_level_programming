#!/usr/bin/python3
'''
This module contains the class definition of a state
and an instance Base = declarative_base()
'''
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql://localhost:3306/mydatabase')

Base = declarative_base()


class State (Base):
    """ the class inheriting the declarative base"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)


if __name__ == '__main__':
    from sqlalchemy import create_engine
    engine = create_engine('mysql://localhost:3306/mydatabase')
    Base.metadata.create_all(engine)
