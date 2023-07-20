#https://leetcode.com/problems/k-radius-subarray-averages/description/
#time O(n), space O(n)
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = [-1]*n
        total = 0
        l = 0
        for r in range(n):
            total += nums[r]
            if r>=k*2:
                ans[r-k]=total//(r-l+1)
                total -= nums[l]
                l+=1
                
        return ans
