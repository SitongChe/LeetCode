#Problem: Determine if a string s1 is a rotation of another string s2, by calling (only once) a function is_substring.

Constraints
Can we assume the string is ASCII?
Yes
Note: Unicode strings could require special handling depending on your language
Is this case sensitive?
Yes
Can we use additional data structures?
Yes
Can we assume this fits in memory?
Yes

Test Cases
Any strings that differ in size -> False
None, 'foo' -> False (any None results in False)
' ', 'foo' -> False
' ', ' ' -> True
'foobarbaz', 'barbazfoo' -> True



class Rotation(object):
Complexity:
Time: O(len(s1)*len(s2))
Space: O(1)
    def is_substring(self, s1, s2):
        return s2 in s1

Complexity:
Time: O(len(s1)+len(s2))
Space: O(len(s2))
    def is_substring_kmp(self, s1, s2):
        n1 = len(s1)
        n2 = len(s2)
        lps = [0]*n2
        i = 1
        j = 0
        while i<n2:
            if s2[i]==s2[j]:
                lps[i]=j+1
                i+=1
                j+=1
            else:
                if j == 0:
                    lps[i]=0
                    i+=1
                else:
                    j=lps[j-1]
        i = 0
        j = 0
        while i<n1:
            if s1[i]==s2[j]:
                i+=1
                j+=1
            else:
                if j == 0:
                    i+=1
                else:
                    j = lps[j-1]
            if j == n2:
                return True
        return False
        
    def is_rotation(self, s1, s2):
        if not s1 and not s2:
            return True
        if not s1 or not s2:
            return False
        if len(s1)!=len(s2):
            return False
        return self.is_substring(s1+s1,s2)

