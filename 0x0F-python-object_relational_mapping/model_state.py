#!/usr/bin/python3
'''
This module contains the class definition of a state
and an instance Base = declarative_base()
'''
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql://localhost:3306/mydatabase')

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'
    id = ColumnInteger, primary_key=True, nullable=False,\
                autoincrement=True
    name = Column(String(128), nullable=False)

    Base.metadata.create_all(engine)
