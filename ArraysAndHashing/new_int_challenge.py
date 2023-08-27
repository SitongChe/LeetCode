#Problem: Given an array of 32 integers, find an int not in the input. Use a minimal amount of memory.

Constraints
Are we working with non-negative ints?
Yes
What is the range of the integers?
Discuss the approach for 4 billion integers
Implement for 32 integers
Can we assume the inputs are valid?
No

Test Cases
None -> Exception
[] -> Exception
General case
There is an int excluded from the input -> int
There isn't an int excluded from the input -> None

Complexity:
Time: O(n)
Space: O(1)

class Bits(object):

    def new_int(self, array, max_size):
        if array is None or max_size is None:
            raise TypeError
        if not array:
            raise TypeError
        ans = 0
        for i in range(max_size):
            ans ^= i
        for a in array:
            ans ^= a
        return ans if ans else None
        


Complexity:
Time: O(b), where b is the number of bits
Space: O(b)

from bitstring import BitArray  # Run pip install bitstring


class Bits(object):

    def new_int(self, array, max_size):
        if not array:
            raise TypeError('array cannot be None or empty')
        bit_vector = BitArray(max_size)
        for item in array:
            bit_vector[item] = True
        for index, item in enumerate(bit_vector):
            if not item:
                return index
        return None
