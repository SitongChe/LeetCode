#https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/description/
#time O(nlogn), space O(1)
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        r = n-1
        l = 0
        ans = 0
        while l<=r:
            while nums[r]+nums[l]>target and l<=r:
                r-=1
            if l<=r:
                ans += (2**(r-l))
                ans %= (10**9+7)
            l+=1
        return ans

