import threading
import tkinter as tk
import time
import pyautogui
from Xlib import X, display, ext

class ClickGenerator:
    def __init__(self, clicks_per_minute):
        self.clicks_per_second = clicks_per_minute / 60.0
        self.interval = 1.0 / self.clicks_per_second
        self.running = False
        self.click_thread = None

    def start_clicks(self):
        self.running = True
        self.click_thread = threading.Thread(target=self._click_thread)
        self.click_thread.start()

    def stop_clicks(self):
        self.running = False
        if self.click_thread:
            self.click_thread.join()
            self.click_thread = None

    def _click_thread(self):
        while self.running:
            pyautogui.click()
            time.sleep(self.interval)

class App:
    def __init__(self, clicks_per_minute=60):
        self.click_generator = ClickGenerator(clicks_per_minute)

        self.root = tk.Tk()
        self.root.title("Click Generator")
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        self.root.bind("<KeyPress-F6>", self.toggle_clicks)

        self.frame = tk.Frame(self.root)
        self.frame.pack()

        self.clicks_label = tk.Label(self.frame, text="Clicks per minute:")
        self.clicks_label.pack(side=tk.LEFT)

        self.clicks_entry = tk.Entry(self.frame)
        self.clicks_entry.insert(0, str(clicks_per_minute))
        self.clicks_entry.pack(side=tk.LEFT)

        self.start_button = tk.Button(self.root, text="Start", command=self.start_clicks)
        self.start_button.pack()

        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_clicks)
        self.stop_button.pack()

        self.update()

    def update(self):
        clicks_per_minute = int(self.clicks_entry.get())
        self.click_generator.clicks_per_second = clicks_per_minute / 60.0
        self.click_generator.interval = 1.0 / self.click_generator.clicks_per_second

        self.root.after(1000, self.update)

    def start_clicks(self):
        self.click_generator.start_clicks()

    def stop_clicks(self):
        self.click_generator.stop_clicks()

    def toggle_clicks(self, event):
        if self.click_generator.running:
            self.click_generator.stop_clicks()
        else:
            self.click_generator.start_clicks()

    def on_close(self):
        self.stop_clicks()
        self.root.destroy()

def main():
    app = App()
    app.root.mainloop()

if __name__ == '__main__':
    main()
