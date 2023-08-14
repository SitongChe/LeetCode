#https://leetcode.com/problems/roman-to-integer/description/
#time  O(n)  space O(1)
class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        n = len(s)
        for i,c in enumerate(s):
            if c=='I':
                if i+1<n:
                    if s[i+1]=='V' or s[i+1]=='X':
                        total-=2
                total+=1
            if c=='X':
                if i+1<n:
                    if s[i+1]=='L' or s[i+1]=='C':
                        total-=20
                total += 10
            if c=='C':
                if i+1<n:
                    if s[i+1]=='D' or s[i+1]=='M':
                        total-=200
                total += 100
            if c=='V':
                total += 5
            if c=='L':
                total += 50
            if c=='D':
                total += 500
            if c=='M':
                total += 1000
        return total


class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        total = 0
        n = len(s)
        for i in range(n):
            cur = roman[s[i]]
            if i+1<n and roman[s[i+1]]>cur:
                total-=cur
            else:
                total+=cur
        return total
