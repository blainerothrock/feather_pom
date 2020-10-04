import displayio
import adafruit_displayio_ssd1306
import time
from display_manager import present

class Display:

    def __init__(self, i2c, timer=10):
        displayio.release_displays()

        display_bus = displayio.I2CDisplay(i2c, device_address=0x3c)
        self._oled = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=32)

        self._state = 0
        self._on_timer = 0.0
        self.timer = timer

    
    @property
    def state(self):
        return self._state
    
    @state.setter
    def state(self, n):
        self._state = n
        if self.state == 1: 
            self._on_timer = 0

    def update(self):
        if self._state == 1:
            self._on_timer += 1

        if self._on_timer >= self.timer:
            self.state = 0

    def handle_presentation(self, pom):
        if self.state == 0:
            splash = displayio.Group(max_size=10)
            self._oled.show(splash)
        else:
            grp = present(pom)
            self._oled.show(grp)