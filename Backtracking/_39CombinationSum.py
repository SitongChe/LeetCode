#https://leetcode.com/problems/combination-sum/
#time O(2^N) space O(N)
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(candidates)
        def traceback(tmp,target,index):
            if target == 0:
                ans.append(tmp.copy())
                return
            if target < 0:
                return
            for i in range(index,n):
                tmp.append(candidates[i])
                traceback(tmp,target-candidates[i],i)
                tmp.pop()
        traceback([],target,0)
        return ans


                    



