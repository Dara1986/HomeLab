from sqlite3 import Connection as s3
from dataclass.container_data import Container_data

class Container_Repo:
    def __init__(self, container_data: Container_data, s3: s3):
        """
        Purpose: value
        """
        self.__s3 = s3
        self.container_data = container_data

    def add(self, container_data: Container_data):
        #cur = self.__s3.execute(
            """
            INSERT INTO 
            """


