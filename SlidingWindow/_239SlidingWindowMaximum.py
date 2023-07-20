#https://leetcode.com/problems/sliding-window-maximum/
#time O(N), space O(k), where k is the size of the sliding window
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        stack = []
        l = 0
        ans = []
        for r in range(len(nums)):
            while stack and nums[stack[-1]]<nums[r]:
                stack.pop()
            stack.append(r)
            if l>stack[0]:
                stack.pop(0)
            if r>=k-1:
                ans.append(nums[stack[0]])
                l+=1
        return ans

