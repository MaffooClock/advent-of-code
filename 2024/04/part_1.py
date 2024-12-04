#!/usr/bin/env python3
## -*- coding: utf-8 -*-

from setup import *


DIRECTIONS = [
    # right    # left
    (  1, 0 ), ( -1,  0 ),
    # up       # down
    (  0, 1 ), (  0, -1 ),
    # up-right # down-right
    (  1, 1 ), (  1, -1 ),
    # up-left  # down-left
    ( -1, 1 ), ( -1, -1 )
]


def count_word_at_cell( directions: list, grid: list, x: int, y: int, word: str ) -> list:
        
    current_cell = grid[x][y]
    first_letter = word[0]
    word_length = len( word )

    found = []

    if current_cell != first_letter:
        # the word doesn't begin here
        return found

    # see if the whole word is in any direction from the current cell
    for dir_x, dir_y in directions:
        
        # coordinates for the next cell in the current direction
        next_x = x + dir_x
        next_y = y + dir_y

        # start at the second letter in the word (we already matched the first letter)
        next_i = 1

        while next_i < word_length:
            next_letter = word[next_i]

            # make sure the cell has the current letter in the word
            if not is_letter_in_cell( grid, next_x, next_y, next_letter ):
                break

            # advance to the next cell in the same direction...
            next_x += dir_x
            next_y += dir_y

            # ...and the next character in the word
            next_i += 1

        # if we made it through every character in the word
        # without breaking out of the `while` loop early,
        # then add the cell coordinates to the list
        if next_i == word_length:
            found.append( [ x, y ] )

    return found


def word_search( grid: list, word: str ) -> int:
    
    rows = len( grid )
    columns = len( grid[0] )

    found = 0

    for ri in range( rows ):
        for ci in range( columns ):
            found += len( count_word_at_cell( DIRECTIONS, grid, ri, ci, word ) )

    return found


def test():
    test_grids = [
        [   # 2
            [ 'X', 'M', 'A', 'S', 'A', 'M', 'X' ],
            [ ' ', ' ', ' ', ' ', ' ', ' ', ' ' ],
            [ ' ', ' ', ' ', ' ', ' ', ' ', ' ' ],
            [ ' ', ' ', ' ', ' ', ' ', ' ', ' ' ],
            [ ' ', ' ', ' ', ' ', ' ', ' ', ' ' ],
            [ ' ', ' ', ' ', ' ', ' ', ' ', ' ' ],
            [ ' ', ' ', ' ', ' ', ' ', ' ', ' ' ],
        ],
        [   # 3
            [ 'X', 'M', 'A', 'S', 'A', 'M', 'X' ],
            [ ' ', ' ', ' ', 'A', ' ', ' ', ' ' ],
            [ ' ', ' ', ' ', 'M', ' ', ' ', ' ' ],
            [ ' ', ' ', ' ', 'X', ' ', ' ', ' ' ],
            [ ' ', ' ', ' ', ' ', ' ', ' ', ' ' ],
            [ ' ', ' ', ' ', ' ', ' ', ' ', ' ' ],
            [ ' ', ' ', ' ', ' ', ' ', ' ', ' ' ],
        ],
        [   # 4
            [ ' ', ' ', ' ', 'S', ' ', ' ', ' ' ],
            [ ' ', ' ', ' ', 'A', ' ', ' ', ' ' ],
            [ ' ', ' ', ' ', 'M', ' ', ' ', ' ' ],
            [ 'S', 'A', 'M', 'X', 'M', 'A', 'S' ],
            [ ' ', ' ', ' ', 'M', ' ', ' ', ' ' ],
            [ ' ', ' ', ' ', 'A', ' ', ' ', ' ' ],
            [ ' ', ' ', ' ', 'S', ' ', ' ', ' ' ],
        ],
        [   # 8
            [ 'S', ' ', ' ', 'S', ' ', ' ', 'S' ],
            [ ' ', 'A', ' ', 'A', ' ', 'A', ' ' ],
            [ ' ', ' ', 'M', 'M', 'M', ' ', ' ' ],
            [ 'S', 'A', 'M', 'X', 'M', 'A', 'S' ],
            [ ' ', ' ', 'M', 'M', 'M', ' ', ' ' ],
            [ ' ', 'A', ' ', 'A', ' ', 'A', ' ' ],
            [ 'S', ' ', ' ', 'S', ' ', ' ', 'S' ],
        ]
    ]

    for i, grid in enumerate( test_grids ):
        found = word_search( grid, 'XMAS' )
        print( f"Test {i+1}: {found}" )


def main():
    grid = list()
    for line in input.splitlines():
        grid.append( list( line ) )

    found = word_search( grid, 'XMAS' )
    print( f"Part 1: {found}" )

# test()
main()
