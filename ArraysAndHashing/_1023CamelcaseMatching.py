#https://leetcode.com/problems/camelcase-matching/description/
#time O(n) ,space  O(n)
class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def isMatch(query):
            i = 0
            for c in query:
                if i<len(pattern) and c == pattern[i]:
                    i+=1
                elif c.isupper():
                    return False
            return i == len(pattern)
        return [isMatch(q) for q in queries]
