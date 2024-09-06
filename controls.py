import time
from pynput import keyboard
import threading


class _BlockingInputThread(threading.Thread):
    '''
    The `inputs` library's IO is blocking, which means a new thread is needed to wait for
    events to avoid blocking the program when no inputs are received.
    '''
    def __init__(self, lock):
        super(_BlockingInputThread, self).__init__(daemon=True)
        self.lock = lock
        self.space_held = False
    def on_press(self, key):
        self.space_held = True
    def on_release(self, key):
        self.space_held = False
    def run(self):
        listener = keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release)
        listener.start()

def capture_input(engine):
    lock = threading.Lock()
    blockingInputThread = _BlockingInputThread(lock)
    blockingInputThread.start()

    while True:
        with lock:
            engine.throttle(1.0 if blockingInputThread.space_held else 0.0)

        # normal accelleration
        time.sleep(0.02)

        # gaspedal boost
        # time.sleep(0.0029)
