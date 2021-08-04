from config import *
import board
from adafruit_simplemath import constrain
from adafruit_midi.control_change import ControlChange
from adafruit_midi.note_off import NoteOff
from adafruit_midi.note_on import NoteOn
from adafruit_midi.midi_message import MIDIUnknownEvent

class KeyGrid:
    def __init__(self, macropad, display, midi):
        self.macropad = macropad
        self.display = display
        self.midi = midi
        self.last_position = 0
        self.modifier = False
        self.init_keygrid()

    def set_brightness(self, brightness):
        self.macropad.pixels.brightness = brightness

    def init_keygrid(self):
        print("KeyGrid::init")
        self.set_brightness(BRIGHT)

    def sync(self):
        key_event = self.macropad.keys.events.get()  # check for keypad events

        if not key_event:  # Event is None; no keypad event happened, do other stuff
            position = self.macropad.encoder  # store encoder position state
            # lock to cc range
            cc_position = int(constrain((position + CC_OFFSET), 0, 127))

            if self.last_position is None or position != self.last_position:
                if position != self.last_position:
                    self.midi.send(ControlChange(ENCODER_CC_NUMBER, cc_position))
                    print("Encoder: %2d" % (cc_position), ENCODER_CC_NUMBER, cc_position)
                    self.display.set_encoder_display(0, cc_position)
                    # cc_val_text_area.text = str(cc_position)
                    # fader_text_area.text = ENCODER_TEXT
            self.last_position = position

            # check the encoder switch w debouncer
            self.macropad.encoder_switch_debounced.update()
            if self.macropad.encoder_switch_debounced.pressed:
                print("Mod")
                self.modifier = True
                self.set_brightness(DIM)

            if self.macropad.encoder_switch_debounced.released:
                self.modifier = False
                self.set_brightness(BRIGHT)
            self.display.set_modifier(self.modifier)
            return # replaces continue?

        num = key_event.key_number

        print("Macropad", num, key_event.pressed, key_event.released)
        if num == 0:
            if key_event.pressed:
                self.midi.send(ControlChange(CC_STOP, 127))
            print("sent Stop", num)
        elif num == 1:
            if key_event.pressed:
                self.midi.send(ControlChange(CC_PLAY, 127))
            print("sent Start", num)
        elif num == 2:
            if key_event.pressed:
                self.midi.send(ControlChange(CC_REC, 127))
            print("sent Record", num)
        elif num == 3:
            if key_event.pressed:
                self.midi.send(ControlChange(CC_RWD, 127))
            if key_event.pressed:
                self.midi.send(ControlChange(CC_RWD, 0))
            print("sent Rewind", num)
        elif num == 4:
            if key_event.pressed:
                self.midi.send(ControlChange(CC_LOOP, 127))
            # elif key_event.released:
            #    self.midi.send(ControlChange(CC_LOOP, 0))
            print("sent LOOP", num)
        elif num == 3:
            if key_event.pressed:
                self.midi.send(ControlChange(CC_FWD, 127))
            # elif key_event.released:
            #    self.midi.send(ControlChange(CC_FWD, 0))
            print("sent Forward", num)

        self.macropad.pixels.show()