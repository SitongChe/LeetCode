#https://leetcode.com/problems/jump-game-vii/description/
#time O(N) space O(N)
#bfs
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if n == 0:
            return True
        r=0
        queue = [0]
        while queue:
            cur = queue.pop(0)
            for i in range(max(cur+minJump,r+1),min(cur+maxJump,n-1)+1):
                if s[i]=='0':
                    queue.append(i)
                    if i == n-1:
                        return True
            r = cur+maxJump
        return False


