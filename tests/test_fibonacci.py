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
