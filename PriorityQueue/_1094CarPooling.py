#https://leetcode.com/problems/process-tasks-using-servers/description/
#time O(n log n) space O(N)
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = [(start,people) for people,start,end in trips]
        events += [(end,-people) for people,start,end in trips]
        
        heapq.heapify(events)
        cur = 0
        while events:
            location,change = heapq.heappop(events)
            cur+=change
            if cur>capacity:
                return False

        return True
        
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda t:t[1])
        minHeap = []
        curPeople = 0
        for trip in trips:
            people, start, end = trip
            while minHeap and minHeap[0][0]<=start:
                prevEnd, prevPeople = heapq.heappop(minHeap)
                curPeople-=prevPeople
            curPeople += people
            if curPeople > capacity:
                return False
            heapq.heappush(minHeap,(end,people))
        return True
