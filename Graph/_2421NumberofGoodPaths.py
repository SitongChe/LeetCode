#https://leetcode.com/problems/number-of-good-paths/
#time O(V^2) space O(E+V)
#dfs
class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        self.ans = 0
        def dfs(i,val):
            if i in visited:
                return
            visited.add(i)
            for node in graph[i]:
                if node not in visited:
                    if vals[node]==val:
                        self.ans+=1
                    if vals[node]<=val:
                        dfs(node,val)
        for i in range(len(vals)):
            visited = set()
            dfs(i,vals[i])
        return self.ans//2+len(vals)
 
#time O(E+V) space O(E+V)
#uf
class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        uf = {}
        rank = {}
        def find(x):
            uf.setdefault(x,x)
            rank.setdefault(x,0)
            if x!=uf[x]:
                uf[x]=find(uf[x])
            return uf[x]
        def union(x,y):
            rootx = find(x)
            rooty = find(y)
            if rootx == rooty:
                return False
            if rank[rootx]<rank[rooty]:
                uf[rootx]=rooty
                rank[rooty]+=rank[rootx]
            else:
                uf[rooty]=rootx
                rank[rootx]+=rank[rooty]
            return True
        
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        valToIndex = defaultdict(list)
        ans = 0
        for i,val in enumerate(vals):
            valToIndex[val].append(i)
        for val in sorted(valToIndex.keys()):
            for i in valToIndex[val]:
                for node in graph[i]:
                    if vals[node]<=val:
                        union(node,i)
            count = defaultdict(int)
            for i in valToIndex[val]:
                rooti = find(i)
                count[rooti]+=1
                ans+=count[rooti]
        return ans
        
