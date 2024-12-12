## -*- coding: utf-8 -*-

from __future__ import annotations
import sys
import itertools


DEBUG = False

ADD      = '+'
MULTIPLY = '*'
CONCAT   = '||'


with open( sys.path[0] + '/input.txt' ) as f:
    equations = f.read().splitlines()


def left_to_right( operands: list, operators: tuple ) -> tuple[ int, str ]:
    result = operands[0]
    expression = [ str( operands[0] ) ]

    for value, operator in zip( operands[1:], operators ):
        expression.extend( [ operator, str( value ) ] )

        if operator == ADD:
            result += value

        elif operator == MULTIPLY:
            result *= value

        elif operator == CONCAT:
            result = int( f"{result}{value}" )

    expression = ' '.join( expression )
    return result, expression


def evaluate_equations( operators: list[ str ] ) -> int:
    total_calibration = 0

    for i in range( len( equations ) ):
        answer, operands = get_equation( i )
        operand_count = len( operands )
        operator_count = operand_count - 1

        success = False

        # based on the number of operands, generate a list of all possible
        # combinations of addition and multiplication between each one...
        for _operators in itertools.product( operators, repeat=operator_count ):

            # ...then do the math
            result, expression = left_to_right( operands, _operators )
            if result == answer:
                success = True
                total_calibration += result
                if DEBUG:
                    print( f"PASS: {expression} -> {result} == {answer}" )
                break

        if not success:
            if DEBUG:
                print( f"FAIL: {operands} cannot evaluate to {answer}" )

    return total_calibration


def get_equation( i: int ) -> tuple[ int, list ]:
    equation = equations[i].split( sep=':', maxsplit=1 )
    answer = int( equation[0] )
    operands = list( map( int, equation[1].split() ) )
    return answer, operands

__all__ = [
    'DEBUG',
    'ADD', 'MULTIPLY', 'CONCAT',
    'evaluate_equations'
]
