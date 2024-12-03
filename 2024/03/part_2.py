#!/usr/bin/env python3
## -*- coding: utf-8 -*-

import re
from setup import memory


segments = re.split( r"do\(\)", memory )

mul_sum = 0

for segment in segments:
	do_and_dont = re.split( r"don't\(\)", segment )
	
	do = do_and_dont[0]

	matches = re.findall( r"mul\((\d+),(\d+)\)", do )

	for match in matches:
		a = int( match[0] )
		b = int( match[1] )
		mul_sum += a * b

print( f"Part 2: {mul_sum}" )
