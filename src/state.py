import time
import pulseio
import board

class State:

    def __init__(self):
        self.last = None

    def update(self, btnA, btnB, btnC, display, pom, accel, current):
        if self.last == None: 
            self.last = current

        # on
        if display.state == 1: # on
            if pom.state == 0:
                if btnA.active:
                    pom.state = 1
            elif pom.state == 1:
                if btnA.active:
                    pom.state = 2
            elif pom.state == 2:
                if btnA.active:
                    pom.state = 1
        
        # turn on display on btn press and reset on timer on each press
        if any([btnA.active, btnB.active, btnC.active, pom.state == 3, accel.tapped]):
            display.state = 1
        
        # perform all time based updates
        btnA.update()
        btnB.update()
        btnC.update()
        display.handle_presentation(pom)

        if current > self.last:
            self.last = current # tick
            display.update()
            pom.update(current)