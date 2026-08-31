import subprocess


APPLICATIONS = {
    "notepad": ["notepad.exe"],
    "calculator": ["calc.exe"],
    "explorer": ["explorer.exe"],
    "chrome": ["cmd", "/c", "start", "", "chrome"],
    "code": ["cmd", "/c", "start", "", "code"],
}


def open_application(application: str) -> str:

    name = application.lower().strip()

    command = APPLICATIONS.get(name)

    if command is None:
        return f"I don't know how to open {application}."

    try:
        subprocess.Popen(command)

        return f"Opened {application}."

    except Exception as e:
        return f"Failed to open {application}: {e}"