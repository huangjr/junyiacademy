import pytest
# test_coding.py

# def capital_case(x):
#     return x.capitalize()
#
# def test_capital_case():
#     assert capital_case('semaphore') == 'Semaphore'


def print_number(numbers):
    summ = sum(numbers)
    return summ

def test_print_number():
    test_list = [1, 2, 3]
    assert print_number(test_list) == 6