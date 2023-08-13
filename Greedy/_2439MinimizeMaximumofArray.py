#https://leetcode.com/problems/minimize-maximum-of-array/description/
#time O(n) space O(1)
class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        n = len(nums)
        ans = nums[0]
        total = 0
        for i in range(n):
            total += nums[i]
            ans = max(ans,ceil(total/(i+1)))
        return ans
