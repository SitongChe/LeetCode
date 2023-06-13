#https://leetcode.com/problems/combination-sum-ii/
#time O(2^N) space O(2^N)
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()
        ans = []
        def traceback(target,tmp,index):
            if target == 0:
               ans.append(tmp.copy())
               return
            if target<0:
                return
            for i in range(index,n):
                if i>index and candidates[i]==candidates[i-1]:
                    continue
                tmp.append(candidates[i])
                traceback(target-candidates[i],tmp,i+1)
                tmp.pop()
        traceback(target,[],0)
        return ans
            


                    



