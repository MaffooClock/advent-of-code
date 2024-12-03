#!/usr/bin/env python3

from setup import data, check_levels, DEBUG


safe_reports   = 0
unsafe_reports = 0

for i, report in enumerate( data ):
	levels = report.split( " " )

	if DEBUG:
		print( f"{i+1}: {report}" )

	safe = True
	failed = check_levels( levels )

	if failed:
		safe = False
		for i, level in enumerate( levels ):
			_levels = levels.copy()
			_levels.pop( i )
			_failed = check_levels( _levels )
			if not _failed:
				safe = True

	if safe:
		if DEBUG:
			print( "ok" )
		safe_reports += 1
	else:
		if DEBUG:
			print( "fail" )
		unsafe_reports += 1

	if DEBUG:
		print()

print( 'Part 2:' )
print( f"Safe reports:   {safe_reports}" )
print( f"Unsafe reports: {unsafe_reports}" )
