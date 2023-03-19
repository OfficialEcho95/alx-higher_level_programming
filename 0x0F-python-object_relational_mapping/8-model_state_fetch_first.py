#!/usr/bin/python3
"""
A module that prints the first state object from the database
"""
from model_state import Base, State
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # we create a connection to the mysql server
    engine = create_engine(f'mysql://{username}:{password}@localhost:3306/\
                           {db_name}')
    Base.metadata.create_all(engine)

    # session created
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State[0]).order_by(State.id[0])

    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()

