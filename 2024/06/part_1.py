#!/usr/bin/env python3
## -*- coding: utf-8 -*-

from __future__ import annotations

from setup import *

# starting position
X, Y, D = get_guard_position()
EDGE = is_at_edge()

while not EDGE:
    
    moved = False
    current_position = X, Y

    while not moved:
        if D == UP:
            if can_move_up():
                Y -= 1
                moved = True
            else:
                D = RIGHT
            
        elif D == RIGHT:
            if can_move_right():
                X += 1
                moved = True
            else:
                D = DOWN
            
        elif D == DOWN:
            if can_move_down():
                Y += 1
                moved = True
            else:
                D = LEFT
            
        elif D == LEFT:
            if can_move_left():
                X -= 1
                moved = True
            else:
                D = UP
    

    mark_position( *current_position )
    move_to( X, Y, D )

    EDGE = is_at_edge()


moves = count_positions()
print( f"Part 1: {moves}" )

if DEBUG:
    dump_map()
