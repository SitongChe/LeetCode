#https://leetcode.com/problems/k-closest-points-to-origin/
#time O(m+f*logm) space O(m)  m: the number of unique tasks, f: maximum frequency of a task
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        queue = []
        ans = 0
        while maxHeap or queue:
            ans += 1
            if not maxHeap:
                ans = queue[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt != 0:
                    queue.append((cnt,ans+n))
            if queue and queue[0][1]==ans:
                heapq.heappush(maxHeap,queue.pop(0)[0])
        return ans
