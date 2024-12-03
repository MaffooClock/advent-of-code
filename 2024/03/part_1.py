#!/usr/bin/env python3
## -*- coding: utf-8 -*-

import re
from setup import memory


matches = re.findall( r"mul\((\d+),(\d+)\)", memory )

mul_sum = 0

for match in matches:
	a = int( match[0] )
	b = int( match[1] )
	mul_sum += a * b

print( f"Part 1: {mul_sum}" )
