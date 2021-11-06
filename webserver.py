from fastapi import FastAPI
import json
import schedule
import time

app=FastAPI()

def server():
    for i in range(0,90):
        @app.put()
        
while True:
    schedule.run_pending()
    time.sleep(60)

