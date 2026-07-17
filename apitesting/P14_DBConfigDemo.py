import mysql.connector
from utilities.configurations import *

conn = getConnection() # from configurations.py
print(conn.is_connected())
cursor = conn.cursor()
cursor.execute('select * from CustomerInfo')

rows = cursor.fetchall()
print(type(rows))
print(rows)
sum = 0
for row in rows:  #('selenium', datetime.date(2020, 6, 7), 120, 'Africa')
    sum = sum + row[2]

print(sum)
assert sum == 361

conn.close()




