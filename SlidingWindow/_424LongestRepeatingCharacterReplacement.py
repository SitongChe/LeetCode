#https://leetcode.com/problems/longest-repeating-character-replacement/
#time O(N), space O(1)
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # find the longest substring with at most k diff chars
        n = len(s)
        if n == 0:
            return 0
        start,end = 0,0
        maxF,ans = 0,0
        count = Counter()
        for end in range(n):
            count[s[end]]+=1
            maxF=max(maxF,count[s[end]])
            if end-start+1-maxF>k:
                count[s[start]]-=1
                start+=1
            ans = max(ans,end-start+1)
        return ans
