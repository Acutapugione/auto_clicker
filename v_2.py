import threading
import time
import pyautogui

class ClickGenerator(threading.Thread):
    def __init__(self, clicks_per_minute, key):
        super().__init__()
        self._stop_event = threading.Event()
        self.clicks_per_minute = clicks_per_minute
        self.key = key
        
    def run(self):
        while not self._stop_event.is_set():
            pyautogui.press(self.key)
            time.sleep(60 / self.clicks_per_minute)
            
    def stop(self):
        self._stop_event.set()
        
def main():
    clicks_per_minute = int(input("Enter the number of clicks per minute: "))
    key = input("Enter the key to click: ")
    click_generator = ClickGenerator(clicks_per_minute, key)
    click_generator.start()
    
if __name__ == "__main__":
    main()
