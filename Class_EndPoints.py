# region imports
import json
from datetime import datetime as dt
import subprocess
import requests
from fastapi import FastAPI
from pydantic import BaseModel
from models.py import *
from abc import ABC
# endregion
app = FastAPI


# Factory:

class MonitoringFactory():
    def __init__(self, vmid:int, targetList:list=None, target:object=None):
        self.vmid = vmid
        self.targetList = targetList
        self.target = id_target

    # Erstelle hier objekte mit den Parametern vmid + targetList
    def createMonitor(self):
        monitors = {}
        for i in range(len(targetList)): 
            id_target = f"{self.vmid}+{self.targetList[i]}"
            monitors[id_target] = MonitoringFactory()       # Erstellung der Objekte nochmals überdenken.
    

class ObjManager(MonitoringFactory, DataGrabber):
    def __init__(self, monitors):
        self.monitors = monitors
        

    @app.post("/{container}/{service}/{name}")
    def Pullnotification(EndPoints):
        requests.post("http://192.168.0.254:2586/pve_alerts",
        data=data.message
        )
        return {
            {"name:", container.service.name}: {"status:", container.service.status},
        }

class DataGrabber():        
    def __init__(self,  vmid:int, containerData:str, ip:str):
        self.vmid = vmid
        self.containerData = conData
        self.ip = ip


    @app.post("/ConData")
    def getContainerData(self):
        self.conData = {}
        user_agent = requests.headers.get(url="localhost:8000")
        if "Linux" in user_agent: 
            self.conData = subprocess.run(
                "pct","status", f"{vmid:int}", "--verbose", capture_output=True)
            return self.conData.capture_output()
        else:
            return {"conData" : "no Data"}
            
            

            
            
        




        