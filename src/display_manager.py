from adafruit_display_text import label
import displayio
import terminalio
import time

font = terminalio.FONT
WIDTH = 128

def present(pom):
    if pom.state == 0:
        return state_0(pom)
    if pom.state == 1:
        return state_1(pom)
    if pom.state == 2: 
        return state_2(pom)
    if pom.state == 3:
        return state_3(pom)
    if pom.state == 4:
        return state_4(pom)

def lbl(text, y):
    lbl_state = label.Label(font, text=f'{text}')
    (_, _, width, height) = lbl_state.bounding_box
    lbl_state.x = WIDTH  // 2 - width // 2
    lbl_state.y = y

    return lbl_state

def state_0(pom):

    lbl_time = lbl(pom.pretty_datetime, 5)
    lbl_state = lbl(pom, 5 + 14)

    grp = displayio.Group()
    grp.append(lbl_time)
    grp.append(lbl_state)

    return grp

def state_1(pom):
    lbl_time = lbl(f'{pom.countdown_title}', 5)
    lbl_state = lbl(pom.pretty_countdown, 5 + 14)

    grp = displayio.Group()
    grp.append(lbl_time)
    grp.append(lbl_state)

    return grp

def state_2(pom):
    lbl_time = lbl('PAUSED', 5)
    lbl_state = lbl(pom.pretty_countdown, 5 + 14)

    grp = displayio.Group()
    grp.append(lbl_time)
    grp.append(lbl_state)

    return grp

def state_3(pom):
    lbl_time = lbl('DONE!!!', 5)
    lbl_state = lbl(pom.pretty_countdown, 5 + 14)

    grp = displayio.Group()
    grp.append(lbl_time)
    grp.append(lbl_state)

    return grp