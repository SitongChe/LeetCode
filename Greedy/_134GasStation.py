#https://leetcode.com/problems/jump-game-vii/description/
#time O(N) space O(1)
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        total = 0
        ans = 0
        for i,(g,c) in enumerate(zip(gas,cost)):
            total += g-c
            if total<0:
                total = 0
                ans = i+1
        return ans

        
