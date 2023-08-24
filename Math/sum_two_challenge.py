#Problem: Find the sum of two integers without using the + or - sign.

Constraints
Can we assume the inputs are valid?
No, check for None
Can we assume this fits memory?
Yes

Test Cases

Input: a = 1, b = 2
Output: 3

Input: a = 2, b = 3
Output: 5


Complexity:
Time: O(b), where b is the number of bits
Space: O(b), where b is the number of bits

class Solution(object):

    def sum_two(self, a, b):
        if a is None or b is None:
            raise TypeError
        diff = a^b
        carry = (a&b)<<1
        if carry:
            return self.sum_two(diff,carry)
        return diff
