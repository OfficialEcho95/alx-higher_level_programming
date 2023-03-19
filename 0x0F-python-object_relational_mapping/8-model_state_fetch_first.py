#!/usr/bin/python3
"""
A module that prints the first state object from the database
"""
from model_state import Base, State
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # we create a connection to the mysql server
    engine = create_engine(f'mysql://{username}:{password}@localhost:3306/\
                           {db_name}')

    # session created
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).first()

    if states is None:
        print("Nothing")
    else:
        print("{}: {}".format(state.id, state.name))
