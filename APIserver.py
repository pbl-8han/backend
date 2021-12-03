from fastapi import FastAPI

import database

#インスタンス宣言
db=database()
app=FastAPI()

@app.post("/")

async def main(db,people:int=0):

    #databaseから人数を抽出
    people=db.read("count")

    #json形式で返す
    return {"people":people}