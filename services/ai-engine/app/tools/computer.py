

import pyautogui


def take_screenshot(path: str = "screen.png") -> str:
    try:
        screenshot = pyautogui.screenshot()
        screenshot.save(path)

        return f"Screenshot saved to {path}"

    except Exception as e:
        return f"Failed to take screenshot: {e}"