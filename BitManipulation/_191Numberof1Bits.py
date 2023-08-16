#https://leetcode.com/problems/number-of-1-bits/
#time  O(k) k is the number of 1 in n, space O(1)
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n&=n-1 #get rid of the right most 1
            count+=1
        return count
 
#time  O(n) space O(1)
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            if n&1==1:
                count+=1
            n = n>>1
        return count
