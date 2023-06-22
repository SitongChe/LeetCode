#https://leetcode.com/problems/partition-to-k-equal-sum-subsets/description/
#time O(k^n) space O(n)
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        def traceback(index,side,tmp):
            if side == k:
                return True
            if target == tmp:
                return traceback(0,side+1,0)
            for i in range(index,n):
                if i not in visited and tmp+nums[i]<=target:
                    if i > index and nums[i]==nums[i-1] and i-1 not in visited:
                        continue
                    visited.add(i)
                    tmp+=nums[i]
                    if traceback(i+1,side,tmp):
                        return True
                    tmp-=nums[i]
                    visited.remove(i)
            return False

        total = sum(nums)
        if total%k:
            return False
        target = total//k
        n = len(nums)
        visited = set()
        nums.sort(reverse = True)
        return traceback(0,0,0)



