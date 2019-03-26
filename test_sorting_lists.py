#
#   Tests for sorting list functions
#

import pytest
from sorting_lists import insertion_sort, bubble_sort, selection_sort, merge_sort

def test_insertion_sort_1():
    ulist = [3,2,1]
    assert insertion_sort(ulist) == [1,2,3]

def test_insertion_sort_2():
    ulist = [1,4,5,9,2,15,0]
    assert insertion_sort(ulist) == [0,1,2,4,5,9,15]

def test_insertion_sort_3():
    ulist = [21,9,-1,4]
    assert insertion_sort(ulist) == [-1,4,9,21]


def test_bubble_sort_1():
    pass

def test_bubble_sort_2():
    pass

def test_bubble_sort_3():
    pass


def test_selection_sort_1():
    pass

def test_selection_sort_2():
    pass

def test_selection_sort_3():
    pass


def test_merge_sort_1():
    pass

def test_merge_sort_2():
    pass

def test_merge_sort_3():
    pass