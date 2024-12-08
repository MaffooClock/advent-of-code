#!/usr/bin/env python3
## -*- coding: utf-8 -*-

from __future__ import annotations
from setup import *


invalid_updates = list()
for pages in page_updates:

    rules = get_applicable_rules( pages )
    rule_count = len( rules )
    pass_count = 0

    if DEBUG:
        print( pages )

    # check every applicable rule and count how many pass
    for rule in rules:
        valid = is_valid_update( pages, rule )

        if DEBUG:
            print( "\t", rule, '' if valid else '-> INVALID' )
        
        if valid:
            pass_count += 1

    # if all rules pass, then skip to the next list of updates
    if pass_count == rule_count:
        continue

    if DEBUG:
        print( f"VALID: {pages}" )
        print()

    invalid_updates.append( pages )



fixed_updates = list()

for pages in invalid_updates:
    pages = pages.split( ',' )
    rules = get_applicable_rules( pages )
    valid = False

    while not valid:
        # check every applicable rule...
        for rule in rules:
            a, b = rule.split( '|' )
            ai = pages.index( a )
            bi = pages.index( b )

            # ...and move the second in front of the first to make the rule pass...
            if ai > bi:
                pages.insert( ai, pages.pop( bi ) )

        # ...then check the whole list to see if it's now valid
        # (repeat the above if not)
        valid = updates_are_valid( pages, rules )

    fixed_updates.append( pages )


middle_sum = get_middle_sum( fixed_updates )
print( f"Part 2: {middle_sum}" )
