import sqlite3 as s3
from pathlib import Path

path = Path(__file__).parent / "lxc_factory.db"


def create_database():
    con = s3.connect(path)
    con.execute("PRAGMA foreign_keys = ON")
    con.execute("""
    CREATE TABLE IF NOT EXISTS containers (
        vmid INTEGER PRIMARY KEY,
        name TEXT,
        cpus INTEGER,
        maxdisk INTEGER,
        maxmem INTEGER,
        maxswap INTEGER
    )
""")

    con.execute("""
    CREATE TABLE IF NOT EXISTS units (
        id INTEGER PRIMARY KEY,
        container_vmid INTEGER,
        unit_name TEXT,
        FOREIGN KEY (container_vmid) REFERENCES containers(vmid)
    )
""")

    con.execute("""
    CREATE TABLE IF NOT EXISTS snapshots (
        id INTEGER PRIMARY KEY,
        unit_id INTEGER,
        timestamp TEXT,
        active TEXT,
        loaded TEXT,
        pid INTEGER,
        mem TEXT,
        cpu TEXT,
        uptime INTEGER,
        swap INTEGER,
        status TEXT,
        severity TEXT DEFAULT 'DEBUG',
        FOREIGN KEY (units_id) REFERENCES units(id)
    )
""")
    con.commit()

create_database()