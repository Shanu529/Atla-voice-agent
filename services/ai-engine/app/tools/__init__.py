

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

from app.tools.web import search_web


from app.tools.files import (
    list_directory,
    create_folder,
    create_file,
    read_file,
    get_special_folder,
    write_file
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
    "search_web": search_web,
    "list_directory": list_directory,
    "create_folder": create_folder,
    "read_file": read_file,
    "get_special_folder": get_special_folder,
    "write_file": write_file,
}