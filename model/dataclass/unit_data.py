# region Unit data model
from pydantic import BaseModel
from typing import Optional

class Unit_data(BaseModel):
    container_vmid : int
    unit_name : str
    id : Optional[int] = None
# endregion