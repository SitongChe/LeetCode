#https://leetcode.com/problems/sliding-window-maximum/
#time O(N), space O(k), where k is the size of the sliding window
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        stack = []
        start = end = 0
        ans = []
        for end in range(len(nums)):
            while stack and nums[stack[-1]]<nums[end]:
                stack.pop()
            stack.append(end)
            if start>stack[0]:
                stack.pop(0)
            if end>=k-1:
                ans.append(nums[stack[0]])
                start+=1
        return ans
