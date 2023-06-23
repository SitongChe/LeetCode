#https://leetcode.com/problems/reorganize-string/description/
#time O(Nlogk) space O(k) n is the length of the input string s, and k is the number of unique characters in s
class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxHeap = [(-v,c) for c,v in count.items()]
        heapq.heapify(maxHeap)
        ans = ""
        prev = None
        while maxHeap:
            cnt,c = heapq.heappop(maxHeap)
            ans += c
            cnt+=1
            if prev:
                heapq.heappush(maxHeap,prev)
                prev = None
            if cnt!=0:
                prev = (cnt,c)
                
        if len(ans)!=len(s):
            return ""
        return ans
                


