#!/usr/bin/python3
'''prints all City objects from the database hbtn_0e_14_usa
'''
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


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
    for city in session.query(City).order_by(City.id):
        state = session.query(State).filter(State.id == city.state_id).one()
        print(f"{state.name}: ({city.id}) {city.name}")
    session.close()
