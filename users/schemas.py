from typing import Annotated
from pydantic import BaseModel, EmailStr, Field

class User(BaseModel):
    username : Annotated[str, Field(max_length=10, min_length=3)]
    email : EmailStr