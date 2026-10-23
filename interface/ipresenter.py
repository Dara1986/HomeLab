from abc import ABC, abstractmethod
from iview import *
from datetime import datetime
from model.dataclass.serverity import Severity

class Ipresenter(ABC):
    pass

#region functions from ilivepage_view
    @abstractmethod
    def get_all_unit(self) -> list:
        pass

    @abstractmethod
    def get_all_vmids(self) -> list:
        pass
    
    @abstractmethod
    def get_unit_by_vmid(self, vmid: int) -> list:
        pass

    @abstractmethod
    def get_snaps_by_unit(self, unit_id: int) -> list:
        pass
#endregion

#region functions from ilogspage_view
    @abstractmethod
    def get_units(self) -> list:
        pass

    @abstractmethod        
    def get_snaps_by_filter(self, unit_id: int, start_time: datetime, end_time: datetime, serverity: Severity) -> list:
        pass

    @abstractmethod
    def get_serverity(self) -> list:
        pass

    @abstractmethod
    def download_log(self, path: str, snaps: list):
        pass
#endregion

#region from imainpage_view
    @abstractmethod
    def get_db_status(self)-> bool:
        pass
#endregion