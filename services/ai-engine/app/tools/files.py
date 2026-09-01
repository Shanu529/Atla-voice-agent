from pathlib import Path


def list_directory(path: str) -> str:
    folder = Path(path).expanduser()

    if not folder.exists():
        return f"Directory does not exist: {path}"

    if not folder.is_dir():
        return f"Not a directory: {path}"

    items = []

    for item in folder.iterdir():
        kind = "DIR" if item.is_dir() else "FILE"
        items.append(f"{kind}: {item.name}")

    return "\n".join(items) if items else "Directory is empty."


def create_folder(path: str) -> str:
    folder = Path(path).expanduser()

    try:
        folder.mkdir(parents=True, exist_ok=True)
        return f"Folder created: {folder}"

    except Exception as e:
        return f"Failed to create folder: {e}"


def create_file(path: str) -> str:
    file = Path(path).expanduser()

    try:
        file.parent.mkdir(parents=True, exist_ok=True)
        file.touch(exist_ok=True)

        return f"File created: {file}"

    except Exception as e:
        return f"Failed to create file Please try again : {e}"


def read_file(path: str) -> str:
    file = Path(path).expanduser()

    if not file.exists():
        return f"File does not exist: {path}"

    if not file.is_file():
        return f"Not a file: {path}"

    try:
        return file.read_text(encoding="utf-8")

    except Exception as e:
        return f"Failed to read file: {e}"