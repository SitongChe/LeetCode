#https://leetcode.com/problems/greatest-common-divisor-of-strings/description/
#time O(n/m) space O(n/m), where "n" is the length of the longer string and "m" is the length of the shorter string
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if not str1 or not str2:
            return ""
        if str1 == str2:
            return str1
        l1 = len(str1)
        l2 = len(str2)
        if l1<l2:
            str1,str2 = str2,str1
            l1,l2 = l2,l1
        if str1[:l2]!=str2:
            return ""
        return self.gcdOfStrings(str1[l2:],str2)
