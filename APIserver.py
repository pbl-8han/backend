from fastapi import FastAPI
import database

app=FastAPI()

@app.post("/")
async def main(count:int=0):
    count=get.count()
    return {"count":count}
