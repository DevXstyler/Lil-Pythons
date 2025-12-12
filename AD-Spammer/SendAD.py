from pynput import keyboard
from pynput.keyboard import Controller, Key
import threading
import time

keyboard_controller = Controller()

def spam_ad():
    for _ in range(int(27 / 0.1)):  # 5 seconds, 0.1s per A+D
        keyboard_controller.press('a')
        keyboard_controller.release('a')
        #time.sleep(0.01)
        keyboard_controller.press('d')
        keyboard_controller.release('d')
        #time.sleep(0.01)
    print("Spam finished.")

def on_press(key):
    if key == Key.enter and pressed_keys.get(Key.f1, False):
        threading.Thread(target=spam_ad).start()

def on_release(key):
    if key in pressed_keys:
        pressed_keys[key] = False

pressed_keys = {}

def on_key_event(key):
    if key in [Key.f1, Key.enter]:
        pressed_keys[key] = True
        on_press(key)

listener = keyboard.Listener(
    on_press=on_key_event,
    on_release=on_release
)

listener.start()
print("Running in background. Press F1 + Enter to start.")

listener.join()