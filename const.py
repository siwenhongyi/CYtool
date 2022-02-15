# encoding=utf-8
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


class ButtonImage:
	"""
	game button pic file path, use it to find button position and click it
	"""
	hard = r'images/hard.png'
	barrier_105 = r'images/barrier_105.png'
	confirm_start = r'images/confirm_start.png'
	confirm_end = r'images/confirm_end.png'
	hp = r'images/hp.png'


class AllTimeDelay:
	"""
	Unit second
	"""
	comm_delay = 1
	fight_delay = 50
	end_delay = 2

