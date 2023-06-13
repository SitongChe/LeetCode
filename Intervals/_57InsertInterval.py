#https://leetcode.com/problems/insert-interval/
#time O(N) space O(1)
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        n = len(intervals)
        start = newInterval[0]
        end = newInterval[1]
        for i in range(n):
            interval = intervals[i]
            if interval[1]<start:
                ans.append(interval)
            elif interval[0]>end:
                ans.append([start,end])
                ans += intervals[i:]
                return ans
            else:
                start = min(start,interval[0])
                end = max(end,interval[1])
        ans.append([start,end])
        return ans

                    



