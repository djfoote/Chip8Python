import gamepad_utils

default = {i: i for i in range(0x10)}
gamepad_utils.write_button_mappings(default)