#https://leetcode.com/problems/trapping-rain-water/
#time O(n), space O(1)
#two pointers
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n-1
        leftMax = height[l]
        rightMax = height[r]
        ans = 0
        while l<r:
            if leftMax<rightMax:
                l+=1
                leftMax = max(leftMax, height[l])
                ans+= leftMax-height[l]
            else:
                r-=1
                rightMax = max(rightMax, height[r])
                ans+= rightMax-height[r]
        return ans

#time O(n), space O(1)
#stack
class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        ans = 0
        for i in range(len(height)):
            while stack and height[stack[-1]]<height[i]:
                prev = stack.pop()
                if stack:
                    ans += (min(height[stack[-1]],height[i])-height[prev])*(i-stack[-1]-1)
            stack.append(i)
        return ans

