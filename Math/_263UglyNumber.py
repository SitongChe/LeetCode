#https://leetcode.com/problems/ugly-number/description/
#time  O(log n)  space O(1)
class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        for i in [2,3,5]:
            while n%i==0:
                n//=i
        return n==1
        
