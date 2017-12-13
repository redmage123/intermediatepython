#!/usr/bin/env python3


import psycopg2
import psycopg2.extras

try:
    conn = psycopg2.connect("dbname = 'northwind' user='student' password='student:123' ")
except Exception as e:
    print (e)

#cur = conn.cursor()
dict_cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
#cur.execute('select * from categories')
dict_cur.execute('select * from categories')
rows = dict_cur.fetchone()
print (type(rows))

