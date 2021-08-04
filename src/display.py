import board
import displayio
import terminalio
from adafruit_display_text import label
from config import *

# --- create display strings and positions
x1 = 5
x2 = 35
x3 = 65
y1 = 17
y2 = 27
y3 = 37
y4 = 47
y5 = 57
FONT = terminalio.FONT


class Display:
    def __init__(self):
        # ---Display setup---
        display = board.DISPLAY
        screen = displayio.Group()
        display.show(screen)

        # Draw a title label
        title = TITLE_TEXT
        title_area = label.Label(FONT, text=title, color=0xFFFFFF, x=6, y=3)
        screen.append(title_area)

        # ---Push knob text setup
        push_text_area = label.Label(
            FONT, text="[o]", color=0xffffff, x=WIDTH-22, y=y2)
        screen.append(push_text_area)

        # ---CC knob text setup
        cc_label_text_area = label.Label(
            FONT, text=ENCODER_TEXT, color=0xffffff, x=WIDTH - 42, y=y4)
        screen.append(cc_label_text_area)
        # --- cc value display
        cc_val_text = str(CC_OFFSET)
        cc_val_text_area = label.Label(
            FONT, text=cc_val_text, color=0xffffff, x=WIDTH - 20, y=y5)
        screen.append(cc_val_text_area)

        label_data = (
            # text, x, y
            (TRACK_NAMES[0], x1, y1), (TRACK_NAMES[1],
                                       x2, y1), (TRACK_NAMES[2], x3, y1),
            (".", x1, y2), (".", x2, y2), (".", x3, y2),
            (".", x1, y3), (".", x2, y3), (".", x3, y3),
            (".", x1, y4), (".", x2, y4), (".", x3, y4),
            (".", x1, y5), (".", x2, y5), (".", x3, y5)
        )

        labels = []

        for data in label_data:
            text, x, y = data
            label_area = label.Label(FONT, text=text, color=0xffffff)
            group = displayio.Group(x=x, y=y)
            group.append(label_area)
            screen.append(group)
            labels.append(label_area)  # these are individually addressed later

        self.display = display
        self.screen = screen
        self.cc_label_text_area = cc_label_text_area
        self.cc_val_text_area = cc_val_text_area
        self.push_text_area = push_text_area

    def set_fader_display(self, fader, value):
        self.cc_val_text_area.text = str(value)
        self.cc_label_text_area.text = FADERS[fader][0]

    def set_encoder_display(self, encoder, value):
        self.cc_val_text_area.text = str(value)
        self.cc_label_text_area.text = ENCODER_TEXT
    
    def set_modifier(self, modifier):
        if modifier: 
            self.push_text_area.text = "[.]"
        else:
            self.push_text_area.text = "[o]"
