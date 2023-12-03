import keyboard
import time
def press_alt_tab():
    time.sleep(5)
    keyboard.press_and_release('alt+f4')

press_alt_tab()