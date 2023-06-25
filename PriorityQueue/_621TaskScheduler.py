#https://leetcode.com/problems/k-closest-points-to-origin/
#time O(m+f*logm) space O(m)  m: the number of unique tasks, f: maximum frequency of a task
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [(-cnt,cur) for cur,cnt in count.items()]
        heapq.heapify(maxHeap)
        queue = []
        ans = 0
        while maxHeap or queue:
            ans += 1
            if maxHeap:
                negCnt, cur = heapq.heappop(maxHeap)
                negCnt+=1
                if negCnt:
                    queue.append((ans+n,(negCnt,cur)))
            else:
                ans = queue[0][0]
            if queue:
                if queue[0][0]<=ans:
                    heapq.heappush(maxHeap,queue.pop(0)[1])
        return ans
