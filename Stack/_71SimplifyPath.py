#https://leetcode.com/problems/simplify-path/description/
#time O(n) space O(N)
class Solution:
    def simplifyPath(self, path: str) -> str:
        n = len(path)
        i = 0
        stack = []
        while i < n:
            if path[i]=='/':
                i+=1
                continue
            tmp = ""
            while i<n and path[i]!='/':
                tmp+=path[i]
                i+=1
            if tmp==".":
                i+=1
                continue
            elif tmp == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(tmp)
        return '/'+'/'.join(stack) if stack else "/"


        

