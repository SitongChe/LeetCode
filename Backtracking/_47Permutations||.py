#https://leetcode.com/problems/permutations-ii/description/
#time O(N!) space O(N)
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def traceback():
            if len(tmp)==n:
                ans.append(tmp.copy())
                return
            for i in range(n):
                if i not in used:
                    if i-1>=0 and nums[i]==nums[i-1] and i-1 not in used:
                        continue
                    tmp.append(nums[i])
                    used.add(i)
                    traceback()
                    tmp.pop()
                    used.remove(i)
        ans = []
        tmp = []
        used = set()
        n = len(nums)
        nums.sort()
        traceback()
        return ans


                    



