#https://leetcode.com/problems/daily-temperatures/
#time O(N) space O(N)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        if n == 0:
            return []
        ans = [0]*n
        stack = []
        for i in range(n):
            while stack and temperatures[stack[-1]]<temperatures[i]:
                prev = stack.pop()
                ans[prev]=i-prev
            stack.append(i)
        return ans
