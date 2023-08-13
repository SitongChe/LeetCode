#https://leetcode.com/problems/jump-game-ii/description/
#time O(N) space O(1)
class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        if n == 0:
            return 0
        l = 0
        r = 0
        ans = 0
        maxJump = 0
        while r<n-1:
            for i in range(l,r+1):
                maxJump = max(maxJump,i+nums[i])
            l = r+1
            r = maxJump
            ans +=1
        return ans
                    



