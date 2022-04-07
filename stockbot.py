from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "stockbot"}
@app.get("/about")
def about():
    return {"Data":"about"}

inventory = {
    1: {"stock name": "Tesla",
        "price": 1,
        }
    }

@app.get("/get-item/{item-id}/{name}")
def get_item(item_id:int, name : "str"):
    return inventory[item_id].update

