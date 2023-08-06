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


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        def traceback(i):
            if i == n:
                return True
            for j in range(4):
                if side[j]+matchsticks[i]<=target:
                    side[j]+=matchsticks[i]
                    if traceback(i+1):
                        return True
                    side[j]-=matchsticks[i]
            return False
        total = sum(matchsticks)
        if total % 4:
            return False
        target = total/4
        side = [0]*4
        n = len(matchsticks)
        matchsticks.sort(reverse=True)
        return traceback(0)
        


