from fastapi import FastAPI
import time
import schedule

app=FastAPI()

while True:
    schedule.run_pending()
    time.sleep(60)
    @app.get("/{file}")
    async def main(file):
        if file==None:
            return "file is nothing"
        return {file}

