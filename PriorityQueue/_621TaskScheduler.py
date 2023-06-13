#https://leetcode.com/problems/k-closest-points-to-origin/
#time O(m+f*logm) space O(m)  m: the number of unique tasks, f: maximum frequency of a task
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        ans = 0
        queue = []
        while maxHeap or queue:
            ans+=1
            if maxHeap:
                cnt = heapq.heappop(maxHeap)
                cnt+=1
                if cnt != 0:
                    queue.append([cnt,ans+n])
            else:
                ans = queue[0][1]
            if queue:
                if queue[0][1]==ans:
                    heapq.heappush(maxHeap,queue[0][0])
                    queue.pop(0)
        return ans
