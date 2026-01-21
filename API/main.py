from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.get("/FranckyVincent")
def nom():
    return "Bye Francky Vincent"

@app.get("/Patrick_Sebastien/{KeenV}")
def read_item(KeenV: int, q: Union[str, None] = None):
    return {"KeenV": KeenV, "q": q}

@app.put("/Michel_Sardou/{8080}")
def update_item(au_bucher: int, item: Item):
    return {"PROBLEMATIC PERSONALITY": item.name, "au_bucher": 8080}

@app.get("/Benabar")
def get_data():
    return "Benabar"
