#https://leetcode.com/problems/island-perimeter/description/
#time O(m*n) space O(m*n)
#priority queue
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def dfs(i,j):
            if i<0 or i>=m or j<0 or j>=n or grid[i][j]==0:
                self.ans+=1
                return
            if (i,j) in visited:
                return
            visited.add((i,j))
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        m = len(grid)
        n = len(grid[0])
        visited = set()
        self.ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    dfs(i,j)
        return self.ans
