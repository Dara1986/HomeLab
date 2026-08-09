import json
from datetime import date
from datetime import datetime as dt

import requests
from fastapi import FastAPI

app = FastAPI()


# Pihole Warnung

requests.post(
    timeNow = dt.now().strftime("%d.%m.%y %H:%M")
    "localhost:8000/ph_Grav",
    json={
        "status": "warning(yellow)",
        "daemon": "pihole",
        "timestamp": timeNow,
        "suggestion": "Updating manually in console or via SSH. Probably attaching a API for it",
    },
)

