import time
from button import Button
import json

from piezo import buzz

class Timer:
    def __init__(self, datetime):
        self._state = 0

        self.datetime = datetime
        self.time = time.mktime(self.datetime)

        self.countdown = 0
        self.timer = 0

        self.countdown_title = ""
    
    @property
    def state(self):
        return self._state
    
    @state.setter
    def state(self, n):
        self._state = n

    def start_countdown(self, countdown, title):
        self.countdown = countdown
        self.countdown_title = title
        self._state = 1
    
    @property
    def total_poms(self):
        return ''

    @property
    def pretty_datetime(self):
        return f'{self.datetime.tm_mon:02}.{self.datetime.tm_mday:02}.{self.datetime.tm_year} {self.datetime.tm_hour:02}:{self.datetime.tm_min:02}:{self.datetime.tm_sec:02}'

    @property
    def pretty_countdown(self):
        min = int(self.countdown / 60)
        sec = int(self.countdown % 60)
        return f'{min:02}:{sec:02}'

    def update(self, datetime):
        self.datetime = datetime
        self.time = time.mktime(self.datetime)

        if self._state == 1: # countdown
            self.countdown -= 1

            if self.countdown == 0:
                self._timer = 0
                self._state = 3
        
        if self._state == 3:
            self.timer += 1
            if self.timer == 10:
                self._state = 0
                self.timer = 0

    
    def _state_label(self):
        if self.state == 0: return 'idle'
        if self.state == 1: return 'timer'
        if self.state == 2: return 'paused'
        if self.state == 3: return 'done'
        if self.state == -1: return 'ERR'

    def __str__(self):
        return self._state_label()