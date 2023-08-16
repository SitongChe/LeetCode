#https://leetcode.com/problems/powx-n/description/
#time O(logn) space O(logn)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n<0:
            x = 1/x
            n = -1*n
        if n == 1:
            return x
        res = self.myPow(x*x,n//2)
        return res*x if n%2 else res
