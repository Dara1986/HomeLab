import json
from datetime import datetime as dt
import subprocess
import requests
from fastapi import FastAPI

app = FastAPI()


@app.post("/pull")
def git_pull():        
    subprocess.run(["git", "-C", "/opt/homelab", "pull"])
    return {"status": "ok"}


# Dies ist zum Testen
a = 0
print(a)




   
    
"""
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

"""