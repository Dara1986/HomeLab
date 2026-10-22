from pydantic import BaseModel
from typing import Optional

class Service_data(BaseModel):
    container_vmid : int
    service_name : str
    id : Optional[int] = None