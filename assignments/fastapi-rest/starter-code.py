from typing import Dict, List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    price: float = Field(gt=0)

_db: Dict[int, Item] = {}

@app.get("/health")
def health() -> Dict[str, str]:
    return {"status": "ok"}

@app.post("/items", status_code=201)
def create_item(item: Item) -> Item:
    if item.id in _db:
        raise HTTPException(status_code=400, detail="Item id already exists")
    _db[item.id] = item
    return item

@app.get("/items")
def list_items() -> List[Item]:
    return list(_db.values())

@app.get("/items/{item_id}")
def get_item(item_id: int) -> Item:
    if item_id not in _db:
        raise HTTPException(status_code=404, detail="Item not found")
    return _db[item_id]

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item) -> Item:
    if item_id not in _db:
        raise HTTPException(status_code=404, detail="Item not found")
    if item.id != item_id:
        raise HTTPException(status_code=400, detail="Payload id mismatch")
    _db[item_id] = item
    return item

@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int) -> None:
    if item_id not in _db:
        raise HTTPException(status_code=404, detail="Item not found")
    del _db[item_id]
    return None

# Run: uvicorn starter-code:app --reload
