from fastapi import FastAPI
import json
import schedule
import time


def server():
    for i in range(0,90):
        @app.put()
        


app=FastAPI()

while True:
    schedule.run_pending()
    time.sleep(60)

