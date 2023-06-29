#https://leetcode.com/problems/pyramid-transition-matrix/description/
#time O(M^N) space O(n)
class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        def dfs(cur,top,index):
            if len(cur) == 1:
                return True
            if (cur,top,index) in memo:
                return memo[(cur,top,index)]
            if len(top)==len(cur)-1:
                return dfs(top,"",0)
            curBlock = cur[index:index+2]
            if curBlock not in allowedMap:
                memo[(cur,top,index)] = False
                return False
            for nextBlock in allowedMap[curBlock]:
                if dfs(cur,top+nextBlock,index+1):
                    memo[(cur,top,index)] = True
                    return True
            memo[(cur,top,index)] = False
            return False

        memo = {}
        allowedMap = defaultdict(list)
        for pattern in allowed:
            allowedMap[pattern[:2]].append(pattern[2])
        return dfs(bottom,"",0)
