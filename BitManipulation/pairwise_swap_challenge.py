#Problem: Swap the odd and even bits of a positive integer with as few operations as possible.

Constraints
Can we assume the input is always a positive int?
Yes
Can we assume we're working with 32 bits?
Yes
Is the output an int?
Yes
Can we assume the inputs are valid (not None)?
No
Can we assume this fits memory?
Yes

Test Cases
None -> Exception
0 -> 0
-1 -> -1
General case
  input  = 1001 1111 0110
  result = 0110 1111 1001

Complexity:
Time: O(1)
Space: O(1)

class Bits(object):

    def pairwise_swap(self, num):
        if num is None:
            raise TypeError
        odd = (num&(int('1010101010101010',base = 2)))>>1
        even = (num&(int('0101010101010101',base = 2)))<<1
        return odd | even
