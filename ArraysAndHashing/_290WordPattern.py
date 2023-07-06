#https://leetcode.com/problems/word-pattern/description/
#time O(n) ,space  O(m)
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        map = {}
        letters = s.split(" ")
        if len(pattern)!=len(letters):
            return False
        for i,p in enumerate(pattern):
            if p in map:
                if map[p]!=letters[i]:
                    return False
            else:
                map[p]=letters[i]
        if len(set(map.keys()))!=len(set(map.values())):
            return False
        return True
