#https://leetcode.com/problems/search-insert-position/description/
#time O(logN), space O(1)
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n-1
        while left+1<right:
            mid = left+(right-left)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                left = mid
            else:
                right = mid
        if nums[left]==target:
            return left
        if nums[right]==target:
            return right
        if nums[right]<target:
            return right+1
        if nums[left]<target:
            return right
        return left
