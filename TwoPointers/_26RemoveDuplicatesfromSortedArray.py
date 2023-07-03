#https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
#time O(n), space O(1)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                nums[k]=nums[i]
                k+=1
        return k
