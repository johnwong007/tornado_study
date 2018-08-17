import MySQLdb

db = MySQLdb.connect("localhost", "root", "Root#123", "sdc", charset='utf8')

cursor = db.cursor()

cursor.execute('select login_name from login where id=10010')

data = cursor.fetchone()

print(data)
