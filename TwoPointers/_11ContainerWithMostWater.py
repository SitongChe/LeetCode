#https://leetcode.com/problems/container-with-most-water/
#time O(n), space O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        maxHeight = max(height)
        l = 0
        r = n-1
        ans = 0
        while l<r:
            water = (r-l)*min(height[l],height[r])
            ans = max(ans,water)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
            if (r-l)*maxHeight<ans:
                return ans
        return ans

        
                
