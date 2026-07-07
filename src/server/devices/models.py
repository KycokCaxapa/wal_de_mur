from pydantic import BaseModel
from datetime import datetime


class Device(BaseModel):
    id: int
    ip: str
    name: str
    connected_at: datetime


class LED(Device):
    state: bool
