#https://leetcode.com/problems/minimum-size-subarray-sum/description/
#time O(N), space O(1)
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        total = 0
        ans = inf
        for r in range(len(nums)):
            total += nums[r]
            while total>=target:
                ans=min(ans,r-l+1)
                total-=nums[l]
                l+=1
        return ans if ans != inf else 0
