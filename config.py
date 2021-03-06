TITLE_TEXT = "Live Launcher 2040"
TRACK_NAMES = ["DRUM", "BASS", "SYNTH"]  # Customize these

ENCODER_CC_NUMBER = 74  # CC number to send w encoder
ENCODER_LEFT_CC = 73
ENCODER_RIGHT_CC = 75
ENCODER_TEXT = "Encode"  # change for intended CC name
ENCODER_DEFAULT = 0  # Initial default value of encoder

FADER_COUNT = 1
FADERS = (
    ("Fader 1", 75),
    ("Fader 2", 76),
    ("Fader 3", 77),
    ("Fader 4", 78)
)

BRIGHT = 0.5
DIM = 0.125

# ---Official Launchpad colors---
LP_COLORS = (
    0x000000, 0x101010, 0x202020, 0x3f3f3f, 0x3f0f0f, 0x3f0000, 0x200000, 0x100000,
    0x3f2e1a, 0x3f0f00, 0x200800, 0x100400, 0x3f2b0b, 0x3f3f00, 0x202000, 0x101000,
    0x213f0c, 0x143f00, 0x0a2000, 0x051000, 0x123f12, 0x003f00, 0x002000, 0x001000,
    0x123f17, 0x003f06, 0x002003, 0x001001, 0x123f16, 0x003f15, 0x00200b, 0x001006,
    0x123f2d, 0x003f25, 0x002012, 0x001009, 0x12303f, 0x00293f, 0x001520, 0x000b10,
    0x12213f, 0x00153f, 0x000b20, 0x000610, 0x0b093f, 0x00003f, 0x000020, 0x000010,
    0x1a0d3e, 0x0b003f, 0x060020, 0x030010, 0x3f0f3f, 0x3f003f, 0x200020, 0x100010,
    0x3f101b, 0x3f0014, 0x20000a, 0x100005, 0x3f0300, 0x250d00, 0x1d1400, 0x080d01,
    0x000e00, 0x001206, 0x00051b, 0x00003f, 0x001113, 0x040032, 0x1f1f1f, 0x070707,
    0x3f0000, 0x2e3f0b, 0x2b3a01, 0x183f02, 0x032200, 0x003f17, 0x00293f, 0x000a3f,
    0x06003f, 0x16003f, 0x2b061e, 0x0a0400, 0x3f0c00, 0x213701, 0x1c3f05, 0x003f00,
    0x0e3f09, 0x153f1b, 0x0d3f32, 0x16223f, 0x0c1430, 0x1a1439, 0x34073f, 0x3f0016,
    0x3f1100, 0x2d2900, 0x233f00, 0x201601, 0x0e0a00, 0x001203, 0x031308, 0x05050a,
    0x050716, 0x190e06, 0x200000, 0x36100a, 0x351204, 0x3f2f09, 0x27370b, 0x192c03,
    0x05050b, 0x36341a, 0x1f3a22, 0x26253f, 0x23193f, 0x0f0f0f, 0x1c1c1c, 0x373f3f,
    0x270000, 0x0d0000, 0x063300, 0x011000, 0x2d2b00, 0x0f0c00, 0x2c1400, 0x120500,
)

# TRELLIS I2C ADDR
TRELLIS_ADDR = (
    (0x2E, 0x2F),
    (0x32, 0x30)
)

# Grid Notes Map
# If we receive a MIDI Note, where does it map to?
NOTES_GRID = {
    81: (0, 0), 82: (1, 0), 83: (2, 0), 84: (3, 0), 85: (4, 0), 86: (5, 0), 87: (6, 0), 88: (7, 0), # 1
    71: (0, 1), 72: (1, 1), 73: (2, 1), 74: (3, 1), 75: (4, 1), 76: (5, 1), 77: (6, 1), 78: (7, 1), # 2
    61: (0, 2), 62: (1, 2), 63: (2, 2), 64: (3, 2), 65: (4, 2), 66: (5, 2), 67: (6, 2), 68: (7, 1), # 3
    51: (0, 3), 52: (1, 3), 53: (2, 3), 54: (3, 3), 55: (4, 3), 56: (5, 3), 57: (6, 3), 58: (7, 1), # 4
    41: (0, 4), 42: (1, 4), 43: (2, 4), 44: (3, 4), 45: (4, 4), 46: (5, 4), 47: (6, 4), 48: (7, 1), # 5
    31: (0, 5), 32: (1, 5), 33: (2, 5), 34: (3, 5), 35: (4, 5), 36: (5, 5), 37: (6, 5), 38: (7, 1), # 6
    21: (0, 6), 22: (1, 6), 23: (2, 6), 24: (3, 6), 25: (4, 6), 26: (5, 6), 27: (6, 6), 28: (7, 1), # 7
    11: (0, 7), 12: (1, 7), 13: (2, 7), 14: (3, 7), 15: (4, 7), 16: (5, 7), 17: (6, 7), 18: (7, 1), # 8
}

# If we press a grid button, what note does it send?
GRID_NOTES = (
    (81, 82, 83, 84, 85, 86, 87, 88),  # 1
    (71, 72, 73, 74, 75, 76, 77, 78),  # 2
    (61, 62, 63, 64, 65, 66, 67, 68),  # 3
    (51, 52, 53, 54, 55, 56, 57, 58),  # 4
    (41, 42, 43, 44, 45, 46, 47, 48),  # 5
    (31, 32, 33, 34, 35, 36, 37, 38),  # 6
    (21, 22, 23, 24, 25, 26, 27, 28),  # 7
    (11, 12, 13, 14, 15, 16, 17, 18)   # 8
)

# Key Mappings
KEY_CCS = [
    90,91,92,
    93,94,95,
    96,97,98,
    99,100,101
]

# Should the keys send 0 velocity values?
KEY_TOGGLES = [
    0, 0, 0,
    0, 0, 0,
    1, 1, 0,
    0, 0, 0
]

KEY_COLORS = [
    LP_COLORS[5], LP_COLORS[64], LP_COLORS[87],
    0, LP_COLORS[97], 0,
    LP_COLORS[56], LP_COLORS[56], LP_COLORS[112],
    LP_COLORS[5], LP_COLORS[13], LP_COLORS[79]
]

MODIFIER_NOTES = [41, 42, 43, 41, 42, 43, 41, 42, 43, 41, 42, 43]  # blank row in Live

# MacroPad Display Settings
WIDTH = 128
HEIGHT = 64
