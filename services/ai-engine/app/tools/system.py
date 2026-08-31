

import platform


def get_system_info() -> str:

    return (
        f"Operating system: {platform.system()} "
        f"{platform.release()}\n"
        f"Machine: {platform.machine()}\n"
        f"Processor: {platform.processor()}"
    )