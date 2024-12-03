## -*- coding: utf-8 -*-


import sys

DEBUG = False


with open( sys.path[0] + '/input.txt' ) as f:
    data = f.read().splitlines()


def check_levels( levels ):
	previous_level = None
	direction = None

	failed = []

	for i, current_level in enumerate( levels ):
		current_level = int( current_level )

		if previous_level is None:
			previous_level = current_level
			continue

		_direction = 0
		if current_level > previous_level:
			_direction = 1
		elif current_level < previous_level:
			_direction = -1

		if _direction:

			if direction is None:
				direction = _direction

			if direction != _direction:
				if DEBUG:
					print( f"direction was {direction}, now {_direction}" )
				failed.append( i )

			diff = abs( current_level - previous_level )
			if diff > 3:
				if DEBUG:
					print( f"diff between {previous_level} and {current_level} is {diff}" )
				failed.append( i )

		else:
			if DEBUG:
					print( f"repeating value {previous_level}" )
			failed.append( i )

		previous_level = current_level

	return failed