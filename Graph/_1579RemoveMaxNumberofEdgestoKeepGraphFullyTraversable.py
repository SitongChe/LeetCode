#https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/
# time O(E + V * α(V)) space O(V) 
#union find
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        uf = {}
        def find(x):
            uf.setdefault(x,x)
            if x!=uf[x]:
                uf[x]=find(uf[x])
            return uf[x]
        def union(x,y):
            rootx=find(x)
            rooty=find(y)
            if rootx==rooty:
                return False
            uf[rootx]=rooty
            return True
        e1 = 0
        e2 = 0
        ans = 0
        for t,u,v in edges:
            if t == 3:
                if union(u,v):
                    e1+=1
                    e2+=1
                else:
                    ans+=1
        tmp = uf.copy()
        for t,u,v in edges:
            if t == 1:
                if union(u,v):
                    e1+=1
                else:
                    ans+=1
        uf = tmp
        for t,u,v in edges:
            if t == 2:
                if union(u,v):
                    e2+=1
                else:
                    ans +=1
        return ans if e1==n-1 and e2==n-1 else -1

        
