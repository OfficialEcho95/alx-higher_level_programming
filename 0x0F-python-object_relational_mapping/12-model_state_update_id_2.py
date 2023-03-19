#!/usr/bin/python3
"""
A script that changes the name of a State object from the database
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # create a connection to the mysql server
    engine = create_engine(f'mysql://{username}:{password}@\
            localhost:3306/{db_name}')
    Base.metadata.create_all(engine)

    # create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # query the state with id=2 and change its name to 'New Mexico'
    state = session.query(State).filter_by(id=2).first()
    if state:
        state.name = 'New Mexico'
        session.commit()
        print("State name updated successfully")
    else:
        print("State not found")

    session.close()
