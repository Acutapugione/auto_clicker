import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
import tkinter as tk


class ClickMouse(threading.Thread):
    def __init__(self, delay, button, clicks_per_minute):
        super().__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True
        self.clicks_per_minute = clicks_per_minute

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
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)

    def update_clicks_per_minute(self, new_cpm):
        self.clicks_per_minute = new_cpm
        self.delay = 60 / self.clicks_per_minute


mouse = Controller()
default_clicks_per_minute = 68
delay = 60 / default_clicks_per_minute
button = Button.left
click_thread = ClickMouse(delay, button, default_clicks_per_minute)
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
    elif key == settings_key:
        settings_window()


def settings_window():
    settings = tk.Tk()
    settings.title("Settings")
    settings.geometry("200x200")

    cpm_label = tk.Label(settings, text="Clicks per minute:")
    cpm_label.pack()

    cpm_entry = tk.Entry(settings)
    cpm_entry.pack()

    def update_clicks_per_minute():
        new_cpm = int(cpm_entry.get())
        click_thread.update_clicks_per_minute(new_cpm)

    update_button = tk.Button(settings, text="Update", command=update_clicks_per_minute)
    update_button.pack()

    settings.mainloop()


start_stop_key = KeyCode(char='s')
exit_key = KeyCode(char='e')
settings_key = KeyCode(char='f')

with Listener(on_press=on_press) as listener:
    listener.join()