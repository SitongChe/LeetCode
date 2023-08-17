#https://leetcode.com/problems/missing-number/description/
#time  O(n), space O(1)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = len(nums)
        for i,num in enumerate(nums):
            ans^=i
            ans^=num
        return ans
        
