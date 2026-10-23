# region Application startup and dependency wiring
from presenter.lxc_Factory_presenter import Lxc_Factory_Presenter
from database.create_database import Create_database
from model.repository.container_repo import Container_repo
from model.repository.unit_repo import Unit_repo
from model.repository.snap_repo import Snap_repo
from view.lxc_Factory_view import Lxc_Factory_view
from model.service.database_service import Database_service
import sqlite3

# Database connection
con = sqlite3.connect("lxc_factory.db")


if __name__ == "__main__":
    db_obj = Create_database(con)
    unit_obj = Unit_repo(con)
    snap_obj = Snap_repo(con)
    view_obj = Lxc_Factory_view()
    container_obj = Container_repo(con)
    service_obj = Database_service(container_obj, unit_obj, snap_obj)
    presenter_obj = Lxc_Factory_Presenter(service_obj, container_obj, snap_obj, unit_obj, view_obj)
# endregion

    
