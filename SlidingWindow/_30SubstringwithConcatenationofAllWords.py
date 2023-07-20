#https://leetcode.com/problems/minimum-size-subarray-sum/description/
#time O(wordLength*len(s)), space O(n)
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(words)
        if n == 0:
            return []
        wordLength = len(words[0])
        ans = []
        for l in range(wordLength):
            count = Counter(words)
            k = len(count.keys())
            for r in range(l,len(s)+1-wordLength,wordLength):
                cur = s[r:r+wordLength]
                count[cur]-=1
                if count[cur]==0:
                    k-=1
                while k == 0:
                    if (r-l)/wordLength+1 == n:
                        ans.append(l)
                    cur = s[l:l+wordLength]
                    if count[cur]==0:
                        k+=1
                    count[cur]+=1
                    l+=wordLength
        return ans
                
