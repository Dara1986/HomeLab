# region Combined view contract
from interface.ilivepage_view import Ilivepage_view
from interface.ilogspage_view import Ilogpage_view
from interface.imainpage_view import Imainpage_view

class IView(Imainpage_view, Ilogpage_view, Ilivepage_view):
    pass
# endregion