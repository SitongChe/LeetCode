#https://leetcode.com/problems/longest-substring-without-repeating-characters/
#time O(N), space O(k), where k is the size of the character set
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        start = 0
        end = 0
        ans = 0
        for end in range(len(s)):
            while s[end] in charSet:
                charSet.remove(s[start])
                start += 1
            charSet.add(s[end])
            ans = max(ans,end-start+1)
        return ans
