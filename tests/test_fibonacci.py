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
    assert [number for number in MyRange(0)] == [0]
