import time
import pulseio
import board
import json
from piezo import buzz

class Pom:

    def __init__(self):
        self.last = None

        with open('pom.json', 'r') as f:
            self.config = json.load(f)

        self.pom_time = self.config.get('pom_time', 1500)
        self.break_time = self.config.get('break_time', 300)
        self.additional_time = self.config.get('additional_time', 300)

    def update(self, btnA, btnB, btnC, display, timer, accel, current):
        if self.last == None: 
            self.last = current

        # on
        if display.state == 1: # on
            if timer.state == 0:
                if btnA.active:
                    timer.start_countdown(self.pom_time, "POM")
                elif btnB.active:
                    timer.start_countdown(self.break_time, "BREAK")
            elif timer.state == 1:
                if btnA.active:
                    timer.state = 2
                if btnB.active:
                    timer.countdown += self.additional_time
            elif timer.state == 2:
                if btnA.active:
                    timer.state = 1
                if btnC.active:
                    timer.state = 0
        
        # turn on display on btn press and reset on timer on each press
        if any([btnA.active, btnB.active, btnC.active, timer.state == 3, accel.tapped]):
            display.state = 1
        
        # perform all time based updates
        btnA.update()
        btnB.update()
        btnC.update()
        display.handle_presentation(timer)

        if current > self.last:
            self.last = current # tick
            display.update()
            timer.update(current)