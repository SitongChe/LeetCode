#Problem: Find the difference of two integers without using the + or - sign.

Constraints
Can we assume the inputs are valid?
No, check for None
Can we assume this fits memory?
Yes

Test Cases
* None input -> TypeError
* 7, 5 -> 2
* -5, -7 -> 2
* -5, 7 -> -12
* 5, -7 -> 12

Complexity:
Time: O(b), where b is the number of bits
Space: O(b), where b is the number of bits

class Solution(object):

    def sub_two(self, a, b):
        if a is None or b is None:
            raise TypeError
        diff = a^b
        borrow = ((~a)&b)<<1
        if borrow:
            return self.sub_two(diff,borrow)
        return diff
