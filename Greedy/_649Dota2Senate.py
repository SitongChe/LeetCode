#https://leetcode.com/problems/dota2-senate/description/
#time O(n) space O(n)
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        Rqueue = []
        Dqueue = []
        n = len(senate)
        for i,c in enumerate(senate):
            if c=='R':
                Rqueue.append(i)
            else:
                Dqueue.append(i)
        while Rqueue and Dqueue:
            RIndex = Rqueue.pop(0)
            DIndex = Dqueue.pop(0)
            if RIndex<DIndex:
                Rqueue.append(RIndex+n)
            else:
                Dqueue.append(DIndex+n)
        return "Radiant" if Rqueue else "Dire"
