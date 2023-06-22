#https://leetcode.com/problems/matchsticks-to-square/description/
#time O(4^ n) space O(n)
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        def traceback(index,side,tmp):
            if side == 4:
                return True
            if tmp == target:
                return traceback(0,side+1,0)
            for i in range(index,n):
                if i not in visited and tmp +matchsticks[i]<=target:
                    if i>index and matchsticks[i]==matchsticks[i-1] and i-1 not in visited:
                        continue
                    visited.add(i)
                    if traceback(i+1,side,tmp+matchsticks[i]):
                        return True
                    visited.remove(i)

        total = sum(matchsticks)
        if total%4:
            return False
        target = total//4
        n = len(matchsticks)
        sides=[0]*4
        visited = set()
        return traceback(0,0,0)

        


