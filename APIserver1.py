from fastapi import FastAPI

from database import database

#インスタンス宣言
db=database()
app=FastAPI()

@app.get("/")

async def main():

    #databaseからデータ抽出
    dict_list=db.read()

    #人数を格納
    people=dict_list[0]["count"]

    #json形式で返す
    return {"people":people}