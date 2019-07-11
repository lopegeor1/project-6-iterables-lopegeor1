# fibanacci.py
"""ABC"""
class MyRange:
    """A range used to create object with fibanacci properties"""
    def __init__(self, stop, step=1):
        """
        Requires start and stop values, and an optional step.
        """
        if not isinstance(stop, int):
            raise ValueError

        self.stop = stop + 1
        self.step = step
        start = 0 #  this variable is predifined, no user input (args) required
        self.start = start
        self.current = start - 1  # Use the starting value minus a step

    def __iter__(self):
        """Returns the instance object which is an iterator."""
        return self

    def __next__(self):
        """Defines the instance object as an iterator."""
        self.current += self.step # Increment by the step value

        if self.current >= self.stop:
            raise StopIteration

        return self.current
