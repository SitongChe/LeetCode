#https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/
#time O(2^ n) space O(n)
class Solution:
    def splitString(self, s: str) -> bool:
        def traceback(index,prev):
            if index == n:
                return True
            for i in range(index,n):
                cur = int(s[index:i+1])
                if cur+1==prev:
                    if traceback(i+1,cur):
                        return True
            return False
        n = len(s)
        for i in range(n-1):
            cur = int(s[:i+1])
            if traceback(i+1,cur):
                return True
        return False
                
class Solution:
    def splitString(self, s: str) -> bool:
        def traceback(index,tmp):
            if index == n:
                if len(tmp)>1:
                    return True
                return False
            for i in range(index,n):
                cur = int(s[index:i+1])
                if not tmp or cur+1==tmp[-1]:
                    tmp.append(cur)
                    if traceback(i+1,tmp):
                        return True
                    tmp.pop()
            return False
        n = len(s)
        return traceback(0,[])
                
        


