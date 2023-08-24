#Problem: Maximizing XOR
https://www.hackerrank.com/challenges/maximizing-xor/problem

Why this works.. this looks for highest bit which is different between l and r: for example (11, 12) that is third bit with value 4.. all bits above it are identical in both l and r, and you can not produce any l<=a<=b<=r which have non zero result of a^b. But you can find value a which has third bit zero and all remaining bits set (11 in this example), and b = a + 1 will clear all lower bits and set third bit, so a^b is all ones from highest difference bit down to bottom bit = maximum xor difference. qed.


Complexity:
Time: O(1)
Space: O(1)

class Solution(object):

    def max_xor(self, lower, upper):
        if lower is None or upper is None:
            raise TypeError
        x = lower^upper
        p = 1
        while (x&(p-1))!=x:
            p<<=1
        return p-1
