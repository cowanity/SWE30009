import pytest
from assignment2 import split_and_sort

def test_case_1():
    input_list = [3, 10, 9, 20, 16, 10, 9, 15, 7, 5, 28, 20, 5, 8, 20]
    expected_output = ([3, 5, 7, 9, 15], [8, 10, 16, 20, 28])
    assert split_and_sort(input_list) == expected_output

def test_case_2():
    input_list = [13, 7, 9, 15, 21, 5, 3]
    expected_output = ([3, 5, 7, 9, 13, 15, 21], [])
    assert split_and_sort(input_list) == expected_output

def test_case_3():
    input_list = [4, 8, 12, 16, 20, 2, 10]
    expected_output = ([], [2, 4, 8, 10, 12, 16, 20])
    assert split_and_sort(input_list) == expected_output

def test_case_4():
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    expected_output = ([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], [2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
    assert split_and_sort(input_list) == expected_output

def test_case_5():
    input_list = [5, 5, 5, 10, 10, 15, 15, 20, 20, 25, 25]
    expected_output = ([5, 15, 25], [10, 20])
    assert split_and_sort(input_list) == expected_output

def test_case_6():
    input_list = [19, 22, 5, 8, 12, 25, 30]
    expected_output = ([5, 19, 25], [8, 12, 22, 30])
    assert split_and_sort(input_list) == expected_output
