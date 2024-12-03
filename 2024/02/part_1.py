#!/usr/bin/env python3

from setup import data, check_levels, DEBUG


safe_reports   = 0
unsafe_reports = 0

for i, report in enumerate( data ):
	levels = report.split( " " )

	if DEBUG:
		print( f"{i+1}: {report}" )

	failed = check_levels( levels )

	if not failed:
		if DEBUG:
			print( "ok" )
		safe_reports += 1
	else:
		if DEBUG:
			print( "fail" )
		unsafe_reports += 1

	if DEBUG:
		print()

print( 'Part 1:' )
print( f"Safe reports:   {safe_reports}" )
print( f"Unsafe reports: {unsafe_reports}" )
