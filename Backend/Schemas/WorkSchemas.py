from pydantic import BaseModel, Field, ConfigDict
from pydantic import EmailStr

class GetWork(BaseModel):
    id: int
    title: str
    genre: str
    openopus_id: int
    composer_id: int

    model_config = ConfigDict(from_attributes=True)

class WorkSearchedDB(BaseModel):
    work: GetWork
    rating: int | None
    matched_by: str

class WorkSearchDB(BaseModel):
    works: list[WorkSearchedDB]

class WorkSearchedOpenOpus(BaseModel):
    works: list[GetWork]