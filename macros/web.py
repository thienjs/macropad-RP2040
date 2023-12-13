# SPDX-FileCopyrightText: 2021 Phillip Burgess for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys example: Microsoft Edge web browser for Windows

from adafruit_hid.keycode import Keycode  # REQUIRED if using Keycode.* values

app = {                      # REQUIRED dict, must be named 'app'
    'name': 'Chrome',  # Application name
    'macros': [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x004000, '< Back', [Keycode.ALT, Keycode.LEFT_ARROW]), #Back
        (0x004000, 'Fwd >', [Keycode.ALT, Keycode.RIGHT_ARROW]), #Forward
        (0x400000, 'New', [Keycode.CONTROL, 'n']),    #New Window
        # 2nd row ----------
        (0x101010, 'Dev', [Keycode.CONTROL, Keycode.SHIFT, "I"]),  # Dev tools
        (0x000040, 'Reload', [Keycode.CONTROL, 'r']), #reload
        (0x000040, 'Private', [Keycode.CONTROL, 'N']), #new private window
        # 3rd row ----------
        (0x400000, 'Tab', [Keycode.CONTROL, 't']),  # New Tab               
        (0x000000, 'Last', [Keycode.CONTROL, "9"]), #last tab
        (0x800000, 'Close', [Keycode.CONTROL, "w"]), # Close Tab
        # 4th row ----------
        (0x000000, 'Prev', [Keycode.CONTROL, Keycode.SHIFT, Keycode.TAB]),
        (0x800000, 'Min', [Keycode.ALT, Keycode.SPACE, "n"]), # Minimize window
        (0x000000, 'Next', [Keycode.CONTROL, Keycode.TAB, ]), #next tab
        # Encoder button ---
        (0x800000, 'CloseWin', [Keycode.CONTROL, Keycode.SHIFT, "w"]),  # Close window
    ]
}
