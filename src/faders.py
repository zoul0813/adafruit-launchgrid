from config import *
import board
import simpleio
import adafruit_pcf8591.pcf8591 as PCF
from adafruit_pcf8591.analog_in import AnalogIn
from adafruit_pcf8591.analog_out import AnalogOut
from adafruit_midi.control_change import ControlChange

class Faders:
    def __init__(self, i2c_bus, display, midi):
        print("Faders::init")
        self.pcf = PCF.PCF8591(i2c_bus)
        self.display = display
        self.midi = midi

        self.positions = [0,0,0,0]

    def sync(self):
        # TODO: Loop for up to 4 faders
        for i in range(0,FADER_COUNT):
            pcf_in = AnalogIn(self.pcf, i) # replace PCF.A0 with 'i' as PCF.A0 is const(0)
            raw_value = pcf_in.value
            mapped_value = simpleio.map_range(raw_value, 0, 65535, 0, 127)
            mapped_value_out = int(abs(mapped_value - 127))
            if self.positions[i] is None or self.positions[i] != mapped_value_out:
                CC = FADERS[0][1]
                scaled_value = (raw_value / 65535) * pcf_in.reference_voltage
                print("Fader: %0.2fV" % (scaled_value), CC, raw_value, pcf_in.reference_voltage, mapped_value_out)
                self.midi.send(ControlChange(CC, mapped_value_out))
                self.display.set_fader_display(0, mapped_value_out)
            self.positions[i] = mapped_value_out