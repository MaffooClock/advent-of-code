#!/usr/bin/env python3
## -*- coding: utf-8 -*-

from __future__ import annotations

from setup import *


total_calibration = evaluate_equations( [ ADD, MULTIPLY, CONCAT ] )
print( f"Part 2: {total_calibration}" )
