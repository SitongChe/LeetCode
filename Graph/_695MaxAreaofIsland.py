#https://leetcode.com/problems/max-area-of-island/
#time O(M * N * α(M * N)) space  O(M * N)
#union find
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        uf = {}
        size = {}
        def find(x):
            uf.setdefault(x,x)
            size.setdefault(x,1)
            if x!=uf[x]:
                uf[x]=find(uf[x])
            return uf[x]
        def union(x,y):
            rootx = find(x)
            rooty = find(y)
            if rootx == rooty:
                return
            if size[rootx]<size[rooty]:
                size[rooty]+=size[rootx]
                uf[rootx]=uf[rooty]
            else:
                size[rootx]+=size[rooty]
                uf[rooty]=uf[rootx]
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    ans = max(ans,1)
                    if i>0 and grid[i-1][j]==1:
                        union((i-1,j),(i,j))
                    if j>0 and grid[i][j-1]==1:
                        union((i,j-1),(i,j))
        if size:
            ans = max(ans,max(size.values()))
        return ans
 
#time O(M * N) space  O(M * N)
#dfs
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.ans = 0
        self.max = 0
        m = len(grid)
        n = len(grid[0])
        visited = set()
        def dfs(i,j):
            if i<0 or i>=m or j<0 or j>=n or (i,j) in visited or grid[i][j]==0:
                return
            visited.add((i,j))
            self.ans += 1
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)

        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and (i,j) not in visited:
                    self.ans =0
                    dfs(i,j)
                    self.max=max(self.max,self.ans)

        return self.max


            
                    



