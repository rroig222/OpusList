from typing import Optional

from pydantic import BaseModel, Field
from pydantic import EmailStr
from Backend.Schemas.WorkSchemas import GetWork

class GetUser(BaseModel):

    id: int
    username: str
    email: EmailStr

class NewUser(BaseModel):

    username: str = Field(min_length=3)
    email: EmailStr
    password: str = Field(min_length=4)

class LoginUser(BaseModel):

    username: str
    password: str

class RateWork(BaseModel):

    user_id: int
    work_id: int
    rating: int

class UserWorks(GetUser):

    works: list[GetWork]

class RatingResponse(BaseModel):
    rating: Optional[int] = None