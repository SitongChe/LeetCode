#https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/description/
#time O(2^N) space O(n)
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def traceback(index,tmp):
            self.ans = max(self.ans,len(tmp))
            for i in range(index,n):
                found = False
                if len(set(arr[i]))<len(arr[i]):
                    continue
                for c in arr[i]:
                    if c in visited:
                        found = True
                if not found:
                    for c in arr[i]:
                        visited.add(c)
                    traceback(i+1,tmp+arr[i])
                    for c in arr[i]:
                        visited.remove(c)
            
        n = len(arr)
        self.ans = 0
        visited = set()
        traceback(0,"")
        
        return self.ans
