# region Container and service data collection
# region Imports
import subprocess
# endregion

class DataGrabber():        
    def __init__(self, vmid_list:list, vmid:int, conData:str, targetList:list, target:str, status: str):
        self.vmid_list = vmid_list
        self.vmid = vmid
        self.conData = conData
        self.targetList = targetList
        self.target = target
        self.status = status

    def getContainerId(self) ->list:
        self.vmid_list = subprocess.run(["pct", "list"], capture_output=True).stdout.decode("utf-8").splitlines()[1:]
        self.vmid = [line.split(None)[0] for line in self.vmid_list]
        return self.vmid
        
    def getContainerData(self) -> str:
        self.conData = subprocess.run(
            ["pct", "status", str(self.vmid), "--verbose"], capture_output=True
        ).stdout.decode("utf-8")
        return self.conData

    def getServiceName(self) ->list[str]:
        self.target = subprocess.run(
            ["pct","exec", str(self.vmid), "--", "systemctl","list-units", "--type=service", "--state=active",],
            capture_output=True,
        ).stdout.decode("utf-8").splitlines()[1:]
        self.targetList = [service.split(None)[0] for service in self.target]
        return self.targetList
        
    def getServiceStatus(self):
        pass
# endregion