#https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
#time get O(logN), space O(1)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(left,right,leftBias):
            ans = -1
            while left+1<right:
                mid = left+(right-left)//2
                if nums[mid]==target:
                    if leftBias:
                        right = mid
                    else:
                        left = mid
                elif nums[mid]<target:
                    left = mid
                else:
                    right = mid
            if leftBias:
                if nums[left]==target:
                    ans = left
                elif nums[right]==target:
                    ans = right
            else:
                if nums[right]==target:
                    ans = right
                elif nums[left]==target:
                    ans = left
            return ans


        n = len(nums)
        if n == 0:
            return [-1,-1]
        left = 0
        right = n-1
        start = binarySearch(left,right,True)
        end = binarySearch(left,right,False)
        
        return [start,end]

