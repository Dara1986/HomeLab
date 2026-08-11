# region imports
import json
from datetime import datetime as dt
import subprocess
import requests
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
# endregion 




class ContainerStatus(BaseModel):
    # pct status --verbose
    cpus: int
    disk: int
    diskread: int
    diskwrite: int
    maxdisk: int
    maxmem: int
    maxswap: int
    mem: int
    name: str
    netin: int
    netout: int
    pid: int
    status: str
    swap: int
    tags: Optional[str] = None
    type: str
    uptime: int
    vmid: int
    
    # systemctl status
    service_name: str
    loaded: str
    active: str
    process: Optional[str] = None
    main_pid: int
    tasks: int
    memory: str
    cpu: str
    cgroup: str
    
    severity: Optional[str] = None

    Severity:Enum = {
        "0" : "[INFO]",
        "1" : "[OK]",
        "2" : "[WARNING]",
        "3" : "[CRITICAL]",
    }
