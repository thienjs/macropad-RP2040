# MACROPAD Hotkeys: Windows

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                    # REQUIRED dict, must be named 'app'
    'name' : 'Windows',    # Application name
    'macros' : [           # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x0000FF, 'Search', [Keycode.CONTROL, Keycode.F]),
        (0x0000FF, 'CLI', [Keycode.WINDOWS, Keycode.R], 'cmd', Keycode.RETURN),
        (0x0000FF, 'Desktop', [Keycode.WINDOWS, Keycode.D]),
        # 2nd row ----------
        (0x0000FF, 'Cut', [Keycode.CONTROL, Keycode.X]),
        (0x0000FF, 'Copy',[Keycode.CONTROL, Keycode.C]),
        (0x0000FF, 'Paste', [Keycode.CONTROL, Keycode.V]),
        # 3rd row ----------
        (0x0000FF, 'Line', [Keycode.ALT, Keycode.TAB]),
        (0x0000FF, '^', [Keycode.UP_ARROW]),
        (0x0000FF, 'Close', [Keycode.CONTROL, Keycode.F4]),
        # 4th row ----------
        (0x101010, '<', [Keycode.LEFT_ARROW]),
        (0x800000, 'down', [Keycode.DOWN_ARROW]),
        (0x101010, '>', [Keycode.RIGHT_ARROW]),
        # Encoder button ---
        (0x000000, '', [Keycode.WINDOWS, Keycode.L])
    ]
}