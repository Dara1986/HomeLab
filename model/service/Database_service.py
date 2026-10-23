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

    

