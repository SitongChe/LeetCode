#Problem: Determine whether you can win the Nim game given the remaining stones.

Constraints
Is the input an int?
Yes
Is the output a boolean?
Yes
Can we assume the inputs are valid?
No
Can we assume this fits memory?
Yes

Test Cases
None -> TypeError
1, 2, or 3 -> True
4 -> False
7 -> True
40 -> False

Complexity:
Time: O(1)
Space: O(1)

class Solution(object):

    def can_win_nim(self, num_stones_left):
        if num_stones_left is None:
            raise TypeError
        if num_stones_left%4==0:
            return False
        return True
