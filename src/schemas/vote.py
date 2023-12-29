from pydantic import BaseModel, ValidationError, validator
from typing import Optional, List, Union
from datetime import datetime


class vote_schema(BaseModel):
    id: Optional[int]
    name: str
    description: str
    activity_date: Union[datetime, None]
    end_time: datetime
    server_id: str
    create_time: Optional[datetime]

    @validator('name')
    def name_rules(cls, v, values, **kwargs):
        if len(v) > 20:
            raise ValueError('vote name too long')
        return v

    @validator('description')
    def description_rules(cls, v, values, **kwargs):
        if len(v) > 50:
            raise ValueError('vote description too long')
        return v

    @validator('server_id')
    def server_id_rules(cls, v, values, **kwargs):
        if len(v) > 18:
            raise ValueError('vote server_id too long')
        return v


class option_schema(BaseModel):
    id: Optional[int]
    name: str
    v_id: Optional[int]

    @validator('name')
    def option_rules(cls, v, values, **kwargs):
        if len(v) > 10:
            raise ValueError('option name too long')
        return v


class voter_schema(BaseModel):
    id: Optional[int]
    name: str
    o_id: Optional[int]

    @validator('name')
    def voter_rules(cls, v, values, **kwargs):
        if len(v) > 18:
            raise ValueError('voter name too long')
        return v


class vote_create_body_schema(BaseModel):
    vote: vote_schema
    vote_options: Optional[List[Union[option_schema, None]]]
