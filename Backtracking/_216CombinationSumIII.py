#https://leetcode.com/problems/combination-sum-iii/description/
#time O(C(9,k)) space O(k)
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def traceback(index,target):
            if target<0:
                return
            if target==0:
                if len(tmp)==k:
                    ans.append(tmp.copy())
                return
            if len(tmp)>k:
                return
            for i in range(index,10):
                tmp.append(i)
                traceback(i+1,target-i)
                tmp.pop()
        ans = []
        tmp = []
        traceback(1,n)
        return ans




