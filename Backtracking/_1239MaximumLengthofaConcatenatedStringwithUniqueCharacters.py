#https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/description/
#time O(2^N) space O(n)
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def traceback(index,tmp):
            for i in range(index,n):
                cur = arr[i]
                if not [c for c in cur if c in visited]:
                    if len(set(cur))<len(cur):
                        continue
                    tmp+=len(cur)
                    self.ans = max(self.ans, tmp)
                    for c in cur:
                        visited.add(c)
                    traceback(i+1,tmp)
                    tmp-=len(cur)
                    for c in cur:
                        if c in visited:
                            visited.remove(c)
        self.ans = 0
        n = len(arr)
        visited = set()
        traceback(0,0)
        return self.ans
