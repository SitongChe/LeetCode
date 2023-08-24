#Problem: Find the length of the longest substring with at most k distinct characters.

Constraints
Can we assume the inputs are valid?
No
Can we assume the strings are ASCII?
Yes
Is this case sensitive?
Yes
Is a substring a contiguous block of chars?
Yes
Do we expect an int as a result?
Yes
Can we assume this fits memory?
Yes

Test Cases
None -> TypeError
'', k = 3 -> 0
'abcabcdefgghiij', k=3 -> 6
'abcabcdefgghighij', k=3 -> 7

Complexity:
Time: O(n * k), where n is the number of chars, k is the length of the map due to the min() call
Space: O(n)

from collections import defaultdict
class Solution(object):

    def longest_substr(self, string, k):
        if string is None or k is None:
            raise TypeError
        start = 0
        ans = 0
        count = defaultdict(int)
        for end in range(len(string)):
            if count[string[end]]==0:
                k-=1
            count[string[end]]+=1
            while k < 0:
                count[string[start]]-=1
                if count[string[start]]==0:
                    k+=1
                start+=1
            ans = max(ans,end-start+1)
        return ans
            
