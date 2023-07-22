#https://leetcode.com/problems/daily-temperatures/
#time O(N) space O(N)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0]*n
        stack = []
        for i, temperature in enumerate(temperatures):
            while stack and temperatures[stack[-1]]<temperature:
                prev = stack.pop()
                ans[prev]=i-prev
            stack.append(i)
        return ans
