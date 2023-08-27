#Problem: Sort an array of strings so all anagrams are next to each other.

Constraints
Are there any other sorting requirements other than the grouping of anagrams?
No
Can we assume the inputs are valid?
No
Can we assume this fits memory?
Yes

Test Cases
None -> Exception
[] -> []
General case
Input: ['ram', 'act', 'arm', 'bat', 'cat', 'tab']
Result: ['arm', 'ram', 'act', 'cat', 'bat', 'tab']


Complexity:
Time: O(k * n * log n) time, where k is the average length of the strings and n is the number of strings.
Space: O(n)

class Anagram(object):

    def group_anagrams(self, items):
        if items is None:
            raise TypeError
        items.sort(key = lambda x:sorted([c for c in x]))
        return items
