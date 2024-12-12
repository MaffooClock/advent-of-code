#!/usr/bin/env python3
## -*- coding: utf-8 -*-

from __future__ import annotations

from setup import *


total_calibration = evaluate_equations( [ ADD, MULTIPLY ] )
print( f"Part 1: {total_calibration}" )
