#!/usr/bin/python3
'''lists all cities and their corresponding states
from hbtn_0e_0_usa
'''
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], port=3306,
                         host="localhost", db=sys.argv[3])
    c = db.cursor()
    c.execute(
        '''SELECT cities.id, cities.name, states.name FROM cities INNER JOIN'''
        + ''' states ON cities.state_id = states.id ORDER BY cities.id ASC'''
    )
    for row in c.fetchall():
        print(row)
