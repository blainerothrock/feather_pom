import simpleio, board


def buzz(pin=board.A0, freq=750, time=0.5):
    simpleio.tone(pin, freq, time)
        