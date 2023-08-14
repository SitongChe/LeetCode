#https://leetcode.com/problems/ugly-number/description/
#time  O(m*n)  space O(m*n)
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        #treat like a 1 dimension list, each time shift by 1 position
        k%=(m*n)
        ans = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                index = ((i*n+j)+k)%(m*n)
                ans[index//n][index%n]=grid[i][j]
        return ans
        
#time  O(k*m*n)  space O(m)
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        for _ in range(k):
            tmp = []
            for i in range(m):
                tmp.append(grid[i][n-1])
                for j in range(n-1,0,-1):
                    grid[i][j]=grid[i][j-1]
            for i in range(1,m):
                grid[i][0]=tmp[i-1]
            grid[0][0]=tmp[m-1]
        return grid
