#https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/
#time O(logN), space O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        left = 0
        right = n-1
        while left+1<right:
            while left+1+1<right and nums[left]==nums[left+1]:
                left+=1
            while left+1<right-1 and nums[right]==nums[right-1]:
                right-=1
            mid = left+(right-left)//2
            if nums[mid]==target:
                return True
            if nums[mid]>=nums[left]:
                if nums[mid]>target and nums[left]<=target:
                    right = mid
                else:
                    left = mid
            else:
                if nums[mid]<target and nums[right]>=target:
                    left = mid
                else:
                    right = mid

        if nums[left]==target or nums[right]==target:
            return True
        return False
