#https://leetcode.com/problems/reconstruct-itinerary/
#time O(N^2) space O(N)
#traceback
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def traceback(cur):
            if len(ans) == len(tickets)+1:
                return True
            if cur in graph:
                size = len(graph[cur])
                for i in range(size):
                    node = graph[cur].popleft()
                    ans.append(node)
                    if traceback(node):
                        return True
                    ans.pop()
                    graph[cur].append(node)
            return False

        tickets.sort()
        graph = defaultdict(deque)
        for u,v in tickets:
            graph[u].append(v)
        ans = ["JFK"]
        traceback("JFK")
        return ans
