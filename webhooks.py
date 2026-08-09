import json
from datetime import datetime as dt
import subprocess
import requests
from fastapi import FastAPI

app = FastAPI()


@app.post("/pull")
def git_pull():
    subprocess.run(["git", "-C", "/opt/homelab", "pull"])
    subprocess.run(["systemctl", "restart", "fastapi_server.service"])
    return {"status": "ok"}

# Testnachricht auf ntfy

@app.post("/test")
def test_message():
    requests.post(
        "http://192.168.0.254:2586/pve_alerts",
        json={
            "Nachricht": "Dies ist eine Testnachricht",
        },
    )
    return {"status": "ok"}


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
