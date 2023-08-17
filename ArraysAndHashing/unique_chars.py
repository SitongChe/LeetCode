#Problem: Implement an algorithm to determine if a string has all unique characters.

Constraints

Can we assume the string is ASCII?
Yes
Note: Unicode strings could require special handling depending on your language
Can we assume this is case sensitive?
Yes
Can we use additional data structures?
Yes
Can we assume this fits in memory?
Yes


Test Cases

None -> False
'' -> True
'foo' -> False
'bar' -> True


Code: Sets and Length Comparison
class UniqueCharsSet(object):
    def has_unique_chars(self, string):
        if string is None:
            return False
        return len(set(string)) == len(string)
        
Code: Hash Map Lookup
class UniqueChars(object):
    def has_unique_chars(self, string):
        if string is None:
            return False
        chars_set = set()
        for char in string:
            if char in chars_set:
                return False
            else:
                chars_set.add(char)
        return True
        
Code: In-Place
class UniqueCharsInPlace(object):
    def has_unique_chars(self, string):
        if string is None:
            return False
        for char in string:
            if string.count(char) > 1:
                return False
        return True
