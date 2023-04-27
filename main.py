import tkinter as tk
import pyautogui
import time
import threading

class AutoClickerGUI:
    def __init__(self, master):
        self.master = master
        master.title("AutoClicker")

        self.clicks_per_minute = 0
        self.interval = None
        self.running = False

        self.label = tk.Label(master, text="Clicks per minute:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.button = tk.Button(master, text="Start", command=self.start_clicker)
        self.button.pack()

        self.stop_button = tk.Button(master, text="Stop", command=self.stop_clicker, state="disabled")
        self.stop_button.pack()

    def start_clicker(self):
        self.clicks_per_minute = int(self.entry.get())
        self.interval = 60.0 / self.clicks_per_minute
        self.running = True
        self.thread = threading.Thread(target=self.clicker)
        self.thread.start()
        self.button.config(state="disabled")
        self.stop_button.config(state="normal")

    def stop_clicker(self):
        self.running = False
        self.button.config(state="normal")
        self.stop_button.config(state="disabled")

    def clicker(self):
        while self.running:
            pyautogui.click()
            time.sleep(self.interval)

root = tk.Tk()
gui = AutoClickerGUI(root)
root.mainloop()