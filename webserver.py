from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import time
import schedule

app=FastAPI()

while True:
    schedule.run_pending()
    time.sleep(60)
    @app.get("/{file}",response_class=HTMLResponse)
    async def main(file):
        if file==None:
            return "file is nothing"
        return {file}

