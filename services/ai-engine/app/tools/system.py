

import platform


def get_system_info() -> str:

    return (
        f"Operating system: {platform.system()} "
        f"{platform.release()}\n"
        f"Machine: {platform.machine()}\n"
        f"Processor: {platform.processor()}"
    )


def get_running_applications() -> str:
    try:
        result = subprocess.run(
            ["tasklist"],
            capture_output=True,
            text=True,
            check=True,
        )

        return result.stdout

    except Exception as e:
        return f"Failed to get running applications: {e}"