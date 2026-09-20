import platform
import subprocess


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


def close_application(application: str) -> str:
    name = application.lower().strip()

    try:
        result = subprocess.run(
            ["taskkill", "/IM", f"{name}.exe", "/F"],
            capture_output=True,
            text=True,
        )

        if result.returncode == 0:
            return f"Closed {application}."

        return f"Could not close {application}: {result.stderr.strip()}"

    except Exception as e:
        return f"Failed to close {application}: {e}"