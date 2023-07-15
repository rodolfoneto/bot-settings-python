
import pyautogui
import time

def close_settings_window(window_title):
    try:
        window = pyautogui.getWindowsWithTitle(window_title)[0]
        window.activate()
        window.close()
        # window.maximize()

    except IndexError:
        print("Window not found.")

# Usage example
if __name__ == '__main__':
    close_settings_window("ID.827868070 | Configu")