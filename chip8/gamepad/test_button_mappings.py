import pygame

import gamepad_utils


gamepad_utils.init_joysticks(require=True)
button_mappings = gamepad_utils.get_button_mappings()
while True:
	button = gamepad_utils.get_button()
	for key, button_number in button_mappings.items():
		if button == button_number:
			print(hex(int(key)))