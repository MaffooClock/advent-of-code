## -*- coding: utf-8 -*-

from __future__ import annotations
import sys


DEBUG = False

with open( sys.path[0] + '/input_rules.txt' ) as f:
    page_rules = f.read().splitlines()

with open( sys.path[0] + '/input_updates.txt' ) as f:
    page_updates = f.read().splitlines()


def get_applicable_rules( pages: str|list ) -> list | False:
    """ sift through all page ordering rules and find the ones matching pages numbers in a given list of updates
    """
    rules = list()

    if type( pages ) is str:
        pages = pages.split( ',' )

    for rule in page_rules:
        a, b = rule.split( '|' )
        if a in pages and b in pages:
            rules.append( rule )
    
    return rules or False


def updates_are_valid( pages: str|list, rules=list() ) -> bool:
    """ check if a given list of page updates passes all applicable page ordering rules
    """
    if type( pages ) is str:
        pages = pages.split( ',' )

    if not rules:
        rules = get_applicable_rules( pages )
    rule_count = len( rules )

    if not rule_count:
        return False

    pass_count = 0

    if DEBUG:
        print( pages )

    for rule in rules:
        valid = is_valid_update( pages, rule )

        if DEBUG:
            print( "\t", rule, '-> VALID' if valid else '' )
        
        if valid:
            pass_count += 1

    return pass_count == rule_count


def is_valid_update( pages: str|list, rule: str ) -> bool:
    """ check if a list of page updates passes a specific page ordering rule
    """
    if type( pages ) is str:
        pages = pages.split( ',' )
    a, b = rule.split( '|' )
    return pages.index( a ) < pages.index( b )


def get_middle_page( pages: str|list ) -> int:
    """ get the middle element of a list (assumes odd quantity of elements)
    """
    if type( pages ) is str:
        pages = pages.split( ',' )
    pages_length = len( pages )
    middle = pages_length // 2
    return int( pages[middle] )


def get_middle_sum( updates: list ) -> int:
    """ sum the middle elements in a list of lists
    """
    middle_sum = 0
    for update in updates:
        middle_sum += get_middle_page( update )
    return middle_sum
    

__all__ = [
    'DEBUG',
    'page_updates',
    'get_applicable_rules',
    'updates_are_valid',
    'is_valid_update',
    'get_middle_page',
    'get_middle_sum'
]
