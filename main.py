from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    app_name: str
    source: str
    moe_request_id: str
    events: list

app = FastAPI()

@app.get('/')
def find_users ():
    users = "YUHU"
    return users

@app.post("/items/")
async def create_item(item: Item):
    #print("i : " ,item)
    return item
