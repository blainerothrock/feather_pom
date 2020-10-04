import board
import time
import neopixel
import adafruit_lsm303_accel

from button import Button
from display_manager import present
from pom import Pom
from display import Display
from clock import Clock
from accelerometer import Accelerometer
from state import State
from piezo import buzz

i2c = board.I2C()

display = Display(i2c)
clock = Clock(i2c)
accel = Accelerometer(i2c)
led = neopixel.NeoPixel(board.NEOPIXEL, 1)

led.brightness = 0.0

btnA = Button('A', board.D9)
btnB = Button('B', board.D6)
btnC = Button('C', board.D5)



# set the date (year, mon, day, hour, min, sec, day_of_week, day_of_year, dst)
# rtc.datetime = time.struct_time((2020, 10, 2, 12, 59, 40, 4, 276, 0))

pom = Pom(clock.datetime())
state = State()

while True:

    current = clock.datetime()
    state.update(btnA, btnB, btnC, display, pom, accel, current)
    

print('complete --*')