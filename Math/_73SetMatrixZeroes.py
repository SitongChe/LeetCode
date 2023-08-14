#https://leetcode.com/problems/set-matrix-zeroes/description/
#time O(n*m) space O(1)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        n=len(matrix[0])
        iZero = False
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    matrix[0][j]=0
                    if i == 0:
                        iZero = True
                    else:
                        matrix[i][0]=0
        for i in range(1,m):
            for j in range(1,n):
                if matrix[0][j]==0 or matrix[i][0]==0:
                    matrix[i][j]=0

        if matrix[0][0]==0:
            for i in range(m):
                matrix[i][0]=0
        if iZero:
            for j in range(n):
                matrix[0][j]=0
        
