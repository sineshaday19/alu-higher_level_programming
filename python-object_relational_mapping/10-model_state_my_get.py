#!/usr/bin/python3
'''a script that lists all State objects matching argument
from the database hbtn_0e_6_usa
'''
from sqlalchemy import create_engine
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import NoResultFound
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{user}:{passwd}@localhost:3306/{db}".format(
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            pool_pre_ping=True)
    )
    engine.connect()
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        state = session.query(State).filter(State.name == sys.argv[4]).one()
        print(f"{state.id}")
    except NoResultFound:
        print("Not found")
    session.close()
