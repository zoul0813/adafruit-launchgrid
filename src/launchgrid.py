from config import *
import time
# NeoTrellis Imports
from adafruit_neotrellis.neotrellis import NeoTrellis
from adafruit_neotrellis.multitrellis import MultiTrellis
import neopixel

import adafruit_midi
from adafruit_midi.control_change import ControlChange
from adafruit_midi.note_off import NoteOff
from adafruit_midi.note_on import NoteOn
from adafruit_midi.midi_message import MIDIUnknownEvent

C_STARTUP = LP_COLORS[101]
C_STOP = LP_COLORS[120]
C_PRESS = LP_COLORS[87]
C_OFF = LP_COLORS[0]


class LaunchGrid:
    def __init__(self, i2c_bus, macropad, midi):
        # create the i2c object for the trellis
        trelli = [
            [NeoTrellis(i2c_bus, False, addr=TRELLIS_ADDR[0][0]),NeoTrellis(i2c_bus, False, addr=TRELLIS_ADDR[0][1])],
            [NeoTrellis(i2c_bus, False, addr=TRELLIS_ADDR[1][0]), NeoTrellis(i2c_bus, False, addr=TRELLIS_ADDR[1][1])],
        ]
        self.trelli = trelli
        self.trellis = MultiTrellis(self.trelli)
        self.macropad = macropad
        self.midi = midi
        self.init_trellis()

    def sync(self):
        # wrapper
        self.trellis.sync()

    def set_brightness(self, brightness):
        for x in range(2):
            for y in range(2):
                self.trelli[x][y].pixels.brightness = brightness

    def init_trellis(self):
        print("LaunchGrid::init")
        self.set_brightness(DIM)

        for y in range(8):
            for x in range(8):
                # activate rising edge events on all keys
                self.trellis.activate_key(x, y, NeoTrellis.EDGE_RISING)
                # activate falling edge events on all keys
                self.trellis.activate_key(x, y, NeoTrellis.EDGE_FALLING)
                self.trellis.set_callback(x, y, self.trellis_callback)
                self.trellis.color(x, y, C_STARTUP)

            time.sleep(0.05)
            for y in range(8):
                for x in range(8):
                    self.trellis.color(x, y, LP_COLORS[0])
                    if(y == 7):
                        self.trellis.color(x, y, C_STOP)

    def padToNote(self, x, y):
        #note = (80 - (y * 10)) + (x) + 1
        note = GRID_NOTES[y][x]
        print("Trellis", "padToNote", x, y, note)
        return note

    def noteToPad(self, note):
        # note = (80 - (y * 10)) + (x) + 1
        # x = int(note % 10) # get the row
        # y = abs(int((note - x) / 10) - 8) # get the column
        grid = NOTES_GRID[note]
        print("Trellis", "noteToPad", note, grid)
        return grid

    # this will be called when button events are received
    def trellis_callback(self, x, y, edge):
        print("Trellis", x, y, edge)
        note = self.padToNote(x, y)
        # turn the LED on when a rising edge is detected
        if edge == NeoTrellis.EDGE_RISING:
            self.trellis.color(x, y, C_PRESS)
            self.midi.send(NoteOn(note, 127))
            print("sent NoteOn", note)
        # turn the LED off when a rising edge is detected
        elif edge == NeoTrellis.EDGE_FALLING:
            self.trellis.color(x, y, C_OFF)
            if y == 4:
                self.trellis.color(x, y, C_STOP)
            self.midi.send(NoteOff(note, 0))
            print("sent NoteOff", note)


    def midi_recieve(self, note, vel):
        pad = self.noteToPad(note)
        print("Trellis", "midi", note, vel, pad)
        self.trellis.color(pad[0], pad[1], LP_COLORS[vel])
