# fibanacci.py
"""ABC"""
class MyRange:
    """A range used to create object with fibanacci properties"""
    def __init__(self, stop):
        """
        Requires start and stop values, and an optional step.
        """
        if not isinstance(stop, int):
            raise ValueError

    def __iter__(self):
        """Returns the instance object which is an iterator."""
        return self

    def __next__(self):
        """Defines the instance object as an iterator."""
