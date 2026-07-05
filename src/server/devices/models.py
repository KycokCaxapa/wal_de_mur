from dataclasses import dataclass
from datetime import datetime


@dataclass
class Device:
    id: int
    ip: str
    user_agent: str
    name: str
    connected_at: datetime
