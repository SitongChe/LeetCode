#https://leetcode.com/problems/arranging-coins/description/
#time O(logN), space O(1)
class Solution:
    def arrangeCoins(self, n: int) -> int:
        left = 0
        right = n
        while left+1<right:
            mid = left+(right-left)//2
            total = (mid+1)*mid/2
            if total == n:
                return mid
            elif total<n:
                left = mid
            else:
                right = mid
        if (right+1)*right/2<=n:
            return right
        return left
