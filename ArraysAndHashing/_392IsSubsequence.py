#https://leetcode.com/problems/is-subsequence/description/
#time O(n) ,space  O(1)
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index = 0
        if not s:
            return True
        for c in t:
            if c == s[index]:
                index+=1
            if index == len(s):
                return True
        return False
