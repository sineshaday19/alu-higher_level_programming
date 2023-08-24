#!/usr/bin/python3
''' lists all states with a name starting with N (upper N)
 from the database hbtn_0e_0_usa
'''
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, db=sys.argv[3],
                         user=sys.argv[1], passwd=sys.argv[2])
    c = db.cursor()
    c.execute("SELECT * FROM states ORDER BY states.id ASC")
    for row in c.fetchall():
        if row[1][0] in ['N']:
            print(row)
