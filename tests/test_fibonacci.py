"""
The test module for MyRange
"""
import pytest

from fibonacci import MyRange

def test_invalid_input():
    """
    Given incorrect type input , a ValueError should be raised.
    """
    with pytest.raises(ValueError):
        apple = 'apple'
        list(MyRange(apple))

def test_input_of_0():
    """
    Given input of zero, list should be [0].
    """
    assert list(MyRange(0)) == [0]

def test_input_of_1():
    """
    Given input of one, list should be [0, 1].
    """
    assert list(MyRange(1)) == [0, 1]

def test_input_of_2():
    """
    Given input of two, list should be [0, 1, 1].
    """
    assert list(MyRange(2)) == [0, 1, 1]

def test_input_of_4():
    """
    Given input of four, list should be [0, 1, 1, 2, 3].
    """
    assert list(MyRange(4)) == [0, 1, 1, 2, 3]

def test_input_of_10():
    """
    Given input of ten, list should be [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55].
    """
    assert list(MyRange(10)) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

def test_input_of_neg_int():
    """
    Given a negative integer input value, list should be [] empty.
    """
    assert list(MyRange(-10)) == []
