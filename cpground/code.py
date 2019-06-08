from adafruit_circuitplayground.express import cpx
from digitalio import DigitalInOut, Direction, Pull
import audioio
import board


LEDS = [[board.A1, 6], [board.A2, 8], [board.A3, 9]]
PINS = []
for idx, spec in enumerate(LEDS):
    pin = DigitalInOut(spec[0])
    pin.direction = Direction.INPUT
    pin.pull = Pull.UP
    PINS.append({'pin': pin, 'np': spec[1]})

cpx.pixels.brightness = 0.1


while True:
    for pin in PINS:
        if pin['pin'].value:
            cpx.pixels[pin['np']] = (255, 0, 0)
        else:
            cpx.pixels[pin['np']] = (0, 255, 0)

