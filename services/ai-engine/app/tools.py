from datetime import datetime


def get_current_time() -> str:
    """Return the current time."""

    return datetime.now().strftime("%I:%M %p")