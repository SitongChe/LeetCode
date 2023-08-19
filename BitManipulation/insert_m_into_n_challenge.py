#Problem: Given two 16 bit numbers, n and m, and two indices i, j, insert m into n such that m starts at bit j and ends at bit i.

Constraints
Can we assume j > i?
Yes
Can we assume i through j have enough space for m?
Yes
Can we assume the inputs are valid?
No
Can we assume this fits memory?
Yes

Test Cases
None as an input -> Exception
Negative index for i or j -> Exception
General case
i      = 2
j      = 6
n      = 0000 0100 0000 0000
m      = 0000 0000 0001 0011
result = 0000 0100 0100 1100

Complexity:
Time: O(b), where b is the number of bits in num
Space: O(b), where b is the number of bits in num

class Bits(object):

    def insert_m_into_n_1(self, m, n, i, j):
        if None in (m,n,i,j):
            raise TypeError
        if i<0 or j<0 or j<i:
            raise ValueError
        #clear bits from i to j in n
        left_mask = (1<<(j+1))-1
        right_mask = ~((1<<i)-1)
        mask = ~(left_mask&right_mask)
        return (n&mask)|(m<<i)

    def insert_m_into_n(self, m, n, i, j):
        if None in (m,n,i,j):
            raise TypeError
        if i<0 or j<0 or j<i:
            raise ValueError
        #clear bits from i to j in n
        # -a = (~a) + 1
        # -1 = all 1
        left_mask = -1<<(j+1)
        right_mask = (1<<i)-1
        mask = left_mask|right_mask
        return (n&mask)|(m<<i)
