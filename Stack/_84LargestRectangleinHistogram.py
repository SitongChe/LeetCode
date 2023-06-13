#https://leetcode.com/problems/largest-rectangle-in-histogram/
#time O(N) space O(N)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        n = len(heights)
        if n ==1:
            return 0
        stack = []
        ans = 0
        for i in range(n):
            while stack and heights[stack[-1]]>heights[i]:
                h = heights[stack.pop()]
                if stack:
                    w = i-stack[-1]-1
                else:
                    w = i
                ans = max(ans,h*w)
            stack.append(i)
        return ans


