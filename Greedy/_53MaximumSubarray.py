#https://leetcode.com/problems/maximum-subarray/description/
#time O(N) space O(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0:
            return 0
        maxSum = nums[0]
        total = 0
        for i in range(n):
            total += nums[i]
            maxSum = max(maxSum,total)
            total = max(total,0)
        return maxSum

                    



