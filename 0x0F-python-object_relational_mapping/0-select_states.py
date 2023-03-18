#!/usr/bin/python3
'''
This module lists all states from the db
'''
from MySQLdb import _mysql
db = _mysql.connect(user="Emmanuel", password="password",
                    database="hbtn_0e_0_usa")
db.query("""SELECT states FROM hbtn_0e_0_usa""")
result = db.store_result()

for state in result.fetch_row(maxrows=0):
    print(state[0])
