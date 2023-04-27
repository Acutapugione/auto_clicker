import tkinter as tk
import time
import threading
import pyautogui

class MouseClicker:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Mouse Clicker")

        self.label1 = tk.Label(text="Number of clicks per minute:")
        self.label1.pack()

        self.entry1 = tk.Entry()
        self.entry1.insert(0, "60")
        self.entry1.pack()

        self.button = tk.Button(text="Start", command=self.start_clicking)
        self.button.pack()

    def start_clicking(self):
        self.button.config(state=tk.DISABLED)
        self.num_clicks = int(self.entry1.get())
        self.click_delay = 60.0 / self.num_clicks
        self.stop_flag = False
        self.thread = threading.Thread(target=self.click_loop)
        self.thread.start()

    def click_loop(self):
        while not self.stop_flag:
            pyautogui.click(button='left')
            time.sleep(self.click_delay)

    def stop_clicking(self):
        self.stop_flag = True
        self.thread.join()
        self.button.config(state=tk.NORMAL)

if __name__ == '__main__':
    mouse_clicker = MouseClicker()
    mouse_clicker.root.mainloop()