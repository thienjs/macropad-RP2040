# MACROPAD Hotkeys: VSCode

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                    # REQUIRED dict, must be named 'app'
    'name' : 'VS Code',    # Application name
    'macros' : [           # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x0000FF, 'Search', [Keycode.CONTROL, Keycode.F]),
        (0x0000FF, 'CLI', [Keycode.CONTROL, Keycode.GRAVE_ACCENT]),
        (0x0000FF, 'CP', [Keycode.CONTROL, Keycode.SHIFT, Keycode.P]),
        # 2nd row ----------
        (0x0000FF, 'Cut', [Keycode.CONTROL, Keycode.X]),
        (0x0000FF, 'Copy',[Keycode.CONTROL, Keycode.C]),
        (0x0000FF, 'Paste', [Keycode.CONTROL, Keycode.V]),
        # 3rd row ----------
        (0x0000FF, 'Line', [Keycode.CONTROL, Keycode.L]),
        (0x0000FF, 'up', [Keycode.UP_ARROW]),
        (0x0000FF, 'Close', [Keycode.CONTROL, Keycode.SHIFT, Keycode.W]),
        # 4th row ----------
        (0x101010, '<', [Keycode.CONTROL, Keycode.PAGE_DOWN]),
        (0x800000, 'down', [Keycode.ZERO]),
        (0x101010, '>', [Keycode.CONTROL, Keycode.PAGE_DOWN]),
        # Encoder button ---
        (0x000000, '', [Keycode.CONTROL, Keycode.P])
    ]
}