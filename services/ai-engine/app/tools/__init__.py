

from app.tools.time import (
    get_current_time,
    get_current_date,
)

from app.tools.apps import (
    open_application,
)

from app.tools.browser import (
    open_website,
)

from app.tools.files import (
    list_directory,
    read_file,
    create_file,
)

from app.tools.system import (
    get_system_info,
)


TOOLS = {
    "get_current_time": get_current_time,
    "get_current_date": get_current_date,
    "open_application": open_application,
    "open_website": open_website,
    "list_directory": list_directory,
    "read_file": read_file,
    "create_file": create_file,
    "get_system_info": get_system_info,
}