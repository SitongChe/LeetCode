#https://leetcode.com/problems/redundant-connection/
#time O(N * α(N)) space O(N)
#union find
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = {}
        def find(x):
            uf.setdefault(x,x)
            if x!=uf[x]:
                uf[x]=find(uf[x])
            return uf[x]
        def union(x,y):
            rootx = find(x)
            rooty = find(y)
            if rootx==rooty:
                return 0
            uf[rootx] = rooty
            return 1
        for x,y in edges:
            if union(x,y)==0:
                return [x,y]
            


