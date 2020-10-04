import adafruit_ds3231

class Clock:

    def __init__(self, i2c):
        self._device = adafruit_ds3231.DS3231(i2c)

    def datetime(self):
        return self._device.datetime

    def pretty_datetime(self):
        return f'{self.datetime.tm_mon}.{self.datetime.tm_mday}.{self.datetime.tm_year} {self.datetime.tm_hour}:{self.datetime.tm_min}:{self.datetime.tm_sec}'