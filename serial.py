"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self,a) -> None:
        self.a = a
        self.b = a 

    def __repr__(self) -> str:
        """Description of the object - its current location and its next count"""
        return f'SerialGenerator Start = {self.a} - Next = {self.a + 1} '

    def generate(self):
        """increments the starting number by 1"""
        self.b +=1
        print(self.b)
    
    def reset(self):
        """sets the counting number equal to its starting self"""
        self.b = self.a