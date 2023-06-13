#https://leetcode.com/problems/trapping-rain-water/
#time O(n), space O(1)
#two pointers
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0
        i = 0
        j = n-1
        leftMax = height[i]
        rightMax = height[j]
        ans = 0
        while i<j:
            if leftMax<rightMax:
                i+=1
                leftMax = max(leftMax,height[i])
                ans += leftMax-height[i]
            else:
                j-=1
                rightMax = max(rightMax,height[j])
                ans += rightMax-height[j]
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

