#https://leetcode.com/problems/n-queens/
#time O(N!) space O(N^2*N!)
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def traceback(i):
            if i == n:
                ans.append(tmp.copy())
                return
            for j in range(n):
                if j in cols or i+j in posDiag or i-j in negDiag:
                    continue
                cols.add(j)
                posDiag.add(i+j)
                negDiag.add(i-j)
                tmp.append("."*j+"Q"+"."*(n-1-j))
                traceback(i+1)
                tmp.pop()
                cols.remove(j)
                posDiag.remove(i+j)
                negDiag.remove(i-j)
        ans = []
        tmp = []
        cols = set()
        posDiag = set()
        negDiag = set()
        traceback(0)
        return ans




