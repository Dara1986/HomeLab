from interface.iview import IView
from datetime import datetime
from model.dataclass.serverity import Severity

class Lxc_Factory_view(IView):
    def get_db_status(self) -> bool:
        raise NotImplementedError

    def get_units(self) -> list:
        raise NotImplementedError

    def get_snaps_by_filter(
        self,
        unit_id: int,
        start_time: datetime,
        end_time: datetime,
        serverity: Severity,
    ) -> list:
        raise NotImplementedError

    def get_serverity(self) -> list:
        raise NotImplementedError

    def download_log(self, path: str, snaps: list):
        raise NotImplementedError

    def get_all_unit(self):
        raise NotImplementedError

    def get_all_vmids(self) -> list:
        raise NotImplementedError

    def get_unit_by_vmid(self, vmid: int):
        raise NotImplementedError

    def get_snaps_by_unit(self, unit_id: int) -> list:
        raise NotImplementedError