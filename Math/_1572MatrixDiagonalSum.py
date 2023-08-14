#https://leetcode.com/problems/matrix-diagonal-sum/description/
#time O(n) space O(1)
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        total = 0
        for i in range(n):
            total += mat[i][i]
            total += mat[i][n-i-1]
        if n%2:
            total -= mat[n//2][n//2]
        return total
