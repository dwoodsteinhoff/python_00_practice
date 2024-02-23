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
    def __init__(self,start=0):
        self.start = start
        self.next_num = start

    def __repr__(self):
        '''Represents the Serial Number'''
        return f'<SerialGenerator start = {self.start} Next Serial Number = {self.next_num}>'

    def generate(self):
        "Generate the next serial number"

        self.next_num += 1
        return self.next_num - 1
    
    def reset(self):
       self.next_num = self.start