#Problem: Given a list of tuples representing ranges, condense the ranges.

Constraints
Are the tuples in sorted order?
No
Are the tuples ints?
Yes
Will all tuples have the first element less than the second?
Yes
Is there an upper bound on the input range?
No
Is the output a list of tuples?
Yes
Is the output a new array?
Yes
Can we assume the inputs are valid?
No, check for None
Can we assume this fits memory?
Yes

Test Cases
* None input -> TypeError
* [] - []
* [(2, 3), (7, 9)] -> [(2, 3), (7, 9)]
* [(2, 3), (3, 5), (7, 9), (8, 10)] -> [(2, 5), (7, 10)]
* [(2, 3), (3, 5), (7, 9), (8, 10), (1, 11)] -> [(1, 11)]
* [(2, 3), (3, 8), (7, 9), (8, 10)] -> [(2, 10)]


Complexity:
Time: O(n log(n))
Space: O(n)

class Solution(object):

    def merge_ranges(self, array):
        if array is None:
            raise TypeError
        if not array:
            return []
        ans = []
        array.sort()
        start,end = array[0]
        for curStart,curEnd in array:
            if curStart<=end:
                end = max(end,curEnd)
            else:
                ans.append((start,end))
                start = curStart
                end = curEnd
        ans.append((start,end))
        return ans
