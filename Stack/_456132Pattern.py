#https://leetcode.com/problems/132-pattern/description/
#time O(n) space O(N)
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        curMin = nums[0]
        for num in nums:
            while stack and stack[-1][0]<= num:
                stack.pop()
            if stack and stack[-1][1]<num:
                return True
            stack.append([num,curMin])
            curMin = min(curMin, num)
            
        return False
