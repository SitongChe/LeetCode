#https://leetcode.com/problems/koko-eating-bananas/
#time O(NlogM), space O(1) N is the number of piles and M is the maximum pile size.
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        left = 1
        right = max(piles)
        while left+1<right:
            mid = left+(right-left)//2
            if sum(math.ceil(piles[i]/mid) for i in range(len(piles)))<=h:
                right = mid
            else:
                left = mid
        if sum(math.ceil(piles[i]/left) for i in range(len(piles)))<=h:
            return left
        return right
        
