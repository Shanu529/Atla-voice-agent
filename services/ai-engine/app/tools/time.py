

from datetime import datetime


def get_current_time() -> str:
    return datetime.now().strftime("%I:%M %p")


def get_current_date() -> str:
    return datetime.now().strftime("%A, %B %d, %Y")