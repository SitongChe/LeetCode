#https://leetcode.com/problems/jump-game/description/
#time O(N) space O(1)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 0:
            return True
        reach = 0
        for i in range(n):
            if i<=reach:
                cur = i+nums[i]
                reach = max(reach,cur)
        return reach>=n-1
        
        
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        goal = n-1
        for i in range(n-2,-1,-1):
            if i+nums[i]>=goal:
                goal = i
        return goal==0

                    



