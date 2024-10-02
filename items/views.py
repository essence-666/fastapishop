from typing import Annotated
from fastapi import APIRouter
from pydantic import Field
from items.schemas import Item
from items import crud

router = APIRouter(prefix="/items", tags=["Items"])


@router.get("/")
def get_items():
    return {
        "items": "all items will be here",
    }


@router.get("/{id}")
def get_item_by_id(id: Annotated[int, Field(ge=0)]):
    return {
        "item": "return an item by id",
    }


@router.post("/")
def create_item(item: Item):
    return crud.create_item(item)
