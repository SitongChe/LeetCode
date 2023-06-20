#https://leetcode.com/problems/top-k-frequent-elements/
#time O(n + m log m) ,space  O(m) n: the length of the nums list  m: number of distinct elements.
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        maxHeap = [[-cnt,v] for v,cnt in count.items()]
        heapq.heapify(maxHeap)
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(maxHeap)[1])
        return ans

