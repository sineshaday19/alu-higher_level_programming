#!/usr/bin/python3
'''a script that lists first State object from the database hbtn_0e_6_usa
'''
from sqlalchemy import create_engine
import sys
from sqlalchemy.orm import sessionmaker
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
    state = session.query(State).order_by(State.id).first()
    if state is not None:
        print(f"{state.id}: {state.name}")
    else:
        print("Nothing")
    session.close()
