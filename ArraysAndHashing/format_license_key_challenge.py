#Problem: Format license keys.

Constraints
Is the output a string?
Yes
Can we change the input string?
No, you can't modify the input string
Can we assume the inputs are valid?
No
Can we assume this fits memory?
Yes

Test Cases
None -> TypeError
'---', k=3 -> ''
'2-4A0r7-4k', k=3 -> '24-A0R-74K'
'2-4A0r7-4k', k=4 -> '24A0-R74K'


Complexity:
Time: O(n)
Space: O(n)

class Solution(object):

    def format_license_key(self, license_key, k):
        s = ""
        for c in license_key:
            if c!='-':
                s+=c.upper()
        if not s:
            return ""
        firstLen = len(s)%k
        ans = ""a
        if firstLen:
            ans = s[:firstLen]+"-"
        for i in range(firstLen,len(s),k):
            ans+=s[i:i+k]
            if i+k<len(s):
                ans+="-"
        return ans
            
class Solution(object):

    def format_license_key(self, license_key, k):
        if license_key is None:
            raise TypeError('license_key must be a str')
        if not license_key:
            raise ValueError('license_key must not be empty')
        formatted_license_key = []
        num_chars = 0
        for char in license_key[::-1]:
            if char == '-':
                continue
            num_chars += 1
            formatted_license_key.append(char.upper())
            if num_chars >= k:
                formatted_license_key.append('-')
                num_chars = 0
        if formatted_license_key and formatted_license_key[-1] == '-':
            formatted_license_key.pop(-1)
        return ''.join(formatted_license_key[::-1])
