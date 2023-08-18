#Problem: Determine if a string is a permutation of another string.

Constraints
Can we assume the string is ASCII?
Yes
Note: Unicode strings could require special handling depending on your language
Is whitespace important?
Yes
Is this case sensitive? 'Nib', 'bin' is not a match?
Yes
Can we use additional data structures?
Yes
Can we assume this fits in memory?
Yes

Test Cases
One or more None inputs -> False
One or more empty strings -> False
'Nib', 'bin' -> False
'act', 'cat' -> True
'a ct', 'ca t' -> True

Complexity:
Time: O(n)
Space: O(n)

from collections import defaultdict
class Permutations(object):

    def is_permutation(self, str1, str2):
        if not str1 and not str2:
            return True
        if not str1 or not str2:
            return False
        if len(str1)!=len(str2):
            return False
        count = defaultdict(int)
        for i in range(len(str1)):
            count[str1[i]]+=1
            count[str2[i]]-=1
        return max(count.values())==0 and min(count.values())==0
