#https://leetcode.com/problems/insert-interval/
#time O(N) space O(1)
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start = newInterval[0]
        end = newInterval[1]
        left = []
        right = []
        for i,interval in enumerate(intervals):
            if interval[1]<start:
                left.append(interval)
            elif interval[0]>end:
                right = intervals[i:]
                break
            else:
                end = max(interval[1],end)
                start = min(interval[0],start)
                    
        return left+[[start,end]]+right
                    



