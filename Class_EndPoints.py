# region imports
import json
from datetime import datetime as dt
import subprocess
import requests
from fastapi import FastAPI
from pydantic import BaseModel
from models.py import *
#from abc import ABC
app = FastAPI
# endregion

"""
    @app.post("/{container}/{service}/{name}")
    def Pullnotification(EndPoints):
        requests.post("http://192.168.0.254:2586/pve_alerts",
        data=data.message
        )
        return {
            {"name:", container.service.name}: {"status:", container.service.status},
        }
"""

class MonitoringFactory():
    def __init__(self, vmid:int, targetList:list=None, target:object=None):
        self.vmid = vmid
        self.targetList = targetList
        self.target = target

    # Erstelle hier objekte mit den Parametern vmid + targetList
    def createMonitor(self):
        monitors = {}
        for i in range(len(targetList)): 
            target = f"{self.vmid}+{self.targetList[i]}"
            monitors[target] = MonitoringFactory()       # Erstellung der Objekte nochmals überdenken.
    
class DataGrabber():        
    def __init__(self, vmid_list:list, vmid:int, conData:str, targetList:list=None, target:str=None):
        self.vmid_list = vmid_list
        self.vmid = vmid
        self.conData = conData
        self.targetList = targetList
        self.target = target

    def getContainerId(self):
        self.vmid_list = subprocess.run("pct", "list", capture_output=True).stdout.decode("utf-8").splitlines()[1:]
        self.vmid = [line.split(None)[0] for line in self.vmid_list]
        return self.vmid
        
    def getContainerData(self):
        self.conData = subprocess.run(
            "pct","status", f"{self.vmid}", "--verbose", capture_output=True).stdout.decode("utf-8")
        return self.conData

    def getServiceName(self):
        self.target = subprocess.run("pct", "exec", f"{self.vmid}","--","systemctl","list-units","--type=service",
        "--state=active", capture_output=True).stdout.decode("utf-8").splitlines()[1:]
        self.targetList = [service.split(None)[0] for service in self.target]
        return self.targetList
        
    def getServiceStatus(self):
        pass
    
#region Beispielausgabe 1
        """
        Beispielausgabe: 

        root@pve:~# pct exec 203 -- systemctl list-units --type=service --state=active
        UNIT                               LOAD   ACTIVE SUB     DESCRIPTION                                    
        console-getty.service              loaded active running Console Getty
        container-getty@1.service          loaded active running Container Getty on /dev/tty1
        container-getty@2.service          loaded active running Container Getty on /dev/tty2
        cron.service                       loaded active running Regular background program processing daemon
        dbus.service                       loaded active running D-Bus System Message Bus
        ifupdown-pre.service               loaded active exited  Helper to synchronize boot up for ifupdown
        ifupdown-wait-online.service       loaded active exited  Wait for network to be configured by ifupdown
        networking.service                 loaded active exited  Raise network interfaces
        nftables.service                   loaded active exited  nftables
        pihole-FTL.service                 loaded active running Pi-hole FTL
        postfix.service                    loaded active exited  Postfix Mail Transport Agent
        postfix@-.service                  loaded active running Postfix Mail Transport Agent (instance -)
        ssh.service                        loaded active running OpenBSD Secure Shell server
        systemd-journal-flush.service      loaded active exited  Flush Journal to Persistent Storage
        systemd-journald.service           loaded active running Journal Service
        systemd-logind.service             loaded active running User Login Management
        systemd-modules-load.service       loaded active exited  Load Kernel Modules
        systemd-network-generator.service  loaded active exited  Generate network units from Kernel command line
        systemd-networkd.service           loaded active running Network Configuration
        systemd-remount-fs.service         loaded active exited  Remount Root and Kernel File Systems
        systemd-sysctl.service             loaded active exited  Apply Kernel Variables
        systemd-sysusers.service           loaded active exited  Create System Users
        systemd-tmpfiles-setup-dev.service loaded active exited  Create Static Device Nodes in /dev
        systemd-tmpfiles-setup.service     loaded active exited  Create System Files and Directories
        systemd-update-utmp.service        loaded active exited  Record System Boot/Shutdown in UTMP
        systemd-user-sessions.service      loaded active exited  Permit User Sessions
        """
#endregion
#region Beispielausgabe 2
        """ 
        root@pve:~# pct exec 203 -- systemctl status console-getty.service
● console-getty.service - Console Getty
     Loaded: loaded (/lib/systemd/system/console-getty.service; enabled-runtime; preset: disabled)
     Active: active (running) since Tue 2026-08-18 15:31:04 UTC; 2 days ago
       Docs: man:agetty(8)
             man:systemd-getty-generator(8)
   Main PID: 174 (agetty)
      Tasks: 1 (limit: 17832)
     Memory: 264.0K
        CPU: 1ms
     CGroup: /system.slice/console-getty.service
             └─174 /sbin/agetty -o "-p -- \\u" --noclear --keep-baud - 115200,38400,9600 linux

Aug 18 15:31:04 pihole systemd[1]: Started console-getty.service - Console Getty.
root@pve:~# pct exec 203 -- systemctl status container-getty@1.service
● container-getty@1.service - Container Getty on /dev/tty1
     Loaded: loaded (/lib/systemd/system/container-getty@.service; enabled; preset: enabled)
     Active: active (running) since Tue 2026-08-18 15:31:04 UTC; 2 days ago
       Docs: man:agetty(8)
             man:systemd-getty-generator(8)
             man:machinectl(1)
   Main PID: 175 (agetty)
      Tasks: 1 (limit: 17832)
     Memory: 204.0K
        CPU: 1ms
     CGroup: /system.slice/system-container\x2dgetty.slice/container-getty@1.service
             └─175 /sbin/agetty -o "-p -- \\u" --noclear - linux
        """
#endregion 
   