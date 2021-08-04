# Adafruit MIDI Launchgrid

This project creates an 8x8 MIDI Launch Grid with a 3x4 Key Grid, OLED 
Display, Faders and an Endless Encoder.

This project is inspired by the [Adabox 019 "Ableton Live Launcher"](https://learn.adafruit.com/ableton-live-macropad-launcher/overview) 
project by [John Park](https://learn.adafruit.com/users/johnpark)

## Library Requirements

Install the following libraries in your `/lib` folder

```
adafruit_bus_device
adafruit_debouncer.mpy
adafruit_display_text
adafruit_hid
adafruit_macropad.mpy
adafruit_midi
adafruit_neotrellis
adafruit_pcf8591
adafruit_pixelbuf.mpy
adafruit_seesaw
adafruit_simple_text_display.mpy
adafruit_simplemath.mpy
neopixel.mpy
simpleio.mpy
```

## Parts List

* [Adafruit MacroPad](https://www.adafruit.com/product/5100)
* [Adafruit NeoTrellis](https://www.adafruit.com/product/3954) x 4 
* [Adafruit PCF8591](https://www.adafruit.com/product/4648)
* [Slide Potentiometer](https://www.adafruit.com/product/4219)

This project uses the "kits" provided for the MacroPad and NeoTrellis, which
includes additional parts such knobs, silocone buttons, keycaps, mechanical 
keys, and various other small parts.


** This project is not affiliated with or endorsed by [Adafruit](https://www.adafruit.com) **