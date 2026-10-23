from abc import ABC, abstractmethod
from datetime import datetime
from model.dataclass.serverity import Severity

class Ilogpage_view(ABC):

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
