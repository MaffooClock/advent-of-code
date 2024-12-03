## -*- coding: utf-8 -*-

import sys


with open( sys.path[0] + '/list1.txt' ) as f:
    list1 = f.read().splitlines()
    list1.sort()

with open( sys.path[0] + '/list2.txt' ) as f:
    list2 = f.read().splitlines()
    list2.sort()