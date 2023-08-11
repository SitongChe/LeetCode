#https://leetcode.com/problems/number-of-enclaves/description/
#time O(V + E) space O(V + E) 
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def dfs(i,j):
            if i<0 or i>=m or j<0 or j>=n or grid[i][j]==0 or (i,j) in visited:
                return 0
            visited.add((i,j))
            return 1+dfs(i+1,j)+dfs(i-1,j)+dfs(i,j+1)+dfs(i,j-1)

        m = len(grid)
        n = len(grid[0])
        visited = set()
        land = sum(sum(row) for row in grid)
        boarderLand = 0
        for i in range(m):
            if grid[i][0]==1:
                boarderLand += dfs(i,0)
            if grid[i][n-1]==1:
                boarderLand += dfs(i,n-1)
        for j in range(n):
            if grid[0][j]==1:
                boarderLand += dfs(0,j)
            if grid[m-1][j]==1:
                boarderLand += dfs(m-1,j)
        return land-boarderLand

