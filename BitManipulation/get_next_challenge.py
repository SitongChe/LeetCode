#Problem: Given a positive integer, get the next largest number and the next smallest number with the same number of 1's as the given number.

Constraints
Is the output a positive int?
Yes
Can we assume the inputs are valid?
No
Can we assume this fits memory?
Yes

Test Cases
None -> Exception
0 -> Exception
negative int -> Exception
General case:
  * Input:         0000 0000 1101 0111
  * Next largest:  0000 0000 1101 1011
  * Next smallest: 0000 0000 1100 1111

Complexity:
Time: O(b), where b is the number of bits in num
Space: O(b), where b is the number of bits in num

class Bits(object):

    def get_next_largest(self, num):
        if num is None:
            raise TypeError
        if num<=0:
            raise ValueError
        num_copy = num
        count_zero = 0
        count_one = 0
        # We'll look for index, which is the right-most non-trailing zero
        while num_copy and num_copy&1==0:
            count_zero+=1
            num_copy>>=1
        while num_copy and num_copy&1==1:
            count_one+=1
            num_copy>>=1
        # Determine index and set the bit
        index = count_zero+count_one
        num |= 1<<index
        # Clear all bits to the right of index
        num &= ~((1<<index)-1)
        # Set bits starting from 0
        num |= (1<<(count_one-1))-1
        return num
        

    def get_next_smallest(self, num):
        if num is None:
            raise TypeError
        if num<=0:
            raise ValueError
        num_copy = num
        count_zero = 0
        count_one = 0
        # We'll look for index, which is the right-most non-trailing 1
        while num_copy and num_copy&1==1:
            count_one+=1
            num_copy>>=1
        while num_copy and num_copy&1==0:
            count_zero+=1
            num_copy>>=1
        # Determine index and clear the bit
        index = count_zero+count_one
        num &= ~(1<<index)
        # Clear all bits to the right of index
        num &= ~((1<<index)-1)
        # Set bits starting from 0
        num |= (1<<(count_one+1))-1
        return num
