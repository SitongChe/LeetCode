#https://leetcode.com/problems/pacific-atlantic-water-flow/
#time O(M*N) space O(M*N)
#dfs
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        result = []
        m = len(heights)
        n = len(heights[0])
        def dfs(i,j,ocean,prev):
            if i <0 or i>=m or j<0 or j>=n or visited[i][j]==3 or visited[i][j]==ocean or heights[i][j]<prev:
                return
            prev = heights[i][j]
            visited[i][j]+=ocean
            if visited[i][j]>=3:
                result.append([i,j])
                visited[i][j]=3
            dfs(i+1,j,ocean,prev)
            dfs(i-1,j,ocean,prev)
            dfs(i,j+1,ocean,prev)
            dfs(i,j-1,ocean,prev)
        visited = [[0]*n for i in range(m)]
        for i in range(m):
            dfs(i,0,1,heights[i][0])
            dfs(i,n-1,2,heights[i][n-1])
        for j in range(n):
            dfs(0,j,1,heights[0][j])
            dfs(m-1,j,2,heights[m-1][j])
        return result

                    



