from adafruit_circuitplayground.express import cpx
import audioio
import board
import time

COOLDOWN = 0.2
LAST_HIT = time.time()
TOUCH_ON = False


def play_file(filename):
    # global LAST_HIT;
    # if (time.time() - LAST_HIT) < COOLDOWN:
        # print("cooling")
        # return

    # LAST_HIT = time.time()

    wave_file = open(filename, "rb")
    with audioio.WaveFile(wave_file) as wave:
        with audioio.AudioOut(board.A0) as audio:
            if audio.playing:
                print("stopping")
                audio.stop()
                while audio.playing:
                    pass

            print("playing")
            audio.play(wave)


while True:
    if cpx.touch_A7:
        if not TOUCH_ON:
            TOUCH_ON = True
            cpx.pixels[3] = (255, 0, 0)
            try:
                play_file("rimshot.wav")
            except Exception as e:
                print(e)
        else:
            print("already touching, not continuing to play")
        time.sleep(COOLDOWN)
    else:
        if TOUCH_ON:
            print("stopped touching")
        TOUCH_ON = False
        cpx.pixels[3] = (0, 0, 0)
