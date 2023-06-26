#https://leetcode.com/problems/meeting-rooms-iii/description/
#time O(nlogn) space O(n)
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        available = [i for i in range(n)]
        unavailable = []
        used = [0]*n
        for meeting in meetings:
            while unavailable and unavailable[0][0]<=meeting[0]:
                heapq.heappush(available,heapq.heappop(unavailable)[1])
            if not available:
                time,room = heapq.heappop(unavailable)
                used[room]+=1
                heapq.heappush(unavailable,[time+meeting[1]-meeting[0],room])
            else:
                room = heapq.heappop(available)
                used[room]+=1
                heapq.heappush(unavailable,[meeting[1],room])
        return used.index(max(used))
                
                
