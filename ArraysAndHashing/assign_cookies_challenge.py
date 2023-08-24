#Problem: Assign Cookies.
https://leetcode.com/problems/assign-cookies/description/

Constraints
Are the inputs two list(int), one for greed factor and the other for cookie size?
Yes
Are the inputs are sorted increasing order?
No
Can we change inputs themselves, or do we need to make a copy?
You can change them
Is the output an int?
Yes
Is the greed factor always >= 1?
Yes
Can we assume the inputs are valid?
No, check for None
Can we assume this fits memory?
Yes

Test Cases
* None input -> TypeError
[1, 2, 3], [1, 1] -> 1
[1, 2], [1, 2, 3] -> 2
[7, 8, 9, 10], [5, 6, 7, 8] -> 2

Complexity:
Time: O(n log n) for the sort
Space: O(1), assuming the sort is in-place

class Solution(object):

    def find_content_children(self, g, s):
        if g is None or s is None:
            raise TypeError
        g.sort(reverse = True)
        s.sort(reverse = True)
        i = 0
        j = 0
        ans = 0
        while i < len(s):
            if j == len(g):
                break
            if s[i]>=g[j]:
                ans+=1
                i+=1
                j+=1
            else:
                j+=1
        return ans
