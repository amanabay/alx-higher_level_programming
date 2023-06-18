#!/usr/bin/python3

"""
    Script that takes in an argument and displays all values in the states
    table of hbtn_0e_0_usa where name matches the argument
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

    cursor.execute("SELECT * FROM states WHERE name = '{}'\
                    ORDER BY id ASC".format(user_filter))

    for state in cursor.fetchall():
        print(state)

    cursor.close()
    db.close()
