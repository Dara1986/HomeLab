from Class_EndPoints.py import DataGrabber

class UnitFileManager:
    def __init__(self):
        pass

    def loop_unit_file(self):
        for service in DataGrabber.targetList:
            self.create_unit_file(service)
            self.write_unit_file(service)
            self.push_unit_file(service)

    def create_unit_file(self, service):
            new_unit_file = subprocess.run(["pct", "exec", f"{DataGrabber.getContainerId()}", "--", "touch", f"/etc/systemd/system/{service}.service"])
            self.unit_file_path = f"/etc/systemd/system/{service}.service"
            self.template = f"""
[unit]
Description=Service Monitor for {DataGrabber.getContainerId()} + {DataGrabber.getServiceName()[service]}
[Service]
ExecStart=pct exec {DataGrabber.getContainerId()} {self.unit_file_path}
Restart=on-failure
OnFailure=notify-failure@/n.service
[Install]
"""
    
    def write_unit_file(self, service):
        with open({self.unit_file_path}, "w") as f:
            f.write(self.template)
            
    def push_unit_file(self, service):
        subprocess.run(["pct", "push", f"{DataGrabber.getContainerId()}", f"{self.unit_file_path}", f"{self.unit_file_path}"])