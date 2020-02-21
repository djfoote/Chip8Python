import json
import os
import sys

import pygame

MAPPINGS_FILENAME = 'button_mappings.json'


class Gamepad:
	def __init__(self):
		self.initialized = init_joysticks()
		if self.initialized:
			self.joystick = pygame.joystick.Joystick(0)
			self.num_buttons = self.joystick.get_numbuttons()
		self.button_mappings = get_button_mappings()

	def __bool__(self):
		return self.initialized

	def get_keys(self):
		if not self:
			return []

		pressed_keys = []
		for key, mapped_button in self.button_mappings.items():
			if mapped_button < self.num_buttons and self.joystick.get_button(
					mapped_button):
				pressed_keys.append(int(key))
		return pressed_keys

	def is_key_pressed(self, key):
		if not self:
			return False

		mapped_button = self.button_mappings[str(key)]
		return mapped_button < self.num_buttons and self.joystick.get_button(
				mapped_button)

	def wait_for_keypress(self):
		if not self:
			raise RuntimeError(
					'Waiting for button press but there is no gamepad connected.')

		while True:
			keys = self.get_keys()
			if keys:
				return keys[0]


def init_joysticks(require=False):
	pygame.init()
	pygame.joystick.init()

	joystick_count = pygame.joystick.get_count()
	if joystick_count:
		print(f'{joystick_count} joysticks connected.')
		joystick = pygame.joystick.Joystick(0)
		print(f'Will use the first one, {joystick.get_name()}')
		joystick.init()
		return True
	elif require:
		print('No joysticks connected. Connect one and rerun.')
		sys.exit()
	return False


def get_mappings_filepath():
	dir_path = os.path.dirname(os.path.realpath(__file__))
	return os.path.join(dir_path, MAPPINGS_FILENAME)


def get_button_mappings():
	with open(get_mappings_filepath(), 'r') as f:
		return json.load(f)


def write_button_mappings(mappings_dict):
	with open(get_mappings_filepath(), 'w') as f:
		json.dump(mappings_dict, f)


def get_button():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.JOYBUTTONDOWN:
				return event.dict['button']