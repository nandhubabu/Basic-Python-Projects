import pyautogui
import time

def screenshoot():
    name = int(round(time.time()*1000))
    name = '{}.jpg'.format(name)
    time.sleep(5)
    img = pyautogui.screenshot(name)
    img.show()

screenshoot()