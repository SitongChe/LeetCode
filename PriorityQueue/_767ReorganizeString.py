#https://leetcode.com/problems/reorganize-string/description/
#time O(Nlogk) space O(k) n is the length of the input string s, and k is the number of unique characters in s
class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxHeap = [(-cnt,c) for c,cnt in count.items()]
        heapq.heapify(maxHeap)
        prev = None
        ans = ""
        while maxHeap:
            cnt, cur = heapq.heappop(maxHeap)
            ans += cur
            cnt+=1
            if prev:
                heapq.heappush(maxHeap,prev)
                prev = None
            if cnt != 0:
                prev = (cnt, cur)
        if len(ans)!=len(s):
            return ""
        return ans

