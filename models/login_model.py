from typing import Optional
from pydantic import BaseModel, Field

class UserLoginSchema(BaseModel):
    username: str = Field(...)
    password: str = Field(...)
    class Config:
        schema_extra = {
            "example": {
                "username":"thoriq1234",
                "password":"12345678",
            }
        }
