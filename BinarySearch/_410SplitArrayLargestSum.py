#https://leetcode.com/problems/split-array-largest-sum/description/
#time get O(N * log N), space O(1)
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(maxTotal):
            total = 0
            split = 0
            for num in nums:
                total+=num
                if total>maxTotal:
                    split += 1
                    total = num
            return split+1<=k

        left = max(nums)
        right = sum(nums)
        while left+1<right:
            mid = left+(right-left)//2
            if canSplit(mid):
                right = mid
            else:
                left = mid
        if canSplit(left):
            return left
        return right


                
            

