#!/usr/bin/env python3

from setup import list1, list2


similarity_score = 0

for element in list1:
	found = list2.count( element )
	score = int( element ) * found
	similarity_score += score

print( f"Part 2: total similarity: {similarity_score}" )
