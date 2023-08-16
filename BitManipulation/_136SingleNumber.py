#https://leetcode.com/problems/single-number/description/
#time  O(n), space O(1)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans^=num
        return ans
