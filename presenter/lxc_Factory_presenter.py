from interface.ipresenter import Ipresenter
from model.dataclass.container_data import Container_data
from model.dataclass.snap_data import Snap_data
from model.dataclass.unit_data import Unit_data
from model.repository.container_repo import Container_repo
from model.repository.snap_repo import Snap_repo
from model.repository.unit_repo import Unit_repo
from model.dataclass.serverity import Severity
from view.lxc_Factory_view import Lxc_Factory_view
from datetime import datetime



class Lxc_Factory_Presenter(Ipresenter):
    def __init__(self, container_repo: Container_repo, snap_repo: Snap_repo, unit_repo: Unit_repo, view: Lxc_Factory_view):
        self.container_repo = container_repo
        self.snap_repo = snap_repo
        self.unit_repo = unit_repo
        self.view = Lxc_Factory_view

    def get_all_vmids(self) -> list:
        return []
    
    def get_all_unit(self) -> list:
        return []

    def get_unit_by_vmid(self, vmid: int) -> list:
        return []

    def get_snaps_by_unit(self, unit_id: int) -> list:
        return []

    def get_units(self) -> list:
        return []

    def get_snaps_by_filter(
        self,
        unit_id: int,
        start_time: datetime,
        end_time: datetime,
        serverity: Severity,
    ) -> list:
        return []

    def get_serverity(self) -> list:
        return []

    def download_log(self, path: str, snaps: list):
        return None

    def get_db_status(self) -> bool:
        return False