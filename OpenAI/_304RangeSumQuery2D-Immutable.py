#https://leetcode.com/problems/simplify-path/submissions/970892567/
#time O(M*N) space O(M*N)
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0])
        self.sum = matrix.copy()
        for j in range(1,n):
            self.sum[0][j]+=self.sum[0][j-1]
        for i in range(1,m):
            self.sum[i][0]+=self.sum[i-1][0]
        for i in range(1,m):
            for j in range(1,n):
                self.sum[i][j]+=self.sum[i-1][j]+self.sum[i][j-1]-self.sum[i-1][j-1]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        a = self.sum[row2][col2]
        b = self.sum[row1-1][col1-1] if row1-1>=0 and col1-1>=0 else 0
        c = self.sum[row2][col1-1] if col1-1>=0 else 0
        d = self.sum[row1-1][col2] if row1-1>=0 else 0

        return a+b-c-d
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
