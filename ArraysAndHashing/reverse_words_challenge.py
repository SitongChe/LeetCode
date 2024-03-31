#Problem: Given a string of words, return a string with the words in reverse

Constraints
Can we assume the string is ASCII?
Yes
Is whitespace important?
no the whitespace does not change
Is this case sensitive?
yes
What if the string is empty?
return None
Is the order of words important?
yes

Test Cases
Empty string -> None
"the sun is very hot" -> "eht nus si yrev toh"

Complexity:
Time complexity is O(n) where n is the number of chars.
Space complexity is O(n) where n is the number of chars.

def reverse_words (S):
    if not S:
        return None
    strs = S.split(' ')
    ans = ""
    for string in strs:
        for j in range(len(string)-1,-1,-1):
            ans += string[j]
        ans += " "
    n = len(ans)
    return ans[:n-1]
        
