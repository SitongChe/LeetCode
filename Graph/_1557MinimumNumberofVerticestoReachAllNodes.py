#https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/description/
#time O(E) space O(V)
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        count = Counter()
        for u,v in edges:
            count[v]+=1
        return [i for i in range(n) if count[i]==0]
        
#time O(E) space O(V)
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        return list(set(range(n))-set(v for u,v in edges))
 
#time O(E* α(N)) space O(V)
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        uf = {}
        def find(x):
            uf.setdefault(x, x)
            if x != uf[x]:
                uf[x] = find(uf[x])
            return uf[x]
        for u,v in edges:
            uf[v]=find(u)
        return set([find(i) for i in range(n)])
 
#time O(E+V) space O(E+V)
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        def dfs(u):
            visited.add(u)
            for v in graph[u]:
                if v not in visited:
                    dfs(v)
                elif v in ans:
                    ans.remove(v)
        ans = set()
        visited = set()
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
        for i in range(n):
            if i not in visited:
                ans.add(i)
                dfs(i)
        
        return list(ans)
