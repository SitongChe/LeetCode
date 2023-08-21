#Problem: Given an int, repeatedly add its digits until the result is one digit.
Constraints
Can we assume num is not negative?
Yes
Can we assume the inputs are valid?
No
Can we assume this fits memory?
Yes

Test Cases
* None input -> TypeError
* negative input -> ValueError
* 9 -> 9
* 138 -> 3
* 65536 -> 7


class Solution(object):
Complexity:
Time: O(logN)
Space: O(1)
    def add_digits_1(self, val):
        if val is None:
            raise TypeError
        if val<0:
            raise ValueError
        while val//10:
            newVal = 0
            while val:
                newVal += val%10
                val//=10
            val = newVal
        return val
    
Complexity:
Time: O(1)
Space: O(1)
    def add_digits(self, val):
        if val is None:
            raise TypeError
        if val<0:
            raise ValueError
        if val == 0:
            return 0
        if val%9 == 0:
            return 9
        return val%9
