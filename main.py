# encoding = utf-8
from datetime import datetime
from typing import (
	IO,
	Any
)

import helper

log_file: IO[Any] = open(r'CY.log', mode='a', encoding='utf-8')


def prep_init() -> None:
	global log_file
	if log_file is None:
		log_file = open(r'CY.log', mode='a', encoding='utf-8')
	log_file.write(f'{datetime.now()}\n')


def write_log(format_str: str, *args, **kwargs) -> None:
	pass


if __name__ == '__main__':
	prep_init()
	print('start')
	# todo start button
	hp_value = helper.get_hp_value()
	while hp_value:
		hp_value -= 1
		if hp_value < 5:
			hp_value = helper.get_hp_value()
	log_file.close()

