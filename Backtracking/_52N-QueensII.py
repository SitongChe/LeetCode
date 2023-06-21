#https://leetcode.com/problems/n-queens-ii/description/
#time O(n!) space O(n)
class Solution:
    def totalNQueens(self, n: int) -> int:
        def traceback(row):
            if row == n:
                self.ans+=1
                return
            for i in range(n):
                j = row
                if i in cols or i+j in posDiag or i-j in negDiag:
                    continue
                cols.add(i)
                posDiag.add(i+j)
                negDiag.add(i-j)
                traceback(row+1)
                negDiag.remove(i-j)
                posDiag.remove(i+j)
                cols.remove(i)
        self.ans = 0
        cols = set()
        posDiag = set()
        negDiag = set()
        traceback(0)
        return self.ans
                

