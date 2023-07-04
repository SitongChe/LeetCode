#https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/
#time O(n), space O(1)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        r = 0
        l = 0
        while r<n:
            count = 1
            while r+1<n and nums[r+1]==nums[r]:
                count+=1
                r+=1
            for i in range(min(2,count)):
                nums[l]=nums[r]
                l+=1
            r+=1
        return l
        
