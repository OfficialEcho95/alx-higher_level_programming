#!/usr/bin/python3
"""
A module that prints the state object with the given name from the database
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # we create a connection to the mysql server
    engine = create_engine(f'mysql://{username}:{password}@localhost:3306/\
                           {db_name}')
    Base.metadata.create_all(engine)

    # session created
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == state_name)

    if state is None:
        print("Not found")
    else:
        print(state.id)

    session.close()
