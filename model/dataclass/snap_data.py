from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from model.dataclass.serverity import Severity

class Snap_data(BaseModel):
    unit_id: int
    timestamp: datetime
    active: str
    loaded: str
    pid: int
    mem: str
    cpu: str
    uptime: int
    swap: int
    status: str
    severity: Severity = Severity.DEBUG
    id: Optional[int] = None