#https://leetcode.com/problems/combination-sum-iv/description/
#time O(target * n) space O(target)
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        def traceback(index,target):
            if target<0:
                return 0
            if target==0:
                return 1
            if ans[target]!=-1:
                return ans[target]
            count = 0
            for i in range(0,n):
                count += traceback(i,target-nums[i])
            ans[target]=count
            return count
        ans = [-1]*(target+1)
        n = len(nums)
        traceback(0,target)
        return ans[target]



