# region Snapshot persistence operations
import sqlite3
from dataclass.snap_data import Snap_data

class Snap_repo:
    def __init__(self, con: sqlite3.Connection):
        self.__con = con

    def add_snap(self, sData: Snap_data) -> Snap_data:
        cur = self.__con.execute(
            """
            INSERT INTO snapshots 
            (unit_id, timestamp, active, loaded, pid, mem, cpu, uptime, swap, status, severity)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                sData.unit_id, str(sData.timestamp), sData.active,
                sData.loaded, sData.pid, sData.mem, sData.cpu,
                sData.uptime, sData.swap, sData.status, sData.severity.value
            )
        )
        self.__con.commit()
        sData.id = cur.lastrowid or 0
        return sData
    
    def get_snap_by_id(self, id: int) -> Snap_data:
        cur = self.__con.execute(
            "SELECT * FROM snapshots WHERE id = ?;", (id,)
        )
        return cur.fetchone()

    def get_all_snaps(self) -> list[Snap_data]:
        cur = self.__con.execute("SELECT * FROM snapshots;")
        return cur.fetchall()

    def update_snap(self, sData: Snap_data) -> int:
        cur = self.__con.execute(
            """
            UPDATE snapshots
            SET unit_id = ?, timestamp = ?, active = ?, loaded = ?,
                pid = ?, mem = ?, cpu = ?, uptime = ?, swap = ?,
                status = ?, severity = ?
            WHERE id = ?
            """,
            (
                sData.unit_id, str(sData.timestamp), sData.active,
                sData.loaded, sData.pid, sData.mem, sData.cpu,
                sData.uptime, sData.swap, sData.status, sData.severity.value,
                sData.id
            )
        )
        self.__con.commit()
        return cur.rowcount

    def delete_snap(self, id: int) -> int:
        cur = self.__con.execute(
        "DELETE FROM snapshots WHERE id = ?;", (id,)
    )
        self.__con.commit()
        return cur.rowcount
    # endregion