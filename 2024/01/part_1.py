#!/usr/bin/env python3

from setup import list1, list2


total_distance = 0

for i in range( 0, max( len( list1 ), len( list2 ) ) ):
	total_distance += abs( int( list1[i] ) - int( list2[i] ) )

print( f"Part 1: total distance: {total_distance}" )
