

from pathlib import Path


def list_directory(path: str = ".") -> str:

    directory = Path(path)

    if not directory.exists():
        return f"Directory {path} does not exist."

    if not directory.is_dir():
        return f"{path} is not a directory."

    files = [item.name for item in directory.iterdir()]

    if not files:
        return "The directory is empty."

    return "\n".join(files)


def read_file(path: str) -> str:

    file = Path(path)

    if not file.exists():
        return f"File {path} does not exist."

    if not file.is_file():
        return f"{path} is not a file."

    try:
        return file.read_text(encoding="utf-8")

    except Exception as e:
        return f"Could not read file: {e}"


def create_file(path: str) -> str:

    file = Path(path)

    if file.exists():
        return f"File {path} already exists."

    try:
        file.touch()
        return f"Created {path}."

    except Exception as e:
        return f"Could not create file: {e}"