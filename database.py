import sqlite3

"""
・インスタンス作成
 インスタンス名=database()

・テーブル作成
 インスタンス名.create_table()

・データ登録, 引数詳細
 インスタンス名.create(人数 int, 日付 datetime, 曜日ID int, 天気ID int)
   日付 → datetime.datetime.now()
   曜日ID → datetime.datetime.now().weekday()
   天気ID → (0:晴, 1:曇, 2:雨, 3:雪)

・データ読み出し
 インスタンス名.read()
   return [{data}, {data}, ...]

・データ削除, 引数詳細
 インスタンス名.delete(ID int)

・テーブル削除
 インスタンス名.delete_table()
"""

#データベースファイル
dbname='database.db'

class database:
#テーブル作成
    def create_table(self):
        #データベース接続
        conn=sqlite3.connect(dbname)
        cur=conn.cursor()

        # テーブル作成
        sql=f"""CREATE TABLE IF NOT EXISTS statistics(
            id INTEGER NOT NULL PRIMARY KEY,
            count INTEGER,
            date DATETIME,
            dow_id INTEGER,
            weather_id INTEGER
            )"""
        cur.execute(sql)

        sql=f"""CREATE TABLE IF NOT EXISTS dow(
            id INTEGER NOT NULL PRIMARY KEY,
            weekday TXT
            )"""
        cur.execute(sql)

        sql=f"""CREATE TABLE IF NOT EXISTS weather(
            id INTEGER NOT NULL PRIMARY KEY,
            weather TXT
            )"""
        cur.execute(sql)

        #データ追加
        sql='INSERT INTO dow(id, weekday) VALUES(?,?)'
        data=[
            (0, "月曜日"),
            (1, "火曜日"),
            (2, "水曜日"),
            (3, "木曜日"),
            (4, "金曜日"),
            (5, "土曜日"),
            (6, "日曜日")
        ]
        cur.executemany(sql, data)

        sql='INSERT INTO weather(id, weather) VALUES(?,?)'
        data=[
            (0, "晴"),
            (1, "曇"),
            (2, "雨"),
            (3, "雪")
        ]
        cur.executemany(sql, data)

        #コミット
        conn.commit()

        #データベース切断
        cur.close()
        conn.close()

        
#データ登録
    def create(self, count, date, dow_id, weather_id):
        #データベース接続
        conn=sqlite3.connect(dbname)
        cur=conn.cursor()

        #データ追加
        sql='INSERT INTO statistics(count, date, dow_id, weather_id) VALUES(?,?,?,?)'
        cur.execute(sql, [count, date, dow_id, weather_id])

        #コミット
        conn.commit()

        #データベース切断
        cur.close()
        conn.close()

#データ読み出し
    def read(self):
        #辞書型定義
        def dict_factory(cursor, row):
            d={}
            for idx, col in enumerate(cursor.description):
                d[col[0]] = row[idx]
            return d

        #データベース接続
        conn=sqlite3.connect(dbname)

        #row_factory変更
        conn.row_factory = dict_factory

        #カーソル生成
        cur=conn.cursor()

        #データの取得
        sql=f"""SELECT statistics.id, statistics.count, statistics.date, dow.weekday, weather.weather
            FROM statistics, dow, weather 
            ON statistics.dow_id = dow.id AND statistics.weather_id = weather.id"""

        #辞書型のリスト作成
        dict_list=[]
        for row in cur.execute(sql):
            dict_list.append(row)

        #データベース切断
        cur.close()
        conn.close()

        #辞書型のリストをreturn
        return dict_list

#データ削除
    def delete(self, id):
        #データベース接続
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

#テーブル削除
    def delete_table(self):
        #データベース接続
        conn=sqlite3.connect(dbname)
        cur=conn.cursor()

        #テーブル削除
        sql='DROP TABLE IF EXISTS statistics'
        cur.execute(sql)

        sql='DROP TABLE IF EXISTS dow'
        cur.execute(sql)

        sql='DROP TABLE IF EXISTS weather'
        cur.execute(sql)

        #コミット
        conn.commit()

        #データベース切断
        cur.close()
        conn.close()