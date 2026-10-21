class MonitoringFactory():
    def __init__(self, vmid:int, targetList:list, target:object=None):
        self.vmid = vmid
        self.targetList = targetList
        self.target = target

    # Erstelle hier objekte mit den Parametern vmid + targetList
    def createMonitor(self):
        monitors = {}
        for i in range(len(self.targetList)): 
            target = f"{self.vmid}+{self.targetList[i]}"
            monitors[target] = MonitoringFactory(self.vmid, self.targetList)       # Erstellung der Objekte nochmals überdenken.
    