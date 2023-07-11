#https://leetcode.com/problems/isomorphic-strings/description/
#time O(n) ,space  O(n)
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapStoT = {}
        mapTtoS = {}
        if len(s)!=len(t):
            return False
        for ss,tt in zip(s,t):
            if ss in mapStoT:
                if mapStoT[ss]!=tt:
                    return False
            if tt in mapTtoS:
                if mapTtoS[tt]!=ss:
                    return False
            mapStoT[ss]=tt
            mapTtoS[tt]=ss
        return True

        
