# SPDX-FileCopyrightText: 2021 David Higgins
# SPDX-License-Identifier: MIT
# Ableton Live Control Surface

import time
import board
from adafruit_macropad import MacroPad

import busio

import usb_midi
import adafruit_midi
from adafruit_midi.control_change import ControlChange
from adafruit_midi.note_off import NoteOff
from adafruit_midi.note_on import NoteOn
from adafruit_midi.midi_message import MIDIUnknownEvent

from config import *
from src.display import Display
from src.keygrid import KeyGrid
from src.faders import Faders
from src.launchgrid import LaunchGrid

print(TITLE_TEXT) # just so we know it's working? :)

# --- MIDI recieve is complex, so not using macropad.midi
midi = adafruit_midi.MIDI(
    midi_in=usb_midi.ports[0],
    in_channel=(0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
    midi_out=usb_midi.ports[1],
    out_channel=0
)

#modifier = False  # use to add encoder switch modifier to keys for clip mute
#last_position = 0  # encoder position state
i2c_bus = busio.I2C(board.SCL, board.SDA)
macropad = MacroPad()
display = Display()
keygrid = KeyGrid(macropad, display, midi)
launchgrid = LaunchGrid(i2c_bus, midi)
faders = Faders(i2c_bus, display, midi)

num = 1

while True:
    launchgrid.sync() # sync the trellis to detect presses
    keygrid.sync()
    faders.sync()

    msg_in = midi.receive()
    if isinstance(msg_in, NoteOn) and msg_in.velocity != 0:
        print("received NoteOn", "from channel", msg_in.channel + 1,"MIDI note", msg_in.note, "velocity", msg_in.velocity)
        launchgrid.midi_recieve(msg_in.note, msg_in.velocity) # tell the trellis about the received midi note

    elif isinstance(msg_in, NoteOff):
        print("received NoteOff", "from channel", msg_in.channel + 1)

    elif isinstance(msg_in, NoteOn) and msg_in.velocity == 0:
        print("received NoteOff", "from channel", msg_in.channel + 1, "MIDI note", msg_in.note, "velocity", msg_in.velocity)

    elif isinstance(msg_in, ControlChange):
        print("received CC", "from channel", msg_in.channel + 1, "controller", msg_in.control, "value", msg_in.value)

    elif isinstance(msg_in, MIDIUnknownEvent):
        # Message are only known if they are imported
        print("Unknown MIDI event status ", msg_in.status)

    elif msg_in is not None:
        midi.send(msg_in)