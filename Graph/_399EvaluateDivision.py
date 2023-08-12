#https://leetcode.com/problems/evaluate-division/description/
#time O(N + Q * α(N)) space  O(N)
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        uf = {}
        ratio = {}
        def find(x):
            uf.setdefault(x,x)
            ratio.setdefault(x,1)
            if x!=uf[x]:
                rootx,rx=find(uf[x])
                uf[x]=rootx
                ratio[x]*=rx
            return uf[x],ratio[x]
        def union(x,y,v):
            rootx,rx = find(x)
            rooty,ry = find(y)
            uf[rootx]=rooty
            ratio[rootx]=ry/rx*v

        for (x,y),v in zip(equations,values):
            union(x,y,v)
        return [find(x)[1]/find(y)[1] if x in uf and y in uf and find(x)[0]==find(y)[0] else -1 for x,y in queries]
 
 #time O(N * Q) space  O(N)
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def bfs(start,end):
            visited = set()
            queue = [[start,1]]
            while queue:
                cur,ratio = queue.pop(0)
                if cur == end:
                    return ratio
                for node,v in graph[cur]:
                    if node not in visited:
                        visited.add(node)
                        queue.append([node,v*ratio])
            return -1
                        
        graph = defaultdict(list)
        for (x,y),v in zip(equations,values):
            graph[x].append([y,v])
            graph[y].append([x,1/v])
        return [bfs(x,y) if x in graph and y in graph else -1 for x,y in queries]
