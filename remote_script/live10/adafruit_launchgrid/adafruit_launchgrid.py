from __future__ import with_statement
import Live
from _Framework.ControlSurface import ControlSurface
from _Framework.DeviceComponent import DeviceComponent
# Class encompassing several channel strips to form a mixer
from _Framework.MixerComponent import MixerComponent
from _Framework.SliderElement import SliderElement
from _Framework.TransportComponent import TransportComponent
from _Framework.ChannelStripComponent import ChannelStripComponent
from _Framework.InputControlElement import *
from _Framework.ButtonElement import ButtonElement
from _Framework.ButtonMatrixElement import ButtonMatrixElement
from _Framework.SessionComponent import SessionComponent
from _Framework.EncoderElement import *
from Launchpad.ConfigurableButtonElement import ConfigurableButtonElement
from config import *


class adafruit_launchgrid(ControlSurface):

    def __init__(self, c_instance):
        super(adafruit_launchgrid, self).__init__(c_instance)
        with self.component_guard():
            global _map_modes
            _map_modes = Live.MidiMap.MapMode
            # mixer
            global mixer
            num_tracks = 128
            num_returns = 24
            self.mixer = MixerComponent(num_tracks, num_returns)
            global active_mode
            active_mode = "_mode1"
            self._set_active_mode()
            self.show_message("Powered by remotify.io")

    def _mode1(self):
        self.show_message("_mode1 is active")
        # transport
        global transport
        self.transport = TransportComponent()
        self.transport.name = 'Transport'

        # key row 1
        record_button = ConfigurableButtonElement(0, MIDI_CC_TYPE, 0, 90)
        record_button.name = 'record_button'
        self.transport.set_record_button(record_button)

        stop_button = ConfigurableButtonElement(0, MIDI_CC_TYPE, 0, 91)
        stop_button.name = 'stop_button'
        self.transport.set_stop_button(stop_button)

        play_button = ConfigurableButtonElement(0, MIDI_CC_TYPE, 0, 92)
        play_button.name = 'play_button'
        self.transport.set_play_button(play_button)

        # key row 2
        seek_backward_button = ConfigurableButtonElement(
            0, MIDI_CC_TYPE, 0, 93)
        seek_backward_button.name = 'seek_backward_button'
        self.transport.set_seek_backward_button(seek_backward_button)

        loop_button = ConfigurableButtonElement(0, MIDI_CC_TYPE, 0, 94)
        loop_button.name = 'loop_button'
        self.transport.set_loop_button(loop_button)

        seek_forward_button = ConfigurableButtonElement(0, MIDI_CC_TYPE, 0, 95)
        seek_forward_button.name = 'seek_forward_button'
        self.transport.set_seek_forward_button(seek_forward_button)

        # key row 3
        punchin_button = ConfigurableButtonElement(1, MIDI_CC_TYPE, 0, 96)
        punchin_button.text = 'punchin_button'
        self.transport.set_punch_in_button(punchin_button)

        punchout_button = ConfigurableButtonElement(1, MIDI_CC_TYPE, 0, 97)
        punchout_button.text = 'punchout_button'
        self.transport.set_punch_out_button(punchout_button)

        metronome_button = ConfigurableButtonElement(0, MIDI_CC_TYPE, 0, 98)
        metronome_button.name = 'metronome_button'
        self.transport.set_metronome_button(metronome_button)

        # mixer
        global mixer
        self.mixer.channel_strip(0).set_pan_control(
            EncoderElement(MIDI_CC_TYPE, 0, 76, _map_modes.absolute))
        self.mixer.channel_strip(0).set_volume_control(
            EncoderElement(MIDI_CC_TYPE, 0, 75, _map_modes.absolute))

        # key row 4
        arm_button = ConfigurableButtonElement(0, MIDI_CC_TYPE, 0, 99)
        #self.mixer.channel_strip(0).set_arm_button(arm_specific_0)

        mute_button = ConfigurableButtonElement(0, MIDI_CC_TYPE, 0, 101)
        #self.mixer.channel_strip(0).set_mute_button(mute_specific_0)
        #self.mixer.channel_strip(0).set_invert_mute_feedback(True)

        solo_button = ConfigurableButtonElement(0, MIDI_CC_TYPE, 0, 100)
        #self.mixer.channel_strip(0).set_solo_button(solo_specific_0)

        track_left_button = ConfigurableButtonElement(0, MIDI_CC_TYPE, 0, ENCODER_LEFT_CC)
        track_right_button = ConfigurableButtonElement(0, MIDI_CC_TYPE, 0, ENCODER_RIGHT_CC)
        self.mixer.set_select_buttons(track_right_button, track_left_button)

        # session

        TSB_X = 8  # number of horizontal buttons
        TSB_Y = 8  # number of vertical buttons
        # Track selection box size (X,Y) (horizontal, vertical).
        self.session = SessionComponent(TSB_X, TSB_Y)
        self.session.name = 'Session'
        # self._session.set_track_bank_buttons(self._note_map[SESSIONRIGHT], self._note_map[SESSIONLEFT])
        # self._session.set_scene_bank_buttons(self._note_map[SESSIONDOWN], self._note_map[SESSIONUP])
        # self._session.set_select_buttons(self._note_map[SCENEDN], self._note_map[SCENEUP])
        # # range(tsb_x) is the horizontal count for the track selection box
        # self._scene_launch_buttons = [self._note_map[SCENELAUNCH[index]] for index in range(TSB_X)]
        # # range(tsb_y) Range value is the track selection
        # self._track_stop_buttons = [self._note_map[TRACKSTOP[index]] for index in range(TSB_Y)]
        # self._session.set_stop_all_clips_button(self._note_map[STOPALLCLIPS])
        # self._session.set_stop_track_clip_buttons(tuple(self._track_stop_buttons))
        self.session.selected_scene().name = 'Selected_Scene'
        # self._session.selected_scene().set_launch_button(self._note_map[SELSCENELAUNCH])
        # self._session.set_slot_launch_button(self._note_map[SELCLIPLAUNCH])
        # Change range() value to set the vertical count for track selection box
        for scene_index in range(TSB_Y):
            scene = self.session.scene(scene_index)
            scene.name = 'Scene_' + str(scene_index)
            button_row = []
            # scene.set_launch_button(self._scene_launch_buttons[scene_index])
            scene.set_triggered_value(2)
            # Change range() value to set the horizontal count for track selection box
            for track_index in range(TSB_X):
                # button = self._note_map[GRID_NOTES[scene_index][track_index]]
                note = GRID_NOTES[scene_index][track_index]
                button = ButtonElement(1, MIDI_NOTE_TYPE, 0, note)
                button.name = 'Note_' + str(note)
                button_row.append(button)
                clip_slot = scene.clip_slot(track_index)
                clip_slot.name = str(track_index) + \
                    '_Clip_Slot_' + str(scene_index)
                clip_slot.set_launch_button(button)

    def on_arm_button(self):
        self.mixer.selected_strip

    def _remove_mode1(self):
        # mixer
        global mixer
        self.mixer.channel_strip(0).set_pan_control(None)
        self.mixer.channel_strip(0).set_volume_control(None)
        self.mixer.channel_strip(0).set_arm_button(None)
        self.mixer.channel_strip(0).set_mute_button(None)
        self.mixer.channel_strip(0).set_solo_button(None)
        # transport
        global transport
        self.transport.set_seek_backward_button(None)
        self.transport.set_seek_forward_button(None)
        self.transport.set_record_button(None)
        self.transport.set_loop_button(None)
        self.transport.set_play_button(None)
        self.transport.set_stop_button(None)
        self.transport = None

    def _on_selected_track_changed(self):
        ControlSurface._on_selected_track_changed(self)
        self._display_reset_delay = 0
        value = "selected track changed"
        if (hasattr(self, '_set_track_select_led')):
            self._set_track_select_led()
        if (hasattr(self, '_reload_active_devices')):
            self._reload_active_devices(value)
        if (hasattr(self, 'update_all_ab_select_LEDs')):
            self.update_all_ab_select_LEDs(1)

    def _is_prev_device_on_or_off(self):
        self._device = self.song().view.selected_track.view.selected_device
        self._device_position = self.selected_device_idx()
        if (self._device is None) or (self._device_position == 0):
            on_off = "off"
        else:
            on_off = "on"
        return on_off

    def _is_nxt_device_on_or_off(self):
        # add one as this starts from zero
        self._selected_device = self.selected_device_idx() + 1
        if (self._device is None) or (self._selected_device == len(self.song().view.selected_track.devices)):
            on_off = "off"
        else:
            on_off = "on"
        return on_off

    def _set_active_mode(self):
        global active_mode
        # activate mode
        if active_mode == "_mode1":
            self._mode1()
        if hasattr(self, '_set_track_select_led'):
            self._set_track_select_led()
        if hasattr(self, '_turn_on_device_select_leds'):
            self._turn_off_device_select_leds()
            self._turn_on_device_select_leds()
        if hasattr(self, '_all_prev_device_leds'):
            self._all_prev_device_leds()
        if hasattr(self, '_all_nxt_device_leds'):
            self._all_nxt_device_leds()
        if hasattr(self, 'update_all_ab_select_LEDs'):
            self.update_all_ab_select_LEDs(1)

    def _remove_active_mode(self):
        global active_mode
        # remove activate mode
        if active_mode == "_mode1":
            self._remove_mode1()

    def _activate_mode1(self, value):
        global active_mode
        global shift_previous_is_active
        if value > 0:
            shift_previous_is_active = "off"
            self._remove_active_mode()
            active_mode = "_mode1"
            self._set_active_mode()

    def _activate_shift_mode1(self, value):
        global active_mode
        global previous_shift_mode1
        global shift_previous_is_active
        if value > 0:
            shift_previous_is_active = "on"
            previous_shift_mode1 = active_mode
            self._remove_active_mode()
            active_mode = "_mode1"
            self._set_active_mode()
        elif shift_previous_is_active == "on":
            try:
                previous_shift_mode1
            except NameError:
                self.log_message("previous shift mode not defined yet")
            else:
                self._remove_active_mode()
                active_mode = previous_shift_mode1
                self._set_active_mode()

    def selected_device_idx(self):
        self._device = self.song().view.selected_track.view.selected_device
        return self.tuple_index(self.song().view.selected_track.devices, self._device)

    def selected_track_idx(self):
        self._track = self.song().view.selected_track
        self._track_num = self.tuple_index(self.song().tracks, self._track)
        self._track_num = self._track_num + 1
        return self._track_num

    def tuple_index(self, tuple, obj):
        for i in xrange(0, len(tuple)):
            if (tuple[i] == obj):
                return i
        return(False)

    def disconnect(self):
        super(adafruit_launchgrid, self).disconnect()
