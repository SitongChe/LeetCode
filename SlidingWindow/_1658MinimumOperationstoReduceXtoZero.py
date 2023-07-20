#https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/description/
#time O(n), space O(1)
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # finding the longest subarray whose sum is == totalSum - x
        n = len(nums)
        l = 0
        target = sum(nums)-x
        if target<0:
            return -1
        if target == 0:
            return n
        total = 0
        ans = -1
        for r in range(len(nums)):
            total+=nums[r]
            while total>=target:
                if total==target:
                    ans = max(ans,r-l+1)
                total-=nums[l]
                l+=1

        return -1 if ans == -1 else n-ans
                
