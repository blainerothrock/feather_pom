import adafruit_lsm303_accel


class Accelerometer:

    def __init__(self, i2c):
        self._device = adafruit_lsm303_accel.LSM303_Accel(i2c)
        
        self._device.range = adafruit_lsm303_accel.Range.RANGE_8G
        self._device.set_tap(1, 5)

    @property
    def acceleration(self):
        return self._device.acceleration

    @property
    def orientation(self):
        x, y, z = self._device.acceleration

        _max = max(abs(x), abs(y), abs(z))

        if _max == abs(x):
            if x < 0: return 1
            else: return 3
        elif _max == abs(z):
            if z < 0: return 2
            else: return 0
        elif _max == abs(y):
            if y < 0: return 4
            else: return 5

    @property
    def tapped(self):
        return self._device.tapped