#https://leetcode.com/problems/as-far-from-land-as-possible/description/
#time O(R + B) space O(R + B + N)
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        redGraph = defaultdict(list)
        blueGraph = defaultdict(list)
        for u,v in redEdges:
            redGraph[u].append(v)
        for u,v in blueEdges:
            blueGraph[u].append(v)
        ans = [-1]*n
        def bfs():
            step = 0
            visited = set()
            while queue:
                size = len(queue)
                for _ in range(size):
                    cur,color = queue.pop(0)
                    if ans[cur]==-1:
                        ans[cur]=step
                    if color!="R":
                        for node in redGraph[cur]:
                            if (node,"R") not in visited:
                                queue.append((node,"R"))
                                visited.add((node,"R"))
                    if color!="B":
                        for node in blueGraph[cur]:
                            if (node,"B") not in visited:
                                queue.append((node,"B"))
                                visited.add((node,"B"))
                step +=1
        queue = [[0,None]]
        bfs()

        return ans



        
