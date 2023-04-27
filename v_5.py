import time
import threading
import pyautogui
from pynput.keyboard import Listener, KeyCode

pyautogui.FAILSAFE = False
clicks_per_minute = 60
delay = 60.0 / clicks_per_minute
start_stop_key = KeyCode(char='s')
exit_key = KeyCode(char='e')


class ClickMouse(threading.Thread):
    def __init__(self, delay):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                # x, y = pyautogui.position()
                x, y = (450, 356)
                # pyautogui.click(x, y)
                pyautogui.click(x, y, duration=1)
                time.sleep(self.delay)
            time.sleep(0.1)


click_thread = ClickMouse(delay)
click_thread.start()


def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == exit_key:
        click_thread.exit()
        listener.stop()


with Listener(on_press=on_press) as listener:
    listener.join()

from pynput.mouse import Button, Controller

mouse = Controller()
#450, 356
while 1:
    print ("Current position: " + str(mouse.position))