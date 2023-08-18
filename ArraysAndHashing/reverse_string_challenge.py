#Problem: Implement a function to reverse a string (a list of characters), in-place.

Constraints
Can we assume the string is ASCII?
Yes
Note: Unicode strings could require special handling depending on your language
Since we need to do this in-place, it seems we cannot use the slice operator or the reversed function?
Correct
Since Python string are immutable, can we use a list of characters instead?
Yes

Test Cases
None -> None
[''] -> ['']
['f', 'o', 'o', ' ', 'b', 'a', 'r'] -> ['r', 'a', 'b', ' ', 'o', 'o', 'f']


Complexity:
Time: O(n)
Space: O(1)
class ReverseString(object):

    def reverse(self, chars):
        if not chars:
            return chars
        n = len(chars)
        for i in range(n//2):
            chars[i],chars[n-i-1]=chars[n-i-1],chars[i]
        return chars

Pythonic-Code

This question has an artificial constraint that prevented the use of the slice operator and the reversed method. For completeness, the solutions for these are provided below. Note these solutions are not in-place.
class ReverseStringAlt(object):

    def reverse_string_alt(string):
        if string:
            return string[::-1]
        return string

    def reverse_string_alt2(string):
        if string:
            return ''.join(reversed(string))
        return string
