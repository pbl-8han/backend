import sqlite3

"""
・インスタンス作成
 インスタンス名=database()

・データ登録, 引数説明
 インスタンス名.create(人数, "西暦", "月", "日付", "時間", 曜日id, 天気id)

・データ読み出し
 インスタンス名.read()

・データ削除, 引数説明
 インスタンス名.delete(id)
"""

class database:
#初期化
    def __init__(self):
        #データベース接続
        dbname='database.db'
        conn=sqlite3.connect(dbname)
        cur=conn.cursor()

        #曜日と天気のテーブルがあれば削除
        sql='DROP TABLE IF EXISTS dow'
        cur.execute(sql)

        sql='DROP TABLE IF EXISTS weather'
        cur.execute(sql)

        # テーブル作成
        sql=f"""CREATE TABLE IF NOT EXISTS statistics(
            id INTEGER NOT NULL PRIMARY KEY,
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
            id INTEGER NOT NULL PRIMARY KEY,
            name TXT
            )"""
        cur.execute(sql)

        sql=f"""CREATE TABLE weather(
            id INTEGER NOT NULL PRIMARY KEY,
            name TXT
            )"""
        cur.execute(sql)

        #データ追加
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

        #コミット
        conn.commit()

        #曜日と天気データ読みだし
        sql='SELECT *FROM dow'
        for row in cur.execute(sql):
            print(row)
        print("\n")

        sql='SELECT *FROM weather'
        for row in cur.execute(sql):
            print(row)
        print("\n")

        #データベース切断
        cur.close()
        conn.close()

#データ登録
    def create(self, count, year, month, date, time, dow_id, weather_id):
        #データベース接続
        dbname='database.db'
        conn=sqlite3.connect(dbname)
        cur=conn.cursor()

        #データ追加
        sql=f"""INSERT INTO statistics(count, year, month, date, time, dow_id, weather_id)
        VALUES(?,?,?,?,?,?,?)"""
        cur.execute(sql, [count, year, month, date, time, dow_id, weather_id])

        #コミット
        conn.commit()

        #データベース切断
        cur.close()
        conn.close()

#データ読み出し
    def read(self):
        #データベース接続
        dbname='database.db'
        conn=sqlite3.connect(dbname)
        cur=conn.cursor()

        #データの取得と表示
        print("id, 人数, year, month, date, time, 曜日, 天気\n")
        sql=f"""SELECT statistics.id, statistics.count, statistics.year, statistics.month, statistics.date, statistics.time, dow.name, weather.name
            FROM statistics, dow, weather 
            ON statistics.dow_id = dow.id AND statistics.weather_id = weather.id"""
        for row in cur.execute(sql):
            print(row)
        print("\n")

        #データベース切断
        cur.close()
        conn.close()

#データ削除
    def delete(self, id):
        #データベース接続
        dbname='database.db'
        conn=sqlite3.connect(dbname)
        cur=conn.cursor()

        #データ削除
        sql='DELETE FROM statistics WHERE id=?'
        cur.execute(sql, [id])

        #コミット
        conn.commit()

        #データベース切断
        cur.close()
        conn.close()