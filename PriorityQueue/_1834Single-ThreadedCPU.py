#https://leetcode.com/problems/single-threaded-cpu/description/
#time O(NlogN) space O(N)
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = sorted([(t[0],t[1],i) for i,t in enumerate(tasks)])
        ans = []
        curTime = tasks[0][0]
        minHeap = []
        n = len(tasks)
        curTaskIndex = 0
        while len(ans)<n:
            while curTaskIndex < n and tasks[curTaskIndex][0]<=curTime:
                heapq.heappush(minHeap,(tasks[curTaskIndex][1],tasks[curTaskIndex][2]))
                curTaskIndex += 1
            if minHeap:
                curEnd, curIndex = heapq.heappop(minHeap)
                ans.append(curIndex)
                curTime += curEnd
            else:
                curTime = tasks[curTaskIndex][0]
        return ans
                

