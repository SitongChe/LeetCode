#Problem: Given a list of 2x2 matrices, minimize the cost of matrix multiplication.

Constraints
Do we just want to calculate the cost and not list the actual order of operations?
Yes
Can we assume the inputs are valid?
No
Can we assume this fits memory?
Yes

Test Cases
None -> Exception
[] -> 0
[Matrix(2, 3), Matrix(3, 6), Matrix(6, 4), Matrix(4, 5)] -> 124

Complexity:
Time: O(n^3)
Space: O(n^2)

class Matrix(object):

    def __init__(self, first, second):
        self.first = first
        self.second = second
        
class MatrixMultiplicationCost(object):

    def find_min_cost(self, matrices):
        if matrices is None:
            raise TypeError
        if not matrices:
            return 0
        n = len(matrices)
        ans = [[0]*n for _ in range(n)]
        
        for offset in range(1,n):
            for i in range(n-offset):
                j = i+offset
                minCost = float("inf")
                for k in range(i,j):
                    cost = ans[i][k]+ans[k+1][j]+matrices[i].first*matrices[k].second*matrices[j].second
                    minCost = min(minCost,cost)
                ans[i][j]=minCost
        return ans[0][n-1]
