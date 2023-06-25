#https://leetcode.com/problems/longest-happy-string/description/
#time O(n log n) space O(N)
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxHeap = []
        for cnt, cur in [(-a,"a"),(-b,"b"),(-c,"c")]:
            if cnt != 0:
                heapq.heappush(maxHeap,(cnt,cur))
        heapq.heapify(maxHeap)
        ans = ""
        while maxHeap:
            cnt, cur = heapq.heappop(maxHeap)
            if len(ans)>=2 and ans[-1]==ans[-2]==cur:
                if not maxHeap:
                    return ans
                else:
                    cnt2, cur2 = heapq.heappop(maxHeap)
                    cnt2+=1
                    ans += cur2
                    if cnt2!=0:
                        heapq.heappush(maxHeap,(cnt2,cur2))
                    heapq.heappush(maxHeap,(cnt,cur))
            else:
                cnt+=1
                ans+=cur
                if cnt!=0:
                    heapq.heappush(maxHeap,(cnt,cur))
        return ans
