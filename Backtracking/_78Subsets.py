#https://leetcode.com/problems/subsets/
#time O(2^N) space O(2^N)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def traceback(tmp,index):
            ans.append(tmp.copy())
            for i in range(index,len(nums)):
                tmp.append(nums[i])
                traceback(tmp,i+1)
                tmp.pop()
        traceback([],0)
        return ans
