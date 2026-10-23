# region Container data model
from pydantic import BaseModel

class Container_data(BaseModel):
    vmid: int
    name: str
    cpus: int
    maxdisk: int
    maxmem: int
    maxswap: int
# endregion