#https://leetcode.com/problems/merge-intervals/
#time O(NlogN) space O(N)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        if n == 0:
            return []
        intervals.sort(key=lambda x:x[0])
        ans = []
        start = intervals[0][0]
        end = intervals[0][1]
        for i in range(1,n):
            if intervals[i][0]<=end:
                end = max(end,intervals[i][1])
            else:
                ans.append([start,end])
                start = intervals[i][0]
                end = intervals[i][1]
        ans.append([start,end])
        return ans
