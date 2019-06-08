from adafruit_circuitplayground.express import cpx
from digitalio import DigitalInOut, Direction, Pull
import audioio
import board

DRUMS = [
    [board.A6, "snare", board.A7],
    [board.A5, "kick", board.A4],
    [board.A2, "hihat", board.A3],
]


def play_file(filename):
    wave_file = open(filename, "rb")
    with audioio.WaveFile(wave_file) as wave:
        with audioio.AudioOut(board.A0) as audio:
            print("playing %s" % filename)
            audio.play(wave)
            while audio.playing:
                pass


for drum in DRUMS:
    drum_pin = DigitalInOut(drum[0])
    drum_pin.direction = Direction.INPUT
    drum_pin.pull = Pull.UP
    drum.append(drum_pin)
    led_pin = DigitalInOut(drum[2])
    led_pin.direction = Direction.OUTPUT
    drum.append(led_pin)


while True:
    for drum in DRUMS:
        if not drum[3].value:
            try:
                drum[4].value = True
                play_file("%s-8.wav" % drum[1])
                drum[4].value = False
            except Exception as e:
                print(e)
