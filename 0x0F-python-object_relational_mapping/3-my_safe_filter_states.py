#!/usr/bin/python3

"""
    Safe version of 2-my_filter_states.py (Prevent sql injections)
"""

import MySQLdb
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    user_filter = sys.argv[4]

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=username,
                         passwd=password,
                         db=database)

    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name LIKE BINARY %s\
                    ORDER BY id ASC"

    cursor.execute(query, (user_filter,))

    for state in cursor.fetchall():
        print(state)

    cursor.close()
    db.close()
