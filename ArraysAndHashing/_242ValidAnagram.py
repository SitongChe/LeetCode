#https://leetcode.com/problems/valid-anagram/
#time O(N),space O(N)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        map = defaultdict()
        for i in range(len(s)):
            map[s[i]]=map.get(s[i],0)+1
            map[t[i]]=map.get(t[i],0)-1
        return len([k for k,v in map.items() if v!=0])==0
