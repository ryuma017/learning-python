import sqlite3

dbname = "test.db"
tablename = "member"
conn = sqlite3.connect(dbname)
cur = conn.cursor()

query = "CREATE TABLE " + tablename + "(id INTEGER PRIMARY KEY, name STRING)"
cur.execute(query)

query = "INSERT INTO " + tablename + "(id, name) values(1, 'Taro')"
cur.execute(query)

query = "INSERT INTO " + tablename + "(id, name) values(2, 'Ziro')"
cur.execute(query)

query = "INSERT INTO " + tablename + "(id, name) values(3, 'Hanako')"
cur.execute(query)

query = "SELECT * FROM " + tablename
cur.execute(query)
print(cur.fetchall())

conn.commit()
conn.close()