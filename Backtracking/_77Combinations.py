#https://leetcode.com/problems/combinations/description/
#time O(N!) space O(N)
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def traceback(index):
            if len(tmp)==k:
                ans.append(tmp.copy())
                return
            for i in range(index,n+1):
                tmp.append(i)
                traceback(i+1)
                tmp.pop()
        ans = []
        tmp = []
        traceback(1)
        return ans


                    



