#https://leetcode.com/problems/longest-happy-string/description/
#time O(n log n) space O(N)
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxHeap = []
        for cnt,char in [[a,"a"],[b,"b"],[c,"c"]]:
            if cnt:
                maxHeap.append([-cnt,char])
        heapq.heapify(maxHeap)
        ans = ""
        while maxHeap:
            negCnt,char = heapq.heappop(maxHeap)
            if len(ans)>=2 and ans[-1]==char and ans[-2]==char:
                if not maxHeap:
                    return ans
                else:
                    negCnt2,char2 = heapq.heappop(maxHeap)
                    negCnt2+=1
                    ans+=char2
                    if negCnt2:
                        heapq.heappush(maxHeap,[negCnt2,char2])
                    heapq.heappush(maxHeap,[negCnt,char])
            else:
                negCnt+=1
                ans+=char
                if negCnt:
                    heapq.heappush(maxHeap,[negCnt,char])
        return ans
