#https://leetcode.com/problems/process-tasks-using-servers/description/
#time O(n log n) space O(N)
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = []
        for numPassengers, fromi, toi in trips:
            events.append([fromi,numPassengers])
            events.append([toi,-numPassengers])
        events.sort()
        curPassengers = 0
        for event in events:
            curPassengers += event[1]
            if curPassengers > capacity:
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
