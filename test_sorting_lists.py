#
#   Tests for sorting list functions
#

import pytest
from sorting_lists import insertion_sort, bubble_sort, selection_sort, merge_sort, merge_sorted_lists

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
    ulist = [3,2,1]
    assert bubble_sort(ulist) == [1,2,3]

def test_bubble_sort_2():
    ulist = [1,4,5,9,2,15,0]
    assert bubble_sort(ulist) == [0,1,2,4,5,9,15]

def test_bubble_sort_3():
    ulist = [21,9,-1,4]
    assert bubble_sort(ulist) == [-1,4,9,21]


def test_selection_sort_1():
    ulist = [3,2,1]
    assert selection_sort(ulist) == [1,2,3]

def test_selection_sort_2():
    ulist = [1,4,5,9,2,15,0]
    assert selection_sort(ulist) == [0,1,2,4,5,9,15]

def test_selection_sort_3():
    ulist = [21,9,-1,4]
    assert selection_sort(ulist) == [-1,4,9,21]


def test_merge_sort_1():
    ulist = [3,2,1]
    assert merge_sort(ulist) == [1,2,3]

def test_merge_sort_2():
    ulist = [1,4,5,9,2,15,0]
    assert merge_sort(ulist) == [0,1,2,4,5,9,15]

def test_merge_sort_3():
    ulist = [21,9,-1,4]
    assert merge_sort(ulist) == [-1,4,9,21]


def test_merge_sorted_lists_1():
    list1 = [1,3,5]
    list2 = [0,2,4,6]
    assert merge_sorted_lists(list1,list2) == [0,1,2,3,4,5,6]

def test_merge_sorted_lists_2():
    list1 = [5,9,10]
    list2 = [0,2,4,6,8,9]
    assert merge_sorted_lists(list1,list2) == [0,2,4,5,6,8,9,9,10]
