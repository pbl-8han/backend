import sqlite3 as sql

#データベース接続
dbname='statistics.db'
conn=sql.connect(dbname)
cur=conn.cursor()

# テーブル作成
cur.execute(
    'CREATE TABLE statistics(id int PRIMARY KEY, date str, dow_id int, weather_id int, count int)'
    )
cur.execute(
    'CREATE TABLE day_of_week(id int PRIMARY KEY, name str)'
    )
cur.execute(
    'CREATE TABLE weather(id int PRIMARY KEY, name str)'
    )

#データ追加(仮)
cur.execute('INSERT INTO statistics(id, date, dow_id, weather_id, count) VALUES()')

sql='INSERT INTO day_of_week(id, name) VALUES(?,?)'
data=[
    (1, '日曜日'),
    (2, '月曜日'),
    (3, '火曜日'),
    (4, '水曜日'),
    (5, '木曜日'),
    (6, '金曜日'),
    (7, '土曜日')
]
cur.execute(sql, data)

sql='INSERT INTO weather(id, name) VALUES(?,?)'
data=[
    (1, '晴れ'),
    (2, '曇り'),
    (3, '雨')
]
cur.execute(sql, data)

#コミット
conn.commit()

#データの取得と表示
sql='SELECT *FROM statistics'
for row in cur.execute(sql):
    print(row)

#データベース切断
cur.close()
conn.close()