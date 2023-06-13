#https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
#time O(log N), space O(1)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n-1
        while left+1<right:
            mid = left+(right-left)//2
            if nums[mid]>nums[left]:
                left = mid
            else:
                right = mid
        return min(nums[0], nums[left], nums[right])



        
