#https://leetcode.com/problems/k-closest-points-to-origin/
#time O(m+f*logm) space O(m)  m: the number of unique tasks, f: maximum frequency of a task
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        queue = []
        time = 0
        while maxHeap or queue:
            time+=1
            if not maxHeap:
                time = queue[0][0]
            else:
                cnt = 1+heapq.heappop(maxHeap)
                if cnt:
                    queue.append([time+n,cnt])
            if queue and time == queue[0][0]:
                heapq.heappush(maxHeap,queue.pop(0)[1])
        return time
