#Problem: Compress a string such that 'AAABCCDDDD' becomes 'A3BC2D4'. Only compress the string if it saves space.

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
None -> None
'' -> ''
'AABBCC' -> 'AABBCC'
'AAABCCDDDD' -> 'A3BC2D4'

Complexity:
Time: O(n)
Space: O(n)

class CompressString(object):
    def compress(self, string):
        if string is None:
            return None
        ans = ""
        n = len(string)
        i = 0
        while i < n:
            count = 1
            while i+1<n and string[i]==string[i+1]:
                count+=1
                i+=1
            ans += string[i]
            if count>1:
                ans += str(count)
            i+=1
        return ans if len(ans)<n else string
