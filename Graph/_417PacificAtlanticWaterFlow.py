#https://leetcode.com/problems/pacific-atlantic-water-flow/
#time O(M*N) space O(M*N)
#dfs
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def dfs(i,j,water,prevHeight):
            if i<0 or i>=m or j<0 or j>=n or visited[i][j]==water or visited[i][j]==3 or heights[i][j]<prevHeight:
                return
            visited[i][j]+=water
            if visited[i][j]>=3:
                visited[i][j]=3
            dfs(i+1,j,water,heights[i][j])
            dfs(i-1,j,water,heights[i][j])
            dfs(i,j+1,water,heights[i][j])
            dfs(i,j-1,water,heights[i][j])
        m = len(heights)
        n = len(heights[0])
        visited = [[0]*n for i in range(m)]
        for i in range(m):
            dfs(i,0,1,heights[i][0])
            dfs(i,n-1,2,heights[i][n-1])
        for j in range(n):
            dfs(0,j,1,heights[0][j])
            dfs(m-1,j,2,heights[m-1][j])
        ans = []
        for i in range(m):
            for j in range(n):
                if visited[i][j]==3:
                    ans.append([i,j])
        return ans
                    



