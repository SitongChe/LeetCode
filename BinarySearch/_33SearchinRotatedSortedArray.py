#https://leetcode.com/problems/search-in-rotated-sorted-array/
#time O(logN), space O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n-1
        while left+1<right:
            mid = left+(right-left)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>nums[left]:
                if nums[mid]>=target and nums[left]<=target:
                    right = mid
                else:
                    left = mid
            else:
                if nums[mid]<=target and nums[right]>=target:
                    left = mid
                else:
                    right = mid
        if nums[left]==target:
            return left
        if nums[right]==target:
            return right
        return -1
