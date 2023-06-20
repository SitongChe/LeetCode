#https://leetcode.com/problems/mini-parser/description/
#time O(n * m^2) space O(n * m), n number of words, m length of each word
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        n = len(s)
        if n == 0:
            return
        if s[0]!='[':
            return NestedInteger(int(s))
        stack = []
        cur = None
        num = ""
        for i in range(n):
            if s[i]=='[':
                if cur:
                    stack.append(cur)
                cur = NestedInteger()
            elif s[i]==']':
                if num:
                    cur.add(NestedInteger(int(num)))
                    num = ""
                if stack:
                    prev = stack.pop()
                    prev.add(cur)
                    cur = prev
            elif s[i]==',':
                if num:
                    cur.add(NestedInteger(int(num)))
                    num=""
            else:
                num+=s[i]
        return cur

