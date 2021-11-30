from fastapi import FastAPI
import database

db=database()
app=FastAPI()

@app.post("/")
async def main(db,people:int=0):
    people=db.read("count")
    return {"people":people}