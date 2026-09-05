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
        return f"Failed to create file : {e}"


def read_file(path: str) -> str:
    file = Path(path).expanduser()

    if not file.exists():
        return f"File does not exist: {path}"

    if not file.is_file():
        return f"Not a file: {path}"

    try:
        return file.read_text(encoding="utf-8")

    except Exception as e:
        return f"Failed to read file : {e}"



def get_special_folder(folder : str) -> str:

    home = Path.home()

    folders = {
        "home": home,
        "desktop": home / "Desktop",
        "documents": home / "Documents",
        "downloads": home / "Downloads",
        "pictures": home / "Pictures",
        "music": home / "Music",
        "videos": home / "Videos",
    }

    path = folders.get(folder.lower())

    if not path:
        return f"Unknown special folder: {folder}"

    if not path.exists():
        return f"special folder does not exist: {path}"

    return str(path)


def write_file(path: str, content: str) -> str:
    file = Path(path).expanduser()

    try:
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_text(content, encoding="utf-8")

        return f"File written successfully: {file}"
    except Exception as e:
        return f"Failed to write file: {e}"


def append_file(path: str, content: str) -> str:
    file = Path(path).expanduser()

    try:
        file.parent.mkdir(parents=True, exist_ok=True)
        with file.open("a", encoding="utf-8") as f:
            f.write(content)

        return f"Content appended successfully: {file}"
    except Exception as e:
        return f"Failed to append content: {e}"