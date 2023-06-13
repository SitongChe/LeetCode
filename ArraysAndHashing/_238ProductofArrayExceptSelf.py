#https://leetcode.com/problems/product-of-array-except-self/
#time O(N),space O(N)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        if n == 0:
            return []
        prefix = 1
        postfix = 1
        ans = [1]*n
        for i in range(n):
            ans[i]=prefix
            prefix*=nums[i]
        for i in range(n-1,-1,-1):
            ans[i]*=postfix
            postfix*=nums[i]
        return ans
