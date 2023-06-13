#https://leetcode.com/problems/subsets-ii/
#time O(2^N) space O(2^N)
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        n = len(nums)
        def traceback(tmp,index):
            ans.append(tmp.copy())
            for i in range(index,n):
                if i>index and nums[i-1]==nums[i]:
                    continue
                tmp.append(nums[i])
                traceback(tmp,i+1)
                tmp.pop()
        traceback([],0)
        return ans

                    



