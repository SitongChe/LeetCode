#Problem: Utopian Tree

The Utopian Tree goes through 2 cycles of growth every year. Each spring, it doubles in height. Each summer, its height increases by 1 meter.
A Utopian Tree sapling with a height of 1 meter is planted at the onset of spring. How tall will the tree be after  growth cycles?
For example, if the number of growth cycles is , the calculations are as follows:
Period  Height
0          1
1          2
2          3
3          6
4          7
5          14

Constraints
Can we assume the inputs are valid?
No, check for None
Can we assume this fits memory?
Yes

Complexity:
Time: O(1)
Space: O(1)

class Solution(object):

    def calc_utopian_tree_height(self, cycles):
        if cycles is None:
            raise TypeError
        ans = 2**(cycles//2+1)-1
        if cycles%2==0:
            return ans
        else:
            return 2*ans
