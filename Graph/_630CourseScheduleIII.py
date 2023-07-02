#https://leetcode.com/problems/course-schedule-iv/description/
#time O(n log n) space O(n)
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        heap = []
        start = 0
        for t,end in sorted(courses, key = lambda x:x[1]):
            start += t
            heapq.heappush(heap,-t)
            while start>end:
                start += heapq.heappop(heap)
        return len(heap)
        
