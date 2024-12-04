## -*- coding: utf-8 -*-

import sys


with open( sys.path[0] + '/input.txt' ) as f:
    input = f.read()


def cell_exists( x: int, y: int, grid: list ) -> bool:
    return 0 <= x < len( grid ) and 0 <= y < len( grid[x] )


def is_letter_in_cell( grid: list, x: int, y: int, letter: str ) -> bool:
    return cell_exists( x, y, grid ) and grid[x][y] == letter


__all__ = [
    'input',
    'cell_exists',
    'is_letter_in_cell'
]
