import sqlite3
from dataclass.unit_data import Unit_data

class Unit_repo:
    def __init__(self, con: sqlite3.Connection):
        self.__con = con

    def add_unit(self, uData: Unit_data) -> Unit_data:
        cur = self.__con.execute(
            """
            INSERT INTO units (container_vmid, unit_name)
            VALUES (?, ?)
            """,
            (uData.container_vmid, uData.unit_name)
        )
        self.__con.commit()
        uData.id = cur.lastrowid or 0
        return uData

    def get_unit_by_id(self, id: int) -> Unit_data:
        cur = self.__con.execute(
            "SELECT * FROM units WHERE id = ?;", (id,)
        )
        return cur.fetchone()

    def get_units_by_vmid(self, vmid: int) -> list[Unit_data]:
        cur = self.__con.execute(
            "SELECT * FROM units WHERE container_vmid = ?;", (vmid,)
        )
        return cur.fetchall()

    def get_all_units(self) -> list[Unit_data]:
        cur = self.__con.execute("SELECT * FROM units;")
        return cur.fetchall()

    def update_unit(self, uData: Unit_data) -> int:
        cur = self.__con.execute(
            """
            UPDATE units
            SET container_vmid = ?, unit_name = ?
            WHERE id = ?
            """,
            (uData.container_vmid, uData.unit_name, uData.id)
        )
        self.__con.commit()
        return cur.rowcount

    def delete_unit(self, id: int) -> int:
        cur = self.__con.execute(
            "DELETE FROM units WHERE id = ?;", (id,)
        )
        self.__con.commit()
        return cur.rowcount