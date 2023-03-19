#!/usr/bin/python3
"""
A script that deletes all State objects with a name containing the letter a
from the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    # Get command line arguments
    mysql_user = sys.argv[1]
    mysql_pwd = sys.argv[2]
    db_name = sys.argv[3]

    # Create a connection to the database
    engine = create_engine(f'mysql://{mysql_user}:{mysql_pwd}@\
            localhost:3306/{db_name}')

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Delete all State objects with a name containing the letter 'a'
    states = session.query(State).filter(State.name.like('%a%'))
    for state in states:
        session.delete(state)

    # Commit the changes to the database
    session.commit()

    # Close the session
    session.close()
