from typing import Annotated
from sqlalchemy import DateTime
from pydantic import UUID4, BaseModel, Field


class BaseSchema(BaseModel):
    class Config:
        extra = 'forbid'
        from_attributes= True

#TODO
class OutMixin(BaseModel):
    id: Annotated(UUID4, Field(description='Identificador'))
    create_at: DateTime