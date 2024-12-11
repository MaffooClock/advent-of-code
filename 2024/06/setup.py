## -*- coding: utf-8 -*-

from __future__ import annotations
import sys


DEBUG = False

UP    = '^'
RIGHT = '>'
DOWN  = 'v'
LEFT  = '<'
DIRECTIONS = [ UP, RIGHT, DOWN, LEFT ]


with open( sys.path[0] + '/input.txt' ) as f:
    the_map = f.read().splitlines()


def rows() -> int:
    return len( the_map )


def columns() -> int:
    return len( the_map[0] )


def max_x() -> int:
    return columns() - 1


def max_y() -> int:
    return rows() - 1


def get_guard_position() -> tuple[ int, int, str ]:
    for y, row in enumerate( the_map ):
        for facing in DIRECTIONS:
            x = row.find( facing )
            if x > -1:
                return x, y, facing


def can_move_to( x, y ) -> bool:
    try:
        return the_map[y][x] != '#'
    except IndexError:
        return False


def can_move_up() -> bool:
    x, y, facing = get_guard_position()
    return can_move_to( x, y-1 )


def can_move_right() -> bool:
    x, y, facing = get_guard_position()
    return can_move_to( x+1, y )


def can_move_down() -> bool:
    x, y, facing = get_guard_position()
    return can_move_to( x, y+1 )


def can_move_left() -> bool:
    x, y, facing = get_guard_position()
    return can_move_to( x-1, y )


def is_at_edge() -> bool:
    x, y, facing = get_guard_position()
    return x == 0 or x == max_x() or y == 0 or y == max_y()


def mark_position( x: int, y: int ) -> bool:
    if the_map[y][x] == '#':
        return False
    row = the_map[y]
    row = row[:x] + 'X' + row[x + 1:]
    the_map[y] = row
    return True


def move_to( x: int, y: int, d: str ) -> bool:
    if the_map[y][x] == '#':
        return False
    row = the_map[y]
    row = row[:x] + d + row[x + 1:]
    the_map[y] = row
    return True


def count_positions() -> int:
    positions = 1
    for row in the_map:
        positions += row.count( 'X' )
    return positions


def dump_map() -> None:
    for row in the_map:
        print( row )
