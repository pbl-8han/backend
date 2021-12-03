import sqlite3

"""
・インスタンス作成
 インスタンス名=database()

 ・テーブル作成
 インスタンス名.createtable()

 ・データ登録, 引数説明
 インスタンス名.create(人数, "西暦", "月", "日付", "時間", 曜日ID, 天気ID)
   曜日ID(1:月曜日, 2:火曜日 3:水曜日, 4:木曜日, 5:金曜日, 6:土曜日, 7:日曜日)
   天気ID(1:晴, 2:曇, 3:雨, 4:雪)

・データ読み出し
 インスタンス名.read()

・データ削除, 引数説明
 インスタンス名.delete(ID)
"""

class database:
#テーブル作成
    def createtable(self):
        #データベース接続
        dbname='database.db'
        conn=sqlite3.connect(dbname)
        cur=conn.cursor()

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

        sql=f"""CREATE TABLE IF NOT EXISTS dow(
            id INTEGER NOT NULL PRIMARY KEY,
            name TXT
            )"""
        cur.execute(sql)

        sql=f"""CREATE TABLE IF NOT EXISTS weather(
            id INTEGER NOT NULL PRIMARY KEY,
            name TXT
            )"""
        cur.execute(sql)

        #データ追加
        sql='INSERT INTO dow(id, name) VALUES(?,?)'
        data=[
            (1, "月曜日"),
            (2, "火曜日"),
            (3, "水曜日"),
            (4, "木曜日"),
            (5, "金曜日"),
            (6, "土曜日"),
            (7, "日曜日")
        ]
        cur.executemany(sql, data)

        sql='INSERT INTO weather(id, name) VALUES(?,?)'
        data=[
            (1, "晴"),
            (2, "曇"),
            (3, "雨"),
            (4, "雪")
        ]
        cur.executemany(sql, data)

        #コミット
        conn.commit()

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
        print("ID, 人数, 西暦, 月, 日付, 時間, 曜日, 天気\n")
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