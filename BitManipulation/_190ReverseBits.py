#https://leetcode.com/problems/reverse-bits/description/
#time  O(32), space O(1)
class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for _ in range(31):
            ans += n&1
            n>>=1
            ans<<=1
        ans+=n&1
        return ans
        
        
