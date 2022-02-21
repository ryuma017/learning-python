import sqlite3
import socket
import datetime

# socketでの接続設定
s = socket.socket()
host = socket.gethostname()
print(host)
port = 1234
s.bind((host, port))

s.listen(5)

# DBとtableの作成
dbname = input("DB名を入力: ")
conn = sqlite3.connect(dbname+".db")
tablename = "accesslist"
cur = conn.cursor()

query = "CREATE TABLE " + tablename + "(id INTEGER PRIMARY KEY, address STRING, time STRING)"
cur.execute(query)

conn.commit()
conn.close()

id = 1

# クライアントからの接続待ち状態へ移行
while True:
    c, addr = s.accept()
    # クライアントから接続があった場合以下を実行
    conn = sqlite3.connect(dbname + ".db")
    cur = conn.cursor()
    nowtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    query = f"INSERT INTO {tablename} (id, address, time) values({id}, '{addr[0]}', '{nowtime}')"
    cur.execute(query)
    print("接続受付:", addr)
    c.send(bytes(f"接続ありがとうございます。現在時刻は{nowtime}です", "utf-8"))
    id += 1
    c.close
    conn.commit()
    conn.close()