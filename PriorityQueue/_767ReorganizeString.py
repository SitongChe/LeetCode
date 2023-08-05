#https://leetcode.com/problems/reorganize-string/description/
#time O(Nlogk) space O(k) n is the length of the input string s, and k is the number of unique characters in s
class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        available = [[-cnt,c] for c,cnt in count.items()]
        heapq.heapify(available)
        unavailable = None
        ans = ""
        while available:
            negCnt,c = heapq.heappop(available)
            ans += c
            negCnt+=1
            if unavailable:
                heapq.heappush(available,unavailable)
                unavailable = None
            if negCnt:
                unavailable = [negCnt,c]
        if len(ans)==len(s):
            return ans
        return ""
            
