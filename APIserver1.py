from fastapi import FastAPI

from database import database

#インスタンス宣言
db=database()
app=FastAPI()

@app.get("/")

async def main():

    #people宣言・初期化
    people=None

    #databaseから人数を抽出
    dict_list=db.read()

    #要素があるなら２番目を格納
    if len(dict_list)!=0:
        people=dict_list[0]["count"]

    #json形式で返す
    return {"people":people}