#Problem: Given a magazine, see if a ransom note could have been written using the letters in the magazine.

Constraints
Is this case sensitive?
Yes
Can we assume we're working with ASCII characters?
Yes
Can we scan the entire magazine, or should we scan only when necessary?
You can scan the entire magazine
Can we assume the inputs are valid?
No
Can we assume this fits memory?
Yes

Test Cases
None -> Exception
'', '' -> True
'a', 'b' -> False
'aa', 'ab' -> False
'aa', 'aab' -> True


Complexity:
Time: O(n+m)
Space: O(n+m)

from collections import defaultdict
class Solution(object):

    def match_note_to_magazine(self, ransom_note, magazine):
        if ransom_note is None or magazine is None:
            raise TypeError
        count = defaultdict(int)
        for c in magazine:
            count[c]+=1
        for c in ransom_note:
            count[c]-=1
            if count[c]<0:
                return False
        return True
