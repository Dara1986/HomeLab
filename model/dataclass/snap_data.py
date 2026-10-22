from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from serverity import Severity

class Snap_data(BaseModel):
    dienst_id: int
    timestamp: datetime
    active: str
    loaded: str
    pid: int
    mem: str
    cpu: str
    uptime: int
    swap: int
    status: str
    severity: Optional[Severity] = Severity.DEBUG
    id: Optional[int] = None