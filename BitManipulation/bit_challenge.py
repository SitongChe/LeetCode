#Problem: Implement common bit manipulation operations: get_bit, set_bit, clear_bit, clear_bits_msb_to_index, clear_bits_msb_to_lsb, update_bit.

Constraints
Can we assume the inputs are valid?
No
Can we assume this fits memory?
Yes

Test Cases
None as a number input -> Exception
Negative index -> Exception
get_bit
number   = 0b10001110, index = 3
expected = True
set_bit
number   = 0b10001110, index = 4
expected = 0b10011110
clear_bit
number   = 0b10001110, index = 3
expected = 0b10000110
clear_bits_msb_to_index
number   = 0b10001110, index = 3
expected = 0b00000110
clear_bits_index_to_lsb
number   = 0b10001110, index = 3
expected = 0b10000000
update_bit
number   = 0b10001110, index = 3, value = 1
expected = 0b10001110
number   = 0b10001110, index = 3, value = 0
expected = 0b10000110
number   = 0b10001110, index = 0, value = 1
expected = 0b10001111


Time and Space complexity all O(1)

def validate_index(func):
    def validate_index_wrapper(self, *args, **kwargs):
        for arg in args:
            if arg < 0:
                raise IndexError('Invalid index')
        return func(self, *args, **kwargs)
    return validate_index_wrapper

class Bit(object):

    def __init__(self, number):
        self.number = number

    @validate_index
    def get_bit(self, index):
        return (self.number >> index) & 1

    @validate_index
    def set_bit(self, index):
        self.number |= 1<<index
        return self.number

    @validate_index
    def clear_bit(self, index):
        self.number &= ~(1<<index)
        return self.number

    @validate_index
    def clear_bits_msb_to_index(self, index):
        self.number &= (1<<index)-1
        return self.number

    @validate_index
    def clear_bits_index_to_lsb(self, index):
        self.number &= ~((1<<(index+1))-1)
        return self.number

    @validate_index
    def update_bit(self, index, value):
        if value is None or value not in (0, 1):
            raise Exception('Invalid value')
        if self.get_bit(index) == value:
            return self.number
        if value == 1:
            return self.set_bit(index)
        else:
            return self.clear_bit(index)
