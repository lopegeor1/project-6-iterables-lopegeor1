"""
fibonacci.py -- Write the application code here
"""

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
        self.data = []
        start = 0 #  this variable is predifined, no user input (args) required
        self.start = start
        self.current = start - 1  # Use the starting value minus a step
        self.prev1 = 1
        self.prev2 = 0

    def __iter__(self):
        """Returns the instance object which is an iterator."""
        return self

    def __next__(self):
        """Defines the instance object as an iterator."""
        if self.current == (self.start - 1):
            self.current += self.step # Increment by the step value
            self.data.append(self.current)
        elif self.current == 0:
            self.current = self.prev1
            self.data.append(self.current)
        elif self.current >= 1:
            self.current = self.prev1 + self.prev2
            self.data.append(self.current)
            self.prev2 = self.prev1
            self.prev1 = self.current

        if (len(self.data) - 1) >= self.stop:
            raise StopIteration

        return self.current
