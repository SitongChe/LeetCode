#https://leetcode.com/problems/remove-covered-intervals/description/
#time O(NlogN) space O(N)
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        if n == 0:
            return 0
        intervals.sort(key = lambda x:(x[0],-x[1]))
        start,end = intervals[0]
        ans = 0
        for curStart,curEnd in intervals:
            if curStart>=start and curEnd<=end:
                ans+=1
            else:
                start,end = curStart,curEnd
        return n-ans+1
