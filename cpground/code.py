from adafruit_circuitplayground.express import cpx
from digitalio import DigitalInOut, Direction, Pull
import audioio
import board


INPUTS = [
    {'board': board.A1, 'pixel': 6, 'drum': 'snare-8'},
    {'board': board.A2, 'pixel': 8, 'drum': 'kick-8'},
    {'board': board.A5, 'pixel': 1, 'drum': 'hihat-8'},
    {'board': board.A6, 'pixel': 3, 'drum': 'rimshot'},
]


def play_file(filename):
    wave_file = open(filename, "rb")
    with audioio.WaveFile(wave_file) as wave:
        with audioio.AudioOut(board.A0) as audio:
            print("playing %s" % filename)
            audio.play(wave)
            while audio.playing:
                pass


def init():
    for input_spec in INPUTS:
        pin = DigitalInOut(input_spec['board'])
        pin.direction = Direction.INPUT
        pin.pull = Pull.UP
        input_spec['pin'] = pin

    cpx.pixels.brightness = 0.1


init()


while True:
    for input_spec in INPUTS:
        if input_spec['pin'].value:
            cpx.pixels[input_spec['pixel']] = (255, 0, 0)
        else:
            cpx.pixels[input_spec['pixel']] = (0, 255, 0)
            play_file("%s.wav" % input_spec['drum'])

