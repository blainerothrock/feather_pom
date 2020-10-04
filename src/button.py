import digitalio
import time

class Button():
    
    def __init__(self, name, pin, time_buffer=0.5):
        self._btn = digitalio.DigitalInOut(pin)
        self._btn.direction = digitalio.Direction.INPUT
        self._btn.pull = digitalio.Pull.UP

        self._time_buffer = time_buffer
        self._active = False

        self._pressed = False
        self._start = time.monotonic() + self._time_buffer

    @property
    def active(self):
        return self._active

    def update(self):
        t = time.monotonic()

        self._active = False

        if not self._btn.value and not self._pressed:
            self._pressed = True
            self._active = False
        elif self._btn.value and self._pressed and t > self._start :
            self._pressed = False
            self._active = True
            self._start = t