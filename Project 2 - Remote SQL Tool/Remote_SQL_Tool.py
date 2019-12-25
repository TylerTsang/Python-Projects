# -*- coding: utf-8 -*-
import MySQLdb
import prettytable

from prettytable import from_db_cursor
host = raw_input('Enter host name: ')
user = raw_input('Enter User Name: ')
pw = raw_input('Enter Password: ')
database = raw_input('Enter Database: ')
db = MySQLdb.connect(host, # Host, usually local
                     user # Username
                     pw, # Password
                     database # Name of Database)
                     
# Create Cursor object
cur = db.cursor()
col = raw_input('Column Name: ')
table = raw_input('Table Name: ')
#columns = map(col, col.split())
cur.execute("SELECT " +col+" FROM " +database+ "."+table+"")
pt = from_db_cursor(cur)
print(pt)
cur.close()
                     