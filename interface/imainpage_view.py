from abc import ABC, abstractmethod

class Imainpage_view(ABC):

    @abstractmethod
    def get_db_status(self)-> bool:
        pass
