#https://leetcode.com/problems/container-with-most-water/
#time O(n), space O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0
        i = 0
        j = n-1
        hmax = max(height)
        ans = 0
        while i<j:
            cur = (j-i)*min(height[i],height[j])
            ans = max(ans,cur)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
            if (j-i)*hmax<ans:
                return ans
        return ans

        
                
