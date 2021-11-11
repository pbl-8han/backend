from typing import Optional
import datetime as dt
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

#JSONの属性
class Item(BaseModel):
    dt_now:str=dt.datetime.now()
    people:int=0
    dayofweek:Optional[str]=None
    weather:str

#確認用の曜日・天気
dayofweek=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
weather=["sunny","cloudy","raining","raining with thunder","snowing"]

#確認用フラグ
frag1=0
frag2=0
app=FastAPI()

@app.post("/")
async def main(item:Item):

    #曜日の識別
    for DOW in dayofweek:
        if item.dayofweek==DOW:
            frag1=1

    #例外処理
    if frag1==0:
        raise HTTPException(status_code=404,detail="exception input")

    #天気の識別
    for WEA in weather:
        if item.weather==WEA:
            frag2=1

    #例外処理
    if frag2==0:
        raise HTTPException(status_code=404,detail="exception input")

    #JSON返答
    return item