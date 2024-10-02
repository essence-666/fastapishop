from typing import Annotated
from pydantic import BaseModel, Field

class Item(BaseModel):
    item_name : Annotated[str, Field(max_length=10, min_length=3)]
    description : Annotated[str, Field(max_length=500)] = "none"
    