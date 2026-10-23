# region systemd unit file lifecycle
from factory.dataGrabber import *


class UnitFileManager:
    def __init__(self, grabber: DataGrabber):
        self.grabber = grabber

    def loop_unit_file(self):
        for service in self.grabber.getServiceName():
            self.create_unit_file(service)
            self.write_unit_file(service)
            self.push_unit_file(service)

    def create_unit_file(self, service):
            self.unit_file_path = f"/etc/systemd/system/{service}.service"
            self.template = f"""
[unit]
Description=Service Monitor for {self.grabber.getContainerId()} + {service}
[Service]
ExecStart=pct exec {self.grabber.getContainerId()} {self.unit_file_path}
Restart=on-failure
OnFailure=notify-failure@/%.service
[Install]
WantedBy=multi-user.target
"""
    
    def write_unit_file(self, service):
        with open(self.unit_file_path, "w") as f:
            f.write(self.template)
            
    def push_unit_file(self, service):
        subprocess.run(["pct", "push", f"{self.grabber.getContainerId()}", f"{self.unit_file_path}", f"{self.unit_file_path}"])
    # endregion