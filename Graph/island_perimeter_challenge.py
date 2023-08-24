#Problem: Island Perimeter.

Constraints
Can we assume the inputs are valid?
No, check for None
Can we assume this fits memory?
Yes

Test Cases
* None -> TypeError
* [[1, 0]] -> 4
* [[0, 1, 0, 0],
   [1, 1, 1, 0],
   [0, 1, 0, 0],
   [1, 1, 0, 0]] -> 16


class Solution(object):


    def island_perimeter(self, grid):
        if grid is None:
            raise TypeError
        m = len(grid)
        n = len(grid[0])
        self.ans = 0
        visited = set()
        def dfs(i,j):
            if i<0 or i>=m or j<0 or j>=n or grid[i][j]==0:
                self.ans+=1
                return
            if (i,j) in visited:
                return
            visited.add((i,j))
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and (i,j) not in visited:
                    dfs(i,j)
        return self.ans
        
    def island_perimeter(self, grid):
        if grid is None:
            raise TypeError('grid cannot be None')
        sides = 0
        num_rows = len(grid)
        num_cols = len(grid[0])
        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] == 1:
                    # Check left
                    if j == 0 or grid[i][j - 1] == 0:
                        sides += 1
                    # Check right
                    if j == num_cols - 1 or grid[i][j + 1] == 0:
                        sides += 1
                    # Check up
                    if i == 0 or grid[i - 1][j] == 0:
                        sides += 1
                    # Check down
                    if i == num_rows - 1 or grid[i + 1][j] == 0:
                        sides += 1
        return sides
