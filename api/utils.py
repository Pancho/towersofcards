import math


def get_int_distance_ceil(x1, x2, y1, y2):
	return int(math.ceil(math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))))


def get_int_distance_floor(x1, x2, y1, y2):
	return int(math.floor(math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))))


def get_distance_ceil(x1, x2, y1, y2):
	return math.ceil(math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2)))


def get_distance_floor(x1, x2, y1, y2):
	return math.floor(math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2)))


def get_distance_round(x1, x2, y1, y2):
	return round(math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2)))


def get_real_distance(x1, x2, y1, y2):
	return math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))


def get_manhattan_distance(x1, x2, y1, y2):
	return abs(x1 - x2) + abs(y1 - y2)


def field_in_field_list(coord, list_to_check):
	for field in list_to_check:
		if field[0] == coord:
			return True
	return False