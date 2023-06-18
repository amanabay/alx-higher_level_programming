#!/usr/bin/python3

"""
    Script that takes in the name of a state as an argument and
    lists all cities of that state, using the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=username,
                         passwd=password,
                         db=database)

    cursor = db.cursor()

    query = "SELECT c.name\
             FROM cities c, states s\
             WHERE c.state_id = s.id AND s.name LIKE BINARY %s\
             ORDER BY c.id ASC"

    cursor.execute(query, (state_name,))

    print(", ".join(city[0] for city in cursor.fetchall()))

    cursor.close()
    db.close()
