#https://leetcode.com/problems/reconstruct-itinerary/
#time O(N^2) space O(N)
#traceback
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        adjs = defaultdict(list)
        for u,v in tickets:
            adjs[u].append(v)
        ans = []
        def traceback(cur):
            ans.append(cur)
            if len(ans)==len(tickets)+1:
                return True
            if cur not in adjs:
                ans.pop()
                return False
            size = len(adjs[cur])
            for i in range(size):
                node = adjs[cur].pop(0)
                if traceback(node):
                    return True
                adjs[cur].append(node)
            ans.pop()
            return False
        traceback("JFK")
        return ans
        
