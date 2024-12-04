#!/usr/bin/env python3
## -*- coding: utf-8 -*-

from setup import *

"""
    This one got kinda shitty, as the `x_search()` function isn't re-usable.

    The right way to do it would be to pass in a word and the index where the cross-point
    should be, then at each diagonal cell around that cross-point character, keep traversing
    in that direction to find either the first or last slice of the word around that center
    character, with each slice being found exactly twice.
    
    But I got tired of messing with this, so I just hard-coded the characters -- thank
    Aunt Jemima that the puzzle only wanted a three-letter word, so I had to traverse
    only one cell in each direction.
"""


def find_x_cells( grid: list, letter: str ) -> list:
    matches = []

    rows = len( grid )
    columns = len( grid[0] )
    
    # make a list of coordinates for every cell containing the letter we're looking for
    for ri in range( rows ):
        for ci in range( columns ):
            if is_letter_in_cell( grid, ri, ci, letter ):
                matches.append( [ ri, ci ] )
    
    return matches


def x_search( grid: list ) -> int:
    
    found = 0
                
    # with each cell containing 'a'...
    for center_coords in find_x_cells( grid, 'A' ):
        x, y = center_coords

        # calculate coordinates for diagonally adjacent cells
        up    = x + 1
        down  = x - 1
        left  = y - 1
        right = y + 1

        # ensure all four diagonal cells around the 'A' cell exist within the bounds of the grid
        if not (
            cell_exists(   up,  left, grid ) and
            cell_exists(   up, right, grid ) and
            cell_exists( down,  left, grid ) and
            cell_exists( down, right, grid )
        ): continue

        # make a mini grid of the four diagonal cells for easier comparison
        sub_grid = [
            [ grid[up][left], grid[up][right] ],
            [ grid[down][left], grid[down][right] ]
        ]
        
        # check each mini grid for each of the four possible X-MAS arrangements
        if (
            (                                       # S.S
                ''.join( sub_grid[0] ) == 'SS' and  # .A.
                ''.join( sub_grid[1] ) == 'MM'      # M.M
            ) or
            (                                       # M.M
                ''.join( sub_grid[0] ) == 'MM' and  # .A.
                ''.join( sub_grid[1] ) == 'SS'      # S.S
            ) or
            (                                       # S.M
                ''.join( sub_grid[0] ) == 'SM' and  # .A.
                ''.join( sub_grid[1] ) == 'SM'      # S.M
            ) or
            (                                       # M.S
                ''.join( sub_grid[0] ) == 'MS' and  # .A.
                ''.join( sub_grid[1] ) == 'MS'      # M.S
            )
        ): found += 1

    return found


def test():
    test_grids = [
        [   # 1
            [ ' ', ' ', ' ', ' ', ' ', ' ', ' ' ],
            [ ' ', ' ', ' ', ' ', ' ', ' ', ' ' ],
            [ ' ', ' ', 'M', ' ', 'S', ' ', ' ' ],
            [ ' ', ' ', ' ', 'A', ' ', ' ', ' ' ],
            [ ' ', ' ', 'M', ' ', 'S', ' ', ' ' ],
            [ ' ', ' ', ' ', ' ', ' ', ' ', ' ' ],
            [ ' ', ' ', ' ', ' ', ' ', ' ', ' ' ],
        ],
        [   # 1
            [ 'M', ' ', ' ', ' ', 'M', ' ', ' ' ],
            [ ' ', 'A', ' ', 'A', ' ', ' ', ' ' ],
            [ ' ', ' ', 'S', ' ', ' ', ' ', ' ' ],
            [ ' ', ' ', ' ', 'A', ' ', ' ', ' ' ],
            [ ' ', ' ', ' ', ' ', 'M', ' ', 'S' ],
            [ ' ', ' ', ' ', ' ', ' ', 'A', ' ' ],
            [ ' ', ' ', ' ', ' ', 'M', ' ', 'S' ],
        ],
        [   # 3
            [ 'M', ' ', 'M', ' ', 'M', ' ', ' ' ],
            [ ' ', 'A', ' ', 'A', ' ', ' ', ' ' ],
            [ 'S', ' ', 'S', ' ', 'S', ' ', ' ' ],
            [ ' ', ' ', ' ', 'A', ' ', ' ', ' ' ],
            [ ' ', ' ', ' ', ' ', 'M', ' ', 'S' ],
            [ ' ', ' ', ' ', ' ', ' ', 'A', ' ' ],
            [ ' ', ' ', ' ', ' ', 'M', ' ', 'S' ],
        ],
        [   # 4
            [ 'M', ' ', 'M', ' ', 'M', ' ', ' ' ],
            [ ' ', 'A', ' ', 'A', ' ', ' ', ' ' ],
            [ 'S', ' ', 'S', ' ', 'S', ' ', 'S' ],
            [ ' ', 'A', ' ', 'A', ' ', 'A', ' ' ],
            [ ' ', ' ', 'M', ' ', 'M', ' ', 'S' ],
            [ ' ', ' ', ' ', ' ', ' ', 'A', ' ' ],
            [ ' ', ' ', ' ', ' ', 'M', ' ', 'S' ],
        ],
        [   # 9
            [ ' ', 'M', ' ', 'S', ' ', ' ', ' ', ' ', ' ', ' ' ], 
            [ ' ', ' ', 'A', ' ', ' ', 'M', 'S', 'M', 'S', ' ' ], 
            [ ' ', 'M', ' ', 'S', ' ', 'M', 'A', 'A', ' ', ' ' ],
            [ ' ', ' ', 'A', ' ', 'A', 'S', 'M', 'S', 'M', ' ' ], 
            [ ' ', 'M', ' ', 'S', ' ', 'M', ' ', ' ', ' ', ' ' ], 
            [ ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ], 
            [ 'S', ' ', 'S', ' ', 'S', ' ', 'S', ' ', 'S', ' ' ], 
            [ ' ', 'A', ' ', 'A', ' ', 'A', ' ', 'A', ' ', ' ' ], 
            [ 'M', ' ', 'M', ' ', 'M', ' ', 'M', ' ', 'M', ' ' ], 
            [ ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ], 
        ]
    ]

    for i, grid in enumerate( test_grids ):
        found = x_search( grid )
        print( f"Test {i+1}: {found}" )


def main():
    grid = list()
    for line in input.splitlines():
        grid.append( list( line ) )

    found = x_search( grid )
    print( f"Part 2: {found}" )


# test()
main()
