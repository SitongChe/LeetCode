#Problem: Search a sorted matrix for an item.

Constraints
Are items in each row sorted?
Yes
Are items in each column sorted?
Yes
Is the sorting in ascending or descending order?
Ascending
Is the matrix a rectangle? Not jagged?
Yes
Is the matrix square?
Not necessarily
Is the output a tuple (row, col)?
Yes
Is the item you are searching for always in the matrix?
No
Can we assume the inputs are valid?
No
Can we assume this fits memory?
Yes


Test Cases
None -> Exception
General case
Item found -> (row, col)
Item not found -> None


Complexity:
Time: O(n + m), where n and m are the matrix dimensions
Space: O(1)

class SortedMatrix(object):

    def find_val(self, matrix, val):
        if matrix is None:
            raise TypeError
        m = len(matrix)
        if m == 0:
            raise ValueError
        n = len(matrix[0])
        if val is None:
            return None
        row = 0
        col = n-1
        while row<m and col>=0:
            if matrix[row][col]==val:
                return (row,col)
            elif matrix[row][col]<val:
                row+=1
            else:
                col-=1
        return None
        
        
