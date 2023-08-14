#https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/description/
#time O(1) space O(1)
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low%2:
            return ceil((high-low+1)/2)
        else:
            return (high-low+1)//2
