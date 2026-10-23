# region Database service queries and actions
from datetime import datetime
from model.dataclass.serverity import Severity
from repository.container_repo import Container_repo
from repository.unit_repo import Unit_repo
from repository.snap_repo import Snap_repo

class Database_service():
    def __init__(self, container_repo: Container_repo, unit_repo: Unit_repo, snap_repo: Snap_repo):
        self.container_repo = container_repo
        self.snap_repo = snap_repo
        self.unit_repo = unit_repo


    def get_all_vmids(self) -> list:
        containers = self.container_repo.get_all_containers()
        list_vmid = [container.vmid for container in containers]
        return list_vmid
        
        
    def get_all_unit(self) -> list:
        units = self.unit_repo.get_all_units()
        return units
        

    def get_snaps_by_unit(self, unit_id: int) -> list:
        snaps = self.snap_repo.get_all_snaps()
        list_snaps = [snap for snap in snaps if snap.unit_id == unit_id]
        return list_snaps

    def get_snaps_by_filter(self, unit_id: int, start_time: datetime, end_time: datetime, serverity: Severity,) -> list:
        snaps = self.snap_repo.get_all_snaps()
        list_snaps = [
            snap for snap in snaps if snap.unit_id == unit_id 
            and snap.timestamp >= start_time 
            and snap.timestamp <= end_time 
            and snap.severity == serverity
                      ]
        return list_snaps
            
            
    def get_serverity(self) -> list:
        snaps = self.snap_repo.get_all_snaps()
        list_serverity = [snap.severity for snap in snaps]
        return list_serverity
    
    def download_log(self, path: str, snaps: list):
        raise NotImplementedError
        return None

    def get_db_status(self) -> bool:
        connection = self.container_repo.__con
        try:
            connection.execute("SELECT 1")
        except Exception as e:
            raise e
        else:
            return False
# endregion
            

        
            

