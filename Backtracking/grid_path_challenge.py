#Problem: Implement an algorithm to have a robot move from the upper left corner to the bottom right corner of a grid.

Constraints
Are there restrictions to how the robot moves?
The robot can only move right and down
Are some cells off limits?
Yes
Is this a rectangular grid? i.e. the grid is not jagged?
Yes
Will there always be a valid way for the robot to get to the bottom right?
No, return None
Can we assume the inputs are valid?
No
Can we assume this fits memory?
Yes

Test Cases
o = valid cell
x = invalid cell

   0  1  2  3
0  o  o  o  o
1  o  x  o  o
2  o  o  x  o
3  x  o  o  o
4  o  o  x  o
5  o  o  o  x
6  o  x  o  x
7  o  x  o  o
General case
expected = [(0, 0), (1, 0), (2, 0),
            (2, 1), (3, 1), (4, 1),
            (5, 1), (5, 2), (6, 2),
            (7, 2), (7, 3)]
No valid path: In above example, row 7 col 2 is also invalid -> None
None input -> None
Empty matrix -> None


#time O(2^N) space O(N)
class CoinChanger(object):

    def make_change(self, coins, total):
        if coins is None or total is None:
            raise TypeError
        if not coins or not total:
            return 0
        n = len(coins)
        coins.sort()
        self.ans = 0
        def traceback(index,target):
            if target==0:
                self.ans+=1
                return
            if target<0:
                return
            for i in range(index,n):
                traceback(i,target-coins[i])
        traceback(0,total)
        return self.ans
        
   
Algorithm
We'll use a bottom-up dynamic programming approach.
The rows (i) represent the coin values.
The columns (j) represent the totals.

  -------------------------
  | 0 | 1 | 2 | 3 | 4 | 5 |
  -------------------------
0 | 1 | 0 | 0 | 0 | 0 | 0 |
1 | 1 | 1 | 1 | 1 | 1 | 1 |
2 | 1 | 1 | 2 | 2 | 3 | 3 |
3 | 1 | 1 | 2 | 3 | 4 | 5 |
  -------------------------

Number of ways to get total n with coin[n] equals:
* Number of ways to get total n with coin[n - 1] plus
* Number of ways to get total n - coin[n]

if j == 0:
    T[i][j] = 1
if row == 0:
    T[i][j] = 0
if coins[i] >= j
    T[i][j] = T[i - 1][j] + T[i][j - coins[i]]
else:
    T[i][j] = T[i - 1][j]

The answer will be in the bottom right corner of the matrix.

Complexity:
Time: O(M * N * (M + N))
Space: O(M * N)

class Grid(object):

    def find_path(self, matrix):
        if matrix is None:
            return None
        m = len(matrix)
        n = len(matrix[0])
        visited = set()
        self.ans = None
        def traceback(i,j,path):
            if i<0 or i>=m or j<0 or j>=n or (i,j) in visited:
                return
            visited.add((i,j))
            if matrix[i][j]==0:
                return
            path.append((i,j))
            if i == m-1 and j == n-1:
                self.ans = path.copy()
                return
            traceback(i+1,j,path)
            traceback(i,j+1,path)
            path.pop()
        traceback(0,0,[])
        return self.ans
        
class Grid(object):

    def find_path(self, matrix):
        if matrix is None or not matrix:
            return None
        cache = {}
        path = []
        if self._find_path(matrix, len(matrix) - 1,
                           len(matrix[0]) - 1, cache, path):
            return path
        else:
            return None

    def _find_path(self, matrix, row, col, cache, path):
        if row < 0 or col < 0 or not matrix[row][col]:
            return False
        cell = (row, col)
        if cell in cache:
            return cache[cell]
        cache[cell] = (row == 0 and col == 0 or
                       self._find_path(matrix, row, col - 1, cache, path) or
                       self._find_path(matrix, row - 1, col, cache, path))
        if cache[cell]:
            path.append(cell)
        return cache[cell]
