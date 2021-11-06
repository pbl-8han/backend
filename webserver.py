from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import time
import schedule

app=FastAPI()

while True:
    @app.get("/{file}",response_class=HTMLResponse)
    async def main(file):
        if file==None:
            return "file is nothing"
        ll=open(file,"r")
        mm=open("index.html","w")
        mm.writelines(ll.read())
        ll.close()
        mm.close()
        mm=open("index.html","r")
        #htmlファイルをwebブラウザで表示
        mm.close()



