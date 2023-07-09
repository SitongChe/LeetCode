#https://leetcode.com/problems/find-pivot-index/description/
#time O(n) ,space  O(1)
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        leftSum = 0
        n = len(nums)
        for i in range(n):
            rightSum = total - nums[i] - leftSum
            if leftSum == rightSum:
                return i
            leftSum += nums[i]
        return -1


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sumAll = sum(nums)
        prefix = 0
        n = len(nums)
        if nums[0]==sumAll:
            return 0
        for i in range(n):
            prefix += nums[i]
            if i+1 < n and 2*prefix + nums[i+1]==sumAll:
                return i+1
        return -1
