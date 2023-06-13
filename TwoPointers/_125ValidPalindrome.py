#https://leetcode.com/problems/valid-palindrome/
#time O(n), space O(1)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isChar(c):
            val = ord(c)-ord("a")
            if val >=0 and val<=25:
                return True
            val = ord(c)-ord("A")
            if val >=0 and val<=25:
                return True
            val = ord(c)-ord("0")
            if val >=0 and val<=9:
                return True
            return False
        i = 0
        j = len(s)-1
        while i<j:
            while i<j and not isChar(s[i]):
                i+=1
            while i<j and not isChar(s[j]):
                j-=1
            if s[i].lower()!=s[j].lower():
                return False
            i+=1
            j-=1
        return True
