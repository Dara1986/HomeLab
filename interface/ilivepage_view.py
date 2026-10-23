# region Live page view contract
from abc import ABC, abstractmethod

class Ilivepage_view(ABC):

    @abstractmethod
    def get_all_unit(self):
        pass

    @abstractmethod
    def get_all_vmids(self) -> list:
        pass
    
    @abstractmethod
    def get_unit_by_vmid(self, vmid: int):
        pass

    @abstractmethod
    def get_snaps_by_unit(self, unit_id: int) -> list:
        pass
# endregion
