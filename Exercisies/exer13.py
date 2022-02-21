import sqlite3

dbname = input("DB名を入力: ")
tablename = input("table名を入力: ")
conn = sqlite3.connect(dbname+".db")
cur = conn.cursor()

query = "CREATE TABLE " + tablename + "(id INTEGER PRIMARY KEY, name STRING)"
cur.execute(query)

while True:
    command = input("操作を決定してください(1:表示 2:挿入 3:終了): ")
    if command == "1":
        query = "SELECT * FROM " + tablename
        cur.execute(query)
        print(cur.fetchall())
    elif command == "2":
        input_id = input("idを入力: ")
        input_name = input("nameを入力: ")
        query = "INSERT INTO " + tablename + "(id, name) values("+input_id+", '"+input_name+"')"
        cur.execute(query)
    elif command == "3":
        print("終了します")
        break
    else:
        print("正しいコマンドを入力してください")

conn.commit()
conn.close()