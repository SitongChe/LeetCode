#Problem: Given a list of ints, find the products of every other int for each index.

Constraints
Can we use division?
No
Is the output a list of ints?
Yes
Can we assume the inputs are valid?
No
Can we assume this fits memory?
Yes

Test Cases
* None -> TypeError
* [] -> []
* [0] -> []
* [0, 1] -> [1, 0]
* [0, 1, 2] -> [2, 0, 0]
* [1, 2, 3, 4] -> [24, 12, 8, 6]

Complexity:
Time: O(n)
Space: O(n)

class Solution(object):

    def mult_other_numbers(self, array):
        if array is None:
            raise TypeError
        n = len(array)
        if n == 0 or n == 1:
            return []
        ans = [1]*n
        cur = 1
        for i in range(n):
            ans[i] = cur
            cur *= array[i]
        cur = 1
        for i in range(n-1,-1,-1):
            ans[i]*= cur
            cur *= array[i]
        return ans
            
