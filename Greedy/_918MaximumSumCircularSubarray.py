#https://leetcode.com/problems/maximum-sum-circular-subarray/description/
#time O(N) space O(1)
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        total = 0
        curMax = 0
        curMin = 0
        maxSum = nums[0]
        minSum = nums[0]
        for i in range(n):
            cur = nums[i]
            curMax += cur
            curMin += cur
            maxSum = max(maxSum,curMax)
            minSum = min(minSum,curMin)
            curMax = max(curMax,0)
            curMin = min(curMin,0)
            total += cur
        return max(maxSum,total-minSum) if maxSum>0 else maxSum
        



