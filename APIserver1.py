from fastapi import FastAPI

from database import database

#インスタンス宣言
db=database()
app=FastAPI()

@app.get("/")

async def main():

    #databaseから人数を抽出
    people=db.read()

    #json形式で返す
    return {"people":people}