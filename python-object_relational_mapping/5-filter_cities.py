#!/usr/bin/python3
'''lists all cities filtered by their corresponding states
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
        + ''' states ON cities.state_id = states.id WHERE states.name = %s'''
        + ''' ORDER BY cities.id ASC''',
        (sys.argv[4],)
    )
    result = [item[1] for item in c.fetchall()]
    print(", ".join(result))
