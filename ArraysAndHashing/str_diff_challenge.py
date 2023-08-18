#Problem: Find the single different char between two strings.

Constraints
Can we assume the strings are ASCII?
Yes
Is case important?
The strings are lower case
Can we assume the inputs are valid?
No, check for None
Otherwise, assume there is only a single different char between the two strings
Can we assume this fits memory?
Yes

Test Cases
None input -> TypeError
'ab', 'aab' -> 'a'
'aab', 'ab' -> 'a'
'abcd', 'abcde' -> 'e'
'aaabbcdd', 'abdbacade' -> 'e'



class Solution(object):

Complexity:
Time: O(m+n), where m and n are the lengths of s, t
Space: O(26)
    def find_diff(self, str1, str2):
        if str1 is None or str2 is None:
            raise TypeError
        if len(str1)>len(str2):
            str1,str2=str2,str1
        count = [0]*26
        for i in range(len(str1)):
            count[ord(str1[i])-ord('a')]+=1
            count[ord(str2[i])-ord('a')]-=1
        count[ord(str2[-1])-ord('a')]-=1
        return [chr(ord('a')+i) for i,v in enumerate(count) if v==-1][0]
        
Complexity:
Time: O(m+n), where m and n are the lengths of s, t
Space: O(1)
    def find_diff_xor(self, str1, str2):
        if str1 is None or str2 is None:
            raise TypeError
        ans = 0
        for c in str1:
            ans ^= ord(c)
        for c in str2:
            ans ^= ord(c)
        return chr(ans)
