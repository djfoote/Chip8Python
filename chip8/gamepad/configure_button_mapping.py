import gamepad_utils


def key_to_number(key):
	number = int(key, 16)
	if number < 0 or number > 0xF:
		raise ValueError
	return number


if __name__ == '__main__':
	gamepad_utils.init_joysticks(require=True)
	mappings_dict = gamepad_utils.get_button_mappings()

	print('Chip8 has 16 buttons, 0x0 to 0xF')
	while True:
		print('Type 0-F and press enter to specify which Chip8 key to map.')
		entered_key = input()
		try:
			entered_number = key_to_number(entered_key)
		except ValueError:
			print('Invalid choice')
			continue

		button = gamepad_utils.get_button()

		mappings_dict.update({entered_number: button})
		gamepad_utils.write_button_mappings(mappings_dict)
		print(f'0x{entered_key} mapped to button {button}')
