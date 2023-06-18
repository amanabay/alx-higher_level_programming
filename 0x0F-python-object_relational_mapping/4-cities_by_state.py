#!/usr/bin/python3

"""
    Script that lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=username,
                         passwd=password,
                         db=database)

    cursor = db.cursor()

    query = "SELECT c.id, c.name, s.name\
             FROM cities c, states s\
             WHERE c.state_id = s.id\
             ORDER BY c.id ASC"

    cursor.execute(query)

    for city in cursor.fetchall():
        print(city)

    cursor.close()
    db.close()
