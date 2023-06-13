#https://leetcode.com/problems/non-overlapping-intervals/
#time O(NlogN) space O(1)
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        if n == 0:
            return 0
        ans = 0
        intervals.sort()
        start = intervals[0][0]
        end = intervals[0][1]
        for i in range(1,n):
            if intervals[i][0]<end:
                ans += 1
                end = min(end,intervals[i][1])
            else:
                end = intervals[i][1]
        return ans
            

