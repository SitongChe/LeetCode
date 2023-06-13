#https://leetcode.com/problems/binary-search/
#time O(logN), space O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0:
            return -1
        left = 0
        right = n-1
        while left+1<right:
            mid = left+(right-left)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                right = mid
            else:
                left = mid
        if nums[left]==target:
            return left
        if nums[right]==target:
            return right
        return -1
