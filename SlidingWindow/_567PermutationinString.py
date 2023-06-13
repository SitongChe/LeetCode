#https://leetcode.com/problems/permutation-in-string/
#time O(N), space O(k), where k is the size of the character set
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = Counter([c for c in s1])
        k = len(count.keys())
        start,end = 0,0
        for end in range(len(s2)):
            count[s2[end]]-=1
            if count[s2[end]]==0:
                k-=1
            while k == 0:
                if end-start+1==len(s1):
                    return True
                if count[s2[start]]==0:
                    k+=1
                count[s2[start]]+=1
                start+=1
        return False
