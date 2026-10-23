# region Database schema creation
import sqlite3
from pathlib import Path



class Create_database:
    def __init__(self,  s3: sqlite3.Connection, path: Path = Path(__file__).parent / "lxc_factory.db"):
        self.s3 = s3
        self.path = path

def create_database(self):
    con = self.s3.connect(self.path)
    con.execute("PRAGMA foreign_keys = ON")
    con.execute("""
    CREATE TABLE IF NOT EXISTS containers (
        vmid INT PRIMARY KEY,
        name TEXT,
        cpus INTEGER,
        maxdisk INT,
        maxmem INT,
        maxswap INT
    )
""")

    con.execute("""
    CREATE TABLE IF NOT EXISTS units (
        id INT PRIMARY KEY,
        container_vmid INT,
        unit_name TEXT,
        FOREIGN KEY (container_vmid) REFERENCES containers(vmid)
    )
""")

    con.execute("""
    CREATE TABLE IF NOT EXISTS snapshots (
        id INT PRIMARY KEY,
        units_id INT,
        timestamp TEXT,
        active TEXT,
        loaded TEXT,
        pid INT,
        mem TEXT,
        cpu TEXT,
        uptime INT,
        swap INT,
        status TEXT,
        severity TEXT DEFAULT 'DEBUG',
        FOREIGN KEY (units_id) REFERENCES units(id)
    )
""")
    con.commit()

    return con, self.path
# endregion