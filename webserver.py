from typing import Optional
import datetime as dt
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

#JSONの属性
class Info(BaseModel):
    date:str="fixedvariable"
    people:int=0
    dayofweek:Optional[str]="Monday"
    weather:Optional[str]="sunny"

#確認用の曜日・天気
dayofweek=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
weather=["sunny","cloudy","raining","raining with thunder","snowing"]

#確認用フラグ
frag1=0
frag2=0
app=FastAPI()

@app.post("/")
async def main(info:Info):

    #曜日の識別
    for DOW in dayofweek:
        if info.dayofweek.capitalize()==DOW:
            info.dayofweek=info.dayofweek.capitalize()
            frag1=1

    #例外処理
    if frag1==0:
        raise HTTPException(status_code=404,detail="exception input")

    #天気の識別
    for WEA in weather:
        if info.weather.lower()==WEA:
            info.weather=info.weather.lower()
            frag2=1

    #例外処理
    if frag2==0:
        raise HTTPException(status_code=404,detail="exception input")

    #日付と時間を取得
    info.date=dt.datetime.now()
    #info.dayofweek=dt.date(info.date.year,info.date.month,info.date.day)
    #info.dayofweek=info.dayofweek.strftime("%A")

    #JSON返答
    return info
