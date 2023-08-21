#Problem: Determine if a number is a power of two.

Constraints
Is the input number an int?
Yes
Can we assume the inputs are valid?
No
Is the output a boolean?
Yes
Can we assume this fits memory?
Yes

Test Cases
None -> TypeError
0 -> False
1 -> True
2 -> True
15 -> False
16 -> True

Complexity:
Time: O(1)
Space: O(1)

class Solution(object):

    def is_power_of_two(self, val):
        if val is None:
            raise TypeError
        if val<=0:
            return False
        return (val&(val-1))==0
