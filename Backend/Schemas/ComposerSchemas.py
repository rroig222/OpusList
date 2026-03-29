from pydantic import BaseModel, ConfigDict


class GetComposer(BaseModel):
    id: int
    openopus_id: int
    name: str
    complete_name: str
    epoch: str

    model_config = ConfigDict(from_attributes=True)