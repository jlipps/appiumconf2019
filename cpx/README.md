# Circuit Playground Drum Machine App

This is the code that runs on a [Circuit Playground Express](https://www.adafruit.com/product/3333). It is written in [CircuitPython](https://learn.adafruit.com/welcome-to-circuitpython/what-is-circuitpython).

### To run the code

The CPX must be mounted as a USB volume, with the appropriate bootloader (read the CPX docs!). Then all that's necessary to get things running is to copy the code in this directory to the CPX

```
rsync -av ./ /Volumes/CIRCUITPY
```

### To figure out how to connect to device serial console

```
ls /dev/tty.*
# Find the one with "usbmodem"
screen /dev/tty.usbmodemxxxxx
```

This lets you see what's going on on the CPX while running things

### Hardware setup

* 4 drum buttons are supported. Connect buttons to pads A1, A2, A5, A6. Make sure to also ground buttons to one or more of the GND pads.
* Connect audio wire to AO and GND, for audio output.
