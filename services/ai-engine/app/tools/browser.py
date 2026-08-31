

import webbrowser


def open_website(url: str) -> str:

    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    webbrowser.open(url)

    return f"Opened {url}."