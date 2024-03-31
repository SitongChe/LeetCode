#https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
#time O(N), space O(1)
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a','e','i','o','u'}
        n = len(s)
        start = 0
        count = 0
        ans = 0
        for end in range(n):
            if s[end] in vowels:
                count+=1
            if end-start+1>k:
                if s[start] in vowels:
                    count-=1
                start+=1
            ans = max(ans,count)
        return ans
