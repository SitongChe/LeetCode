#https://leetcode.com/problems/squares-of-a-sorted-array/description/
#time O(N), space O(1)
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 0:
            return []
        left = 0
        right = n-1
        ans = [0]*n
        while left<=right:
            lnum = abs(nums[left])
            rnum = abs(nums[right])
            if lnum < rnum:
                ans[right-left]=rnum*rnum
                right-=1
            else:
                ans[right-left]=lnum*lnum
                left+=1
        return ans
