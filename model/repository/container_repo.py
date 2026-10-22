import sqlite3
from dataclass.container_data import Container_data

class Container_Repo:
    def __init__(self, con: sqlite3.Connection):
        self.__con = con

    def add_container(self, cData: Container_data) -> Container_data:
        self.__con.execute(
            """
            INSERT INTO containers (vmid, name, cpus, maxdisk, maxmem, maxswap)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (cData.vmid, cData.name, cData.cpus,
             cData.maxdisk, cData.maxmem, cData.maxswap)
        )
        self.__con.commit()
        return cData

    def get_container_by_vmid(self, vmid: int) -> Container_data:
        cur = self.__con.execute(
            "SELECT * FROM containers WHERE vmid = ?;", (vmid,)
        )
        return cur.fetchone()

    def get_all_containers(self) -> list[Container_data]:
        cur = self.__con.execute("SELECT * FROM containers;")
        return cur.fetchall()

    def update_container(self, cData: Container_data) -> int:
        cur = self.__con.execute(
            """
            UPDATE containers
            SET name = ?, cpus = ?, maxdisk = ?, maxmem = ?, maxswap = ?
            WHERE vmid = ?
            """,
            (cData.name, cData.cpus, cData.maxdisk,
             cData.maxmem, cData.maxswap, cData.vmid)
        )
        self.__con.commit()
        return cur.rowcount

    def delete_container(self, vmid: int) -> int:
        cur = self.__con.execute(
            "DELETE FROM containers WHERE vmid = ?;", (vmid,)
        )
        self.__con.commit()
        return cur.rowcount