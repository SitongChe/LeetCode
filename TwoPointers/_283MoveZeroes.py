#https://leetcode.com/problems/move-zeroes/description/
#time O(n), space O(1)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[k]=nums[i]
                k+=1
        for i in range(k,len(nums)):
            nums[i]=0
            
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        r = 0
        while r<len(nums):
            if nums[r]!=0 and nums[l]==0:
                nums[l],nums[r]=nums[r],nums[l]
            if nums[l]!=0:
                l+=1
            r+=1
        
