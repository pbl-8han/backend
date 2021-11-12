import sqlite3
#データベース接続
dbname='statistics.db'
conn=sqlite3.connect(dbname)
cur=conn.cursor()

#テーブルがあれば削除
sql='DROP TABLE IF EXISTS statistics'
cur.execute(sql)
sql='DROP TABLE IF EXISTS dow'
cur.execute(sql)
sql='DROP TABLE IF EXISTS weather'
cur.execute(sql)

# テーブル作成
sql=f"""CREATE TABLE statistics(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    count INTEGER,
    year TXT,
    month TXT,
    date TXT,
    time TXT,
    dow_id INTEGER,
    weather_id INTEGER
    )"""
cur.execute(sql)

sql=f"""CREATE TABLE dow(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name TXT
    )"""
cur.execute(sql)

sql=f"""CREATE TABLE weather(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name TXT
    )"""
cur.execute(sql)

#データ追加(仮)
sql='INSERT INTO dow(id, name) VALUES(?,?)'
data=[
    (1, "日曜日"),
    (2, "月曜日"),
    (3, "火曜日"),
    (4, "水曜日"),
    (5, "木曜日"),
    (6, "金曜日"),
    (7, "土曜日")
]
cur.executemany(sql, data)

sql='INSERT INTO weather(id, name) VALUES(?,?)'
data=[
    (1, "晴れ"),
    (2, "曇り"),
    (3, "雨")
]
cur.executemany(sql, data)

sql=f"""INSERT INTO statistics(count, year, month, date, time, dow_id, weather_id)
    VALUES(30, "2021", "11", "12", "11:58", 6, 1)"""
cur.execute(sql)

#コミット
conn.commit()

#データの取得と表示
sql='SELECT *FROM dow'
for row in cur.execute(sql):
    print(row)
print("\n")

sql='SELECT *FROM weather'
for row in cur.execute(sql):
    print(row)
print("\n")

sql=f"""SELECT statistics.id, statistics.count, statistics.year, statistics.month, statistics.date, statistics.time, dow.name, weather.name
    FROM statistics, dow, weather 
    ON statistics.dow_id = dow.id AND statistics.weather_id = weather.id"""
for row in cur.execute(sql):
    print(row)
print("\n")

#データベース切断
cur.close()
conn.close()