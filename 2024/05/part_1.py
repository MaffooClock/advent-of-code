#!/usr/bin/env python3
## -*- coding: utf-8 -*-

from __future__ import annotations
from setup import *


valid_updates = list()
for pages in page_updates:
        
    if not updates_are_valid( pages ):
        continue

    if DEBUG:
        print( f"VALID: {pages}" )
        print()

    valid_updates.append( pages )


middle_sum = get_middle_sum( valid_updates )

print( f"Part 1: {middle_sum}" )
