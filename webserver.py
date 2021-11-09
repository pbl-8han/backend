from typing import Optional
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

class Item(BaseModel):
    name:str
    description:Optional[str]=None
    price:float
    tax:Optional[float]=None

app=FastAPI()

@app.post("/",response_class=HTMLResponse)
async def main(item:Item):
        return """
        <html>
            <head>
                <title>item.name</title>
            </head>
            <body>
                <h1>item.price<h1>
            </body>
        </html>
        """