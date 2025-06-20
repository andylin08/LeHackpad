from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.keys import KC
from kmk.extensions.rgb import RGB
from kmk.rgb import AnimationModes

keyboard = KMKKeyboard()

# SW1 to 1, SW2 to 2, SW3 to 4, SW4 to 3
keyboard.col_pins = (1, 2, 4, 3)
keyboard.row_pins = (0,)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Map to arrow keys
keyboard.keymap = [
    [KC.UP, KC.LEFT, KC.DOWN, KC.RIGHT]
]

# RGB on GPIO6 (Pin 5)
rgb_ext = RGB(
    pixel_pin=6,
    num_pixels=2,
    animation_mode=AnimationModes.SOLID,
    hue_default=180,
    sat_default=255,
    val_default=50,
)
keyboard.extensions.append(rgb_ext)

if __name__ == '__main__':
    keyboard.go()
