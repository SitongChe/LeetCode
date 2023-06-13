#https://leetcode.com/problems/n-queens/
#time O(N!) space O(N^2*N!)
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        tmp = []
        def traceback(row,cols,diag1s,diag2s):
            if row == n:
                ans.append(tmp.copy())
                return
            for i in range(n):
                col = i
                if col in cols or row-col in diag1s or row+col in diag2s :
                    continue
                cols.add(col)
                diag1s.add(row-col)
                diag2s.add(col+row)
                cur="."*i+"Q"+"."*(n-i-1)
                tmp.append(cur)
                traceback(row+1,cols,diag1s,diag2s)
                tmp.pop()
                cols.remove(col)
                diag1s.remove(row-col)
                diag2s.remove(col+row)
        traceback(0,set(),set(),set())
        return ans



