#https://leetcode.com/problems/counting-bits/description/
#time  O(n), space O(n)
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]
        offset = 1
        for i in range(1,n+1):
            if offset*2==i:
                offset = i
                ans.append(1)
            else:
                ans.append(ans[i-offset]+1)
        return ans

        
