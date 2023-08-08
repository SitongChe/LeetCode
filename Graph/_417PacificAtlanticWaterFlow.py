#https://leetcode.com/problems/pacific-atlantic-water-flow/
#time O(M*N) space O(M*N)
#dfs
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def dfs(i,j,water,prevHeight):
            if i<0 or i>=m or j<0 or j>=n or heights[i][j]<prevHeight or visited[i][j]==3 or visited[i][j]==water:
                return
            visited[i][j]+=water
            dfs(i+1,j,water,heights[i][j])
            dfs(i-1,j,water,heights[i][j])
            dfs(i,j+1,water,heights[i][j])
            dfs(i,j-1,water,heights[i][j])
        m = len(heights)
        n = len(heights[0])
        visited = [[0]*n for i in range(m)]
        for i in range(m):
            dfs(i,0,1,-1)
            dfs(i,n-1,2,-1)
        for j in range(n):
            dfs(0,j,1,-1)
            dfs(m-1,j,2,-1)
        ans = []
        for i in range(m):
            for j in range(n):
                if visited[i][j]==3:
                    ans.append([i,j])
        return ans

