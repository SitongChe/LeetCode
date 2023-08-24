#Problem: Find the highest product of three numbers in a list.

Constraints
Is the input a list of integers?
Yes
Can we get negative inputs?
Yes
Can there be duplicate entries in the input?
Yes
Will there always be at least three integers?
No
Can we assume the inputs are valid?
No, check for None input
Can we assume this fits memory?
Yes

Test Cases
None -> TypeError
Less than three ints -> ValueError
[5, -2, 3] -> -30
[5, -2, 3, 1, -1, 4] -> 60

Complexity:
Time: O(n)
Space: O(1)

class Solution(object):

    def max_prod_three(self, array):
        if array is None:
            raise TypeError
        n = len(array)
        if n<3:
            raise ValueError
        maxThree = array[0]*array[1]*array[2]
        maxTwo = array[0]*array[1]
        minTwo = array[0]*array[1]
        maxOne = max(array[0],array[1])
        minOne = min(array[0],array[1])
        for i in range(2,n):
            maxThree = max(maxThree, maxTwo*array[i], minTwo*array[i])
            maxTwo = max(maxTwo,maxOne*array[i],minOne*array[i])
            minTwo = min(minTwo,maxOne*array[i],minOne*array[i])
            maxOne = max(maxOne, array[i])
            minOne = max(minOne, array[i])
        return maxThree
        
