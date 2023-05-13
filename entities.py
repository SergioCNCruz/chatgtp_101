from typing import Dict, List

from pydantic import BaseModel


class RequestMessage(BaseModel):
    role: str
    content: str


class RequestPayload(BaseModel):
    model: str
    messages: List[RequestMessage]


class ResponseMessage(BaseModel):
    role: str
    content: str


class ResponseChoice(BaseModel):
    message: ResponseMessage
    finish_reason: str
    index: int


class ResponseData(BaseModel):
    id: str
    object: str
    created: str
    model: str
    usage: Dict
    choices: List[ResponseChoice]
