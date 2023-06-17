#https://leetcode.com/problems/simplify-path/submissions/970892567/
#Given current directory and change directory path, return final path.
#
#For Example:
#
#Curent                 Change            Output
#
#/                    /facebook           /facebook
#/facebook/anin       ../abc/def          /facebook/abc/def
#/facebook/instagram   ../../../../.      /

#/../ no op for parent of root
#/home//foo/ double slash is equal to single slash
#/... all other str is considered valid
#/a//b////c/d//././/.. double dot in the end
#/..hidden double dot with value

#follow up: support ~ for home

#Time O(n) space O(n)

class Solution:
    def simplifyPath(self, path, stack):
        n = len(path)
        i=0
        while i<n:
            if path[i] == '/':
                i+=1
                continue
            tmp = ""
            while i<n and path[i]!='/':
                tmp += path[i]
                i+=1
            if tmp == ".":
                i+=1
                continue
            elif tmp == "..":
                if stack:
                    stack.pop()
            elif tmp == "~":
                stack = []
            else:
                stack.append(tmp)
            i+=1
        return stack
        
    def applyChange(self, current, change):
        stack = self.simplifyPath(current, [])
        stack = self.simplifyPath(change, stack)
        return "/"+"/".join(stack) if stack else "/"
        
